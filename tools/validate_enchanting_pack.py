from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "SuperAwesomeEnchanting"
DATA = PACK / "data"
VANILLA = ROOT / ".cache/minecraft/26.3-rc2/vanilla/data/minecraft"
REGISTRIES = ROOT / ".cache/minecraft/26.3-rc2/reports/reports/registries.json"
GENERATOR = ROOT / "tools/generate_enchanting_pack.py"
FANCYUI = ROOT / "FancyUI"


def constants() -> dict[str, Any]:
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"))
    result: dict[str, Any] = {}
    wanted = {"CATALYSTS", "CATEGORIES", "LOOT_POOLS", "LOOT_TABLE_POOLS"}
    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id in wanted:
            result[node.target.id] = ast.literal_eval(node.value)
    return result


def resolve_item_tag(spec: str, seen: frozenset[tuple[str, str]] = frozenset()) -> set[str]:
    if not spec.startswith("#"):
        return {spec if ":" in spec else f"minecraft:{spec}"}
    identifier = spec[1:]
    namespace, path = identifier.split(":", 1) if ":" in identifier else ("minecraft", identifier)
    key = (namespace, path)
    if key in seen or namespace != "minecraft":
        return set()
    source = VANILLA / "tags/item" / f"{path}.json"
    if not source.exists():
        return set()
    values = json.loads(source.read_text(encoding="utf-8"))["values"]
    return set().union(*(resolve_item_tag(value, seen | {key}) for value in values))


