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
    if "CustomName:{text:" not in create:
        errors.append("container title is not a structured text component")
    if '"minecraft:custom_name":\'' in generated_functions or '"minecraft:lore" set value [\'' in generated_functions:
        errors.append("generated UI text still stores JSON as literal strings")
    if "transformation:{translation:" not in create:
        errors.append("workstation display has no explicit centering transformation")

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