def main() -> int:
    errors: list[str] = []
    config = constants()

    for path in PACK.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")

    function_pattern = re.compile(r"(?:^|\brun\s+)function\s+([a-z0-9_.-]+):([a-z0-9_./-]+)")
    for path in DATA.rglob("*.mcfunction"):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            for match in function_pattern.finditer(line):
                namespace, function = match.groups()
                if namespace == "fancyui":
                    target = FANCYUI / "data/fancyui/function" / f"{function}.mcfunction"
                else:
                    target = DATA / namespace / "function" / f"{function}.mcfunction"
                if not target.exists():
                    errors.append(f"missing function: {path.relative_to(ROOT)}:{line_number}: {namespace}:{function}")

    registries = json.loads(REGISTRIES.read_text(encoding="utf-8"))
    items = set(registries["minecraft:item"]["entries"])
    used_items = {f"minecraft:{entry[0]}" for entry in config["CATALYSTS"].values()}
    used_items.update(f"minecraft:{item}" for group in config["CATEGORIES"].values() for item in group)
    for item in sorted(used_items - items):
        errors.append(f"catalogue references missing 26.3 item: {item}")

    enchantments = {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in (VANILLA / "enchantment").glob("*.json")
    }
    catalogued = set(config["CATALYSTS"])
    if catalogued != set(enchantments):
        errors.append(f"catalogue mismatch: missing={sorted(set(enchantments) - catalogued)}, extra={sorted(catalogued - set(enchantments))}")

    catalysts = {entry[0] for entry in config["CATALYSTS"].values()}
    for category, category_items in config["CATEGORIES"].items():
        for item in category_items:
            item_id = f"minecraft:{item}"
            for catalyst in catalysts:
                applicable = [
                    enchantment
                    for enchantment, (candidate, _, _) in config["CATALYSTS"].items()
                    if candidate == catalyst and item_id in resolve_item_tag(enchantments[enchantment]["supported_items"])
                ]
                if len(applicable) > 1:
                    errors.append(f"ambiguous equipment catalyst: {category}/{item} + {catalyst}: {applicable}")

    mending = json.loads((DATA / "minecraft/enchantment/mending.json").read_text(encoding="utf-8"))
    if mending.get("description") != {"text": "Unbreakable"}:
        errors.append("minecraft:mending is not presented as Unbreakable")
    if set(mending.get("effects", {})) != {"minecraft:item_damage"}:
        errors.append("Unbreakable still has an unwanted Mending effect")

    add_unbreakable = json.loads(
        (DATA / "sae/item_modifier/maintenance/add_unbreakable.json").read_text(encoding="utf-8")
    )
    enchantment_step = next(
        (
            step
            for step in add_unbreakable.get("functions", [])
            if step.get("type") == "minecraft:set_enchantments"
        ),
        None,
    )
    if enchantment_step is None or enchantment_step.get("add") is not False:
        errors.append("automatic Unbreakable maintenance increments its level instead of setting level I")

    for tag_name in ("on_random_loot", "tradeable", "treasure"):
        values = json.loads((DATA / f"minecraft/tags/enchantment/{tag_name}.json").read_text(encoding="utf-8"))["values"]
        if "minecraft:mending" in values:
            errors.append(f"Unbreakable remains directly obtainable through #{tag_name}")

    # Client-facing UI regressions. These checks deliberately inspect the generated
    # commands at the same seam Minecraft reads, rather than trusting the generator.
    generated_functions = "\n".join(
        path.read_text(encoding="utf-8") for path in DATA.rglob("*.mcfunction")
    )
    create = (DATA / "sae/function/workstation/place/create.mcfunction").read_text(encoding="utf-8")
    if (DATA / "sae_ui").exists():
        errors.append("FancyUI is still embedded under the sae_ui namespace")
    if "sae_ui" in generated_functions:
        errors.append("generated SAE functions still reference the embedded sae_ui fork")
    if "function fancyui:initialize_all" not in create:
        errors.append("workstation does not initialize through the FancyUI dependency")
    if "unless score version fancyui.master matches 1.. run return" not in create:
        errors.append("workstation does not stop safely when FancyUI is missing")
    elif create.index("unless score version fancyui.master") > create.index("setblock ~ ~ ~ minecraft:chest"):
        errors.append("missing FancyUI can replace an Enchanting Table with a chest")
    if 'criteria:"*"' not in create:
        errors.append("workstation watch slots do not accept arbitrary inserted items")
    if create.count('type:"watch"') != 2 or 'Slot:10b,type:"watch"' not in create or 'Slot:11b,type:"watch"' not in create:
        errors.append("workstation does not expose exactly the target/source and destination input slots")
    if create.count('type:"button"') != 24 or create.count('action:"empty"') != 21:
        errors.append("workstation does not reserve eighteen contextual Enchanting option controls")
    if any(action in create for action in ('tab_armor', 'tab_melee', 'tab_ranged', 'tab_tools', 'tab_movement', 'tab_curses')):
        errors.append("workstation still contains category-first navigation")
    if "CustomName:{text:" not in create:
        errors.append("container title is not a structured text component")
    if '"minecraft:custom_name":\'' in generated_functions or '"minecraft:lore" set value [\'' in generated_functions:
        errors.append("generated UI text still stores JSON as literal strings")
    if "transformation:{translation:" not in create:
        errors.append("workstation display has no explicit centering transformation")
    load_function = (DATA / "sae/function/load.mcfunction").read_text(encoding="utf-8")
    tick_function = (DATA / "sae/function/tick.mcfunction").read_text(encoding="utf-8")
    if "scoreboard objectives add sae.vanilla trigger" not in load_function:
        errors.append("vanilla-workstation conversion does not register its trigger command")
    if "scoreboard players enable @a sae.vanilla" not in tick_function:
        errors.append("players cannot run /trigger sae.vanilla")
    if "function sae:workstation/restore_vanilla/start" not in tick_function:
        errors.append("the sae.vanilla trigger does not dispatch workstation conversion")
    if (DATA / "sae/advancement/restore_vanilla_workstation.json").exists():
        errors.append("the unreliable Redstone Torch interaction advancement still exists")
    restore_start = (DATA / "sae/function/workstation/restore_vanilla/start.mcfunction").read_text(encoding="utf-8")
    if "@n[type=marker,tag=sae.workstation,distance=..6]" not in restore_start:
        errors.append("the sae.vanilla trigger does not select the nearest workstation within six blocks")
    if "raycast" in restore_start or (DATA / "sae/function/workstation/restore_vanilla/raycast.mcfunction").exists():
        errors.append("the sae.vanilla trigger still depends on unreliable look-direction raycasting")
    restore_apply = (DATA / "sae/function/workstation/restore_vanilla/apply.mcfunction").read_text(encoding="utf-8")
    if "function sae:workstation/unregister" not in restore_apply or "function sae:workstation/uninstall_one" not in restore_apply:
        errors.append("vanilla-workstation opt-out does not unregister and safely restore the table")
    transfer_preview = (DATA / "sae/function/transfer/preview.mcfunction").read_text(encoding="utf-8")
    transfer_apply = (DATA / "sae/function/transfer/apply.mcfunction").read_text(encoding="utf-8")
    if "amethyst_block" in transfer_preview + transfer_apply or "consume_transfer_catalyst" in generated_functions:
        errors.append("enchantment transfer still charges an Amethyst Catalyst")
    if "sae.cooldown 6" not in generated_functions or "sae.timer 60" not in generated_functions:
        errors.append("one-click purchases do not implement the agreed cooldown and arming window")
    option_place = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (DATA / "sae/function/workstation/options/place").glob("*.mcfunction")
    )
    expected_option_slots = {str(slot) for slot in (*range(3, 9), *range(12, 18), *range(21, 27))}
    actual_option_slots = {path.stem for path in (DATA / "sae/function/workstation/options/place").glob("*.mcfunction")}
    if actual_option_slots != expected_option_slots:
        errors.append("Enchanting options do not form the expected three-by-six Catalyst grid")
    equipment_order = re.findall(
        r"function sae:workstation/options/equipment/([a-z_]+)",
        (DATA / "sae/function/workstation/options/equipment.mcfunction").read_text(encoding="utf-8"),
    )
    if equipment_order[-2:] != ["binding_curse", "vanishing_curse"]:
        errors.append("equipment Enchanting options do not place curses last")
    book_order: list[str] = []
    for page in (0, 1):
        book_order.extend(re.findall(
            r"function sae:workstation/options/book/([a-z_]+)",
            (DATA / f"sae/function/workstation/options/book_page_{page}.mcfunction").read_text(encoding="utf-8"),
        ))
    if book_order[-2:] != ["iron_chain", "glass"]:
        errors.append("Book Enchanting options do not place curses last")
    if "].id set" in option_place or '"minecraft:item_model"' not in option_place:
        errors.append("rendered controls replace FancyUI's physical button item instead of its vanilla item model")
    enchant_controls = (DATA / "sae/function/workstation/options/render_enchant_controls.mcfunction").read_text(encoding="utf-8")
    if "function sae:workstation/destination_guard/show" not in enchant_controls:
        errors.append("Enchant mode leaves the Transfer destination watch exposed")
    input_changed = (DATA / "sae/function/workstation/input_changed.mcfunction").read_text(encoding="utf-8")
    if "return_inactive_destination" in input_changed or 'callback_data{slot:11}' not in input_changed or input_changed.count("function sae:workstation/session/claim") < 2:
        errors.append("Transfer item inserted before Source is dropped instead of claiming a session and remaining in its slot")
    transfer_render = (DATA / "sae/function/transfer/render.mcfunction").read_text(encoding="utf-8")
    if "].id set" in enchant_controls or "].id set" in transfer_render:
        errors.append("mode-specific controls replace FancyUI's fixed physical items")
    if not all(label in transfer_render for label in ('Slot:1b', 'Slot:2b', 'Slot:4b', 'Slot:10b', 'Slot:11b', 'Slot:12b', 'Slot:13b', 'Slot:18b', 'text:"Source"', 'text:"Transfer item"', 'text:"Result"', 'action:"mode_toggle"')):
        errors.append("Transfer mode does not render the dedicated left-to-right output workflow")
    transfer_preview = (DATA / "sae/function/transfer/render_preview.mcfunction").read_text(encoding="utf-8")
    if 'action:"transfer_take"' not in transfer_preview or (DATA / "sae/function/workstation/transfer_confirm.mcfunction").exists():
        errors.append("Transfer still uses a confirmation control instead of taking the Result")
    if not all(component in transfer_preview for component in ('"minecraft:item_model"', '"minecraft:enchantments"', '"minecraft:enchantment_glint_override"', "function sae:transfer/render_preview_book")):
        errors.append("Transfer Result does not visually preview the completed enchanted item")
    if "function sae:transfer/preview_line/" in transfer_preview or (DATA / "sae/function/transfer/preview_line").exists():
        errors.append("Transfer Result duplicates native enchantment subtitles in custom lore")
    transfer_book_preview = (DATA / "sae/function/transfer/render_preview_book.mcfunction").read_text(encoding="utf-8")
    if '"minecraft:stored_enchantments"' not in transfer_book_preview:
        errors.append("Book transfers do not preview their stored enchantments")
    delivery = (DATA / "sae/function/transfer/deliver_one.mcfunction").read_text(encoding="utf-8")
    if "player.cursor" not in delivery or "function sae:transfer/deliver_drop" not in delivery:
        errors.append("Transfer Result delivery does not protect an occupied player cursor")
    transfer_apply = (DATA / "sae/function/transfer/apply.mcfunction").read_text(encoding="utf-8")
    apply_selection = (DATA / "sae/function/workstation/apply_selection.mcfunction").read_text(encoding="utf-8")
    if "function fancyui:manual_removal" not in transfer_apply or "function fancyui:manual_placement" not in transfer_apply:
        errors.append("transfer mutation does not synchronize FancyUI's watched source and result slots")
    if "function fancyui:manual_placement" not in apply_selection:
        errors.append("enchanting mutation does not synchronize FancyUI's watched target slot")

    if not (FANCYUI / "pack.mcmeta").exists():
        errors.append("private FancyUI dependency is missing")
    else:
        button_ui = (FANCYUI / "data/fancyui/function/ui/init/slot/append_button.mcfunction").read_text(encoding="utf-8")
        background_ui = (FANCYUI / "data/fancyui/function/ui/init/slot/append_background.mcfunction").read_text(encoding="utf-8")
        safety_tick = (FANCYUI / "data/fancyui/function/ui/safety/tick.mcfunction").read_text(encoding="utf-8")
        inventory_recovery = (FANCYUI / "data/fancyui/function/ui/safety/fixed/inventory/on_detect.mcfunction").read_text(encoding="utf-8")
        received = json.loads((FANCYUI / "data/fancyui/advancement/ui/safety/fixed/received.json").read_text(encoding="utf-8"))
        received_item = received["criteria"]["fancyui.fixed.received"]["conditions"]["items"][0]
        if "hide_tooltip:true" in button_ui:
            errors.append("FancyUI buttons still suppress their hover text")
        if "fancyui:item" in button_ui or '"minecraft:item_model"' in button_ui + background_ui:
            errors.append("FancyUI dependency still requires its resource pack")
        if 'id:"minecraft:stone_button"' not in button_ui or 'id:"minecraft:gray_stained_glass_pane"' not in background_ui:
            errors.append("FancyUI dependency does not use the vanilla no-resource-pack controls")
        if "#fancyui:ui_placeholders" in safety_tick + inventory_recovery or "items" in received_item:
            errors.append("FancyUI fixed-item recovery is still limited to a hard-coded item tag")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    json_count = sum(1 for _ in PACK.rglob("*.json"))
    function_count = sum(1 for _ in DATA.rglob("*.mcfunction"))
    print(f"Validated {json_count} JSON files and {function_count} functions.")
    print(f"Catalogue covers all {len(enchantments)} enchantments with no equipment catalyst collisions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
