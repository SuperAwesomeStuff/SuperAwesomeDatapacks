from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "SuperAwesomeEnchanting"
DATA = PACK / "data"
VANILLA = ROOT / ".cache/minecraft/26.3-rc2/vanilla/data/minecraft"
FANCYUI = ROOT / "FancyUI"


CATALYSTS: dict[str, tuple[str, int, str]] = {
    "aqua_affinity": ("sponge", 1, "Armor"),
    "bane_of_arthropods": ("spider_eye", 1, "Melee"),
    "blast_protection": ("obsidian", 1, "Armor"),
    "breach": ("amethyst_block", 1, "Melee"),
    "channeling": ("lightning_rod", 1, "Ranged"),
    "binding_curse": ("iron_chain", 1, "Curses"),
    "vanishing_curse": ("glass", 1, "Curses"),
    "density": ("gold_block", 1, "Melee"),
    "depth_strider": ("nautilus_shell", 1, "Movement and water"),
    "efficiency": ("redstone_block", 1, "Tools"),
    "feather_falling": ("slime_block", 1, "Movement and water"),
    "fire_aspect": ("blaze_rod", 1, "Melee"),
    "fire_protection": ("magma_cream", 1, "Armor"),
    "flame": ("blaze_rod", 1, "Ranged"),
    "fortune": ("diamond_block", 1, "Tools"),
    "frost_walker": ("blue_ice", 1, "Movement and water"),
    "impaling": ("prismarine_shard", 1, "Ranged"),
    "infinity": ("spectral_arrow", 64, "Ranged"),
    "knockback": ("piston", 1, "Melee"),
    "looting": ("gold_block", 1, "Melee"),
    "loyalty": ("ender_pearl", 1, "Ranged"),
    "luck_of_the_sea": ("pufferfish", 1, "Movement and water"),
    "lunge": ("breeze_rod", 1, "Melee"),
    "lure": ("tropical_fish", 1, "Movement and water"),
    "mending": ("netherite_ingot", 1, "Tools"),
    "multishot": ("dispenser", 1, "Ranged"),
    "piercing": ("amethyst_block", 1, "Ranged"),
    "power": ("amethyst_block", 1, "Ranged"),
    "projectile_protection": ("shield", 1, "Armor"),
    "protection": ("diamond", 1, "Armor"),
    "punch": ("piston", 1, "Ranged"),
    "quick_charge": ("redstone_block", 1, "Ranged"),
    "respiration": ("turtle_scute", 1, "Movement and water"),
    "riptide": ("nautilus_shell", 1, "Movement and water"),
    "sharpness": ("amethyst_block", 1, "Melee"),
    "silk_touch": ("slime_block", 1, "Tools"),
    "smite": ("glowstone", 1, "Melee"),
    "soul_speed": ("soul_sand", 1, "Movement and water"),
    "sweeping_edge": ("breeze_rod", 1, "Melee"),
    "swift_sneak": ("sculk_sensor", 1, "Movement and water"),
    "thorns": ("pointed_dripstone", 1, "Armor"),
    "unbreaking": ("iron_block", 1, "Tools"),
    "wind_burst": ("breeze_rod", 1, "Melee"),
}

SHARED = {
    "amethyst_block": ["breach", "piercing", "power", "sharpness"],
    "blaze_rod": ["fire_aspect", "flame"],
    "breeze_rod": ["lunge", "sweeping_edge", "wind_burst"],
    "gold_block": ["density", "looting"],
    "nautilus_shell": ["depth_strider", "riptide"],
    "piston": ["knockback", "punch"],
    "redstone_block": ["efficiency", "quick_charge"],
    "slime_block": ["feather_falling", "silk_touch"],
}

LOOT_POOLS: dict[str, list[str]] = {
    "mineshaft": ["efficiency", "fortune", "silk_touch", "unbreaking", "feather_falling"],
    "ancient_city": ["efficiency", "silk_touch", "protection", "projectile_protection", "feather_falling", "respiration", "unbreaking", "thorns"],
    "desert_pyramid": ["blast_protection", "fire_protection", "thorns", "unbreaking"],
    "jungle_temple": ["bane_of_arthropods", "infinity", "punch", "projectile_protection", "unbreaking"],
    "pillager_outpost": ["multishot", "piercing", "quick_charge", "projectile_protection", "unbreaking"],
    "dungeon": ["sharpness", "smite", "bane_of_arthropods", "protection", "unbreaking"],
    "stronghold_corridor": ["protection", "projectile_protection", "sharpness", "efficiency", "fortune", "unbreaking"],
    "stronghold_crossing": ["protection", "projectile_protection", "sharpness", "efficiency", "fortune", "unbreaking", "feather_falling", "looting"],
    "underwater_ruin": ["aqua_affinity", "respiration", "depth_strider", "luck_of_the_sea", "lure"],
    "woodland_mansion": ["protection", "projectile_protection", "thorns", "sharpness", "smite", "bane_of_arthropods", "looting", "unbreaking"],
    "fishing": ["luck_of_the_sea", "lure", "unbreaking", "respiration", "frost_walker"],
    "vault_combat": ["sharpness", "bane_of_arthropods", "efficiency", "fortune", "silk_touch", "feather_falling"],
    "vault_aquatic": ["riptide", "loyalty", "channeling", "impaling", "aqua_affinity"],
    "ominous_combat": ["knockback", "punch", "smite", "looting", "multishot"],
    "ominous_mace": ["breach", "density"],
    "stronghold_library": [],
    "swift_sneak": ["swift_sneak"],
    "soul_speed": ["soul_speed"],
    "wind_burst": ["wind_burst"],
}

LOOT_TABLE_POOLS: dict[str, list[str]] = {
    "chests/abandoned_mineshaft": ["mineshaft"],
    "chests/ancient_city": ["swift_sneak", "ancient_city"],
    "chests/bastion_other": ["soul_speed"],
    "chests/desert_pyramid": ["desert_pyramid"],
    "chests/jungle_temple": ["jungle_temple"],
    "chests/pillager_outpost": ["pillager_outpost"],
    "chests/simple_dungeon": ["dungeon"],
    "chests/stronghold_corridor": ["stronghold_corridor"],
    "chests/stronghold_crossing": ["stronghold_crossing"],
    "chests/stronghold_library": ["stronghold_library"],
    "chests/underwater_ruin_big": ["underwater_ruin"],
    "chests/woodland_mansion": ["woodland_mansion"],
    "chests/trial_chambers/reward_rare": ["vault_combat", "vault_aquatic"],
    "chests/trial_chambers/reward_ominous_rare": ["ominous_combat", "ominous_mace", "wind_burst"],
    "gameplay/fishing/treasure": ["fishing"],
    "gameplay/piglin_bartering": ["soul_speed"],
}

CATEGORIES: dict[str, list[str]] = {
    "helmet": ["leather_helmet", "chainmail_helmet", "copper_helmet", "iron_helmet", "golden_helmet", "diamond_helmet", "netherite_helmet", "turtle_helmet"],
    "chestplate": ["leather_chestplate", "chainmail_chestplate", "copper_chestplate", "iron_chestplate", "golden_chestplate", "diamond_chestplate", "netherite_chestplate"],
    "leggings": ["leather_leggings", "chainmail_leggings", "copper_leggings", "iron_leggings", "golden_leggings", "diamond_leggings", "netherite_leggings"],
    "boots": ["leather_boots", "chainmail_boots", "copper_boots", "iron_boots", "golden_boots", "diamond_boots", "netherite_boots"],
    "sword": ["wooden_sword", "stone_sword", "copper_sword", "iron_sword", "golden_sword", "diamond_sword", "netherite_sword"],
    "axe": ["wooden_axe", "stone_axe", "copper_axe", "iron_axe", "golden_axe", "diamond_axe", "netherite_axe"],
    "pickaxe": ["wooden_pickaxe", "stone_pickaxe", "copper_pickaxe", "iron_pickaxe", "golden_pickaxe", "diamond_pickaxe", "netherite_pickaxe"],
    "shovel": ["wooden_shovel", "stone_shovel", "copper_shovel", "iron_shovel", "golden_shovel", "diamond_shovel", "netherite_shovel"],
    "hoe": ["wooden_hoe", "stone_hoe", "copper_hoe", "iron_hoe", "golden_hoe", "diamond_hoe", "netherite_hoe"],
    "spear": ["wooden_spear", "stone_spear", "copper_spear", "iron_spear", "golden_spear", "diamond_spear", "netherite_spear"],
    "bow": ["bow"], "crossbow": ["crossbow"], "mace": ["mace"], "trident": ["trident"],
    "shield": ["shield"], "elytra": ["elytra"], "fishing_rod": ["fishing_rod"], "shears": ["shears"],
    "brush": ["brush"], "flint_and_steel": ["flint_and_steel"], "carrot_on_a_stick": ["carrot_on_a_stick"],
    "warped_fungus_on_a_stick": ["warped_fungus_on_a_stick"],
}


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def minecraft_id(name: str) -> str:
    return name if ":" in name or name.startswith("#") else f"minecraft:{name}"


def load_enchantment(name: str) -> dict[str, Any]:
    return json.loads((VANILLA / "enchantment" / f"{name}.json").read_text(encoding="utf-8"))


def install_enchantments() -> dict[str, int]:
    maximums: dict[str, int] = {}
    out = DATA / "minecraft/enchantment"
    for src in sorted((VANILLA / "enchantment").glob("*.json")):
        value = json.loads(src.read_text(encoding="utf-8"))
        maximums[src.stem] = int(value["max_level"])
        value["anvil_cost"] = 1
        if src.stem == "mending":
            value["description"] = {"text": "Unbreakable"}
            value["effects"] = {
                "minecraft:item_damage": [
                    {"effect": {"type": "minecraft:set", "value": 0.0}}
                ]
            }
        write_json(out / src.name, value)

    tags = DATA / "minecraft/tags/enchantment"
    write_json(tags / "exclusive_set/bow.json", {"values": ["minecraft:infinity"]})
    random_values = ["#minecraft:non_treasure", "minecraft:binding_curse", "minecraft:vanishing_curse", "minecraft:frost_walker"]
    write_json(tags / "on_random_loot.json", {"values": random_values})
    write_json(tags / "tradeable.json", {"values": random_values})
    write_json(tags / "treasure.json", {"values": ["minecraft:binding_curse", "minecraft:vanishing_curse", "minecraft:swift_sneak", "minecraft:soul_speed", "minecraft:frost_walker", "minecraft:wind_burst"]})
    return maximums


def install_item_tags() -> None:
    tag_root = DATA / "sae/tags/item"
    for name, values in CATEGORIES.items():
        write_json(tag_root / f"transfer/{name}.json", {"values": [minecraft_id(v) for v in values]})
    netherite = [v for values in CATEGORIES.values() for v in values if v.startswith("netherite_")]
    write_json(tag_root / "netherite_equipment.json", {"values": [minecraft_id(v) for v in netherite]})


def max_modifier(original: dict[str, Any], pool: list[str], maximums: dict[str, int]) -> dict[str, Any]:
    fixes = []
    for enchantment in pool:
        fixes.append({
            "type": "minecraft:filtered",
            "item_filter": {
                "predicates": {
                    "minecraft:stored_enchantments": [{"enchantments": f"minecraft:{enchantment}"}]
                }
            },
            "on_pass": {
                "type": "minecraft:set_enchantments",
                "enchantments": {f"minecraft:{enchantment}": maximums[enchantment]},
                "add": True,
            },
        })
    return {"type": "minecraft:sequence", "functions": [original, *fixes]}


def install_loot(maximums: dict[str, int]) -> None:
    general = [e for e in CATALYSTS if e not in {"mending", "binding_curse", "vanishing_curse", "swift_sneak", "soul_speed", "wind_burst"}]
    LOOT_POOLS["stronghold_library"] = general
    tag_root = DATA / "sae/tags/enchantment/loot"
    for name, pool in LOOT_POOLS.items():
        write_json(tag_root / f"{name}.json", {"values": [f"minecraft:{v}" for v in pool]})

    for table_id, assignments in LOOT_TABLE_POOLS.items():
        source = VANILLA / "loot_table" / f"{table_id}.json"
        value = json.loads(source.read_text(encoding="utf-8"))
        found = 0

        def visit(node: Any) -> None:
            nonlocal found
            if isinstance(node, list):
                for child in node:
                    visit(child)
                return
            if not isinstance(node, dict):
                return
            if node.get("name") == "minecraft:book" and isinstance(node.get("modifier"), dict) and node["modifier"].get("type") in {"minecraft:enchant_randomly", "minecraft:enchant_with_levels", "minecraft:set_enchantments"}:
                if found >= len(assignments):
                    raise RuntimeError(f"Too many enchanted Book entries in {table_id}")
                pool_name = assignments[found]
                original = node["modifier"]
                if original["type"] == "minecraft:set_enchantments":
                    original["enchantments"] = {
                        f"minecraft:{enchantment}": maximums[enchantment]
                        for enchantment in LOOT_POOLS[pool_name]
                    }
                else:
                    original["options"] = f"#sae:loot/{pool_name}"
                    node["modifier"] = max_modifier(original, LOOT_POOLS[pool_name], maximums)
                found += 1
            for child in node.values():
                visit(child)

        visit(value)
        if found != len(assignments):
            raise RuntimeError(f"Expected {len(assignments)} enchanted Book entries in {table_id}, found {found}")
        write_json(DATA / "minecraft/loot_table" / f"{table_id}.json", value)


def install_recipe() -> None:
    write_json(DATA / "sae/recipe/sponge.json", {
        "type": "minecraft:crafting_shapeless",
        "category": "building",
        "ingredients": ["minecraft:prismarine_crystals", "minecraft:prismarine_crystals", "minecraft:kelp", "minecraft:kelp"],
        "result": {"id": "minecraft:sponge"},
    })


def install_metadata() -> None:
    write_json(PACK / "pack.mcmeta", {
        "pack": {
            "description": "Super Awesome Enchanting for Minecraft Java 26.3",
            "min_format": 121,
            "max_format": 121,
        }
    })


def button(slot: int, item: str, name: str, action: str, lore: str = "") -> str:
    lore_part = f',"minecraft:lore":[{{text:"{lore}",color:"gray",italic:false}}]' if lore else ""
    return (
        f'{{Slot:{slot}b,type:"button",id:"minecraft:{item}",components:{{'
        f'"minecraft:custom_name":{{text:"{name}",color:"white",italic:false}}'
        f'{lore_part},"minecraft:custom_data":{{sae:{{action:"{action}"}}}}}},'
        f'callback:{{function:"sae:workstation/button"}}}}'
    )


def watch(slot: int) -> str:
    return (
        f'{{Slot:{slot}b,type:"watch",criteria:"*",callback:{{function:"sae:workstation/input_changed",data:{{slot:{slot}}}}},'
        f'removal_callback:{{function:"sae:workstation/input_changed",data:{{slot:{slot}}}}}}}'
    )


def background(slot: int) -> str:
    return f'{{Slot:{slot}b,type:"background"}}'


def install_runtime(maximums: dict[str, int]) -> None:
    fn = DATA / "sae/function"

    write_text(fn / "load.mcfunction", """
scoreboard objectives add sae.tmp dummy
scoreboard objectives add sae.clock dummy
scoreboard objectives add sae.uuid0 dummy
scoreboard objectives add sae.uuid1 dummy
scoreboard objectives add sae.uuid2 dummy
scoreboard objectives add sae.uuid3 dummy
scoreboard objectives add sae.deaths deathCount
scoreboard players set #clock sae.clock 0
scoreboard players set #dependency_notice sae.tmp 0
execute unless data storage sae:registry next_id run data modify storage sae:registry next_id set value 0
data modify storage sae:catalog version set value "26.3-rc-2"
tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Loaded for Java 26.3 RC2","color":"aqua"}]
""")
    write_text(fn / "tick.mcfunction", """
scoreboard players add #clock sae.clock 1
execute unless score #dependency_notice sae.tmp matches 1 run function sae:dependency/check
execute if score #clock sae.clock matches 20.. run function sae:maintenance/tick
execute if score #clock sae.clock matches 20.. run scoreboard players set #clock sae.clock 0
execute as @e[type=marker,tag=sae.workstation] at @s run function sae:workstation/tick
execute as @e[type=hopper_minecart,tag=sae.hopper_blocked] at @s unless entity @e[type=marker,tag=sae.workstation,distance=..2] run data modify entity @s Enabled set value true
execute as @e[type=hopper_minecart,tag=sae.hopper_blocked] at @s unless entity @e[type=marker,tag=sae.workstation,distance=..2] run tag @s remove sae.hopper_blocked
execute as @a[scores={sae.deaths=1..}] run function sae:escrow/on_death
scoreboard players set @a[scores={sae.deaths=1..}] sae.deaths 0
execute as @a at @s run function sae:escrow/return
""")
    write_text(fn / "dependency/check.mcfunction", """
scoreboard players set #dependency_notice sae.tmp 1
execute unless score version fancyui.master matches 1.. run tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Missing or incompatible FancyUI datapack. Install the included private compatibility fork.","color":"red"}]
""")

    write_text(fn / "workstation/place/start.mcfunction", """
advancement revoke @s only sae:place_workstation
scoreboard players set #ray sae.tmp 0
scoreboard players set #found sae.tmp 0
execute anchored eyes positioned ^ ^ ^0.25 run function sae:workstation/place/raycast
""")
    write_text(fn / "workstation/place/raycast.mcfunction", """
execute if block ~ ~ ~ minecraft:enchanting_table align xyz run function sae:workstation/place/create
execute if score #found sae.tmp matches 1 run return 1
scoreboard players add #ray sae.tmp 1
execute if score #ray sae.tmp matches ..24 positioned ^ ^ ^0.25 run function sae:workstation/place/raycast
""")

    slots: list[str] = []
    slots.extend([
        button(0, "iron_chestplate", "Armor recipes", "tab_armor"),
        button(1, "iron_sword", "Melee recipes", "tab_melee"),
        button(2, "bow", "Ranged recipes", "tab_ranged"),
        button(3, "iron_pickaxe", "Tool recipes", "tab_tools"),
        button(4, "nautilus_shell", "Movement and water", "tab_movement"),
        button(5, "iron_chain", "Curse recipes", "tab_curses"),
        button(6, "arrow", "Previous page", "previous"),
        button(7, "enchanting_table", "Enchant mode", "mode_enchant"),
        button(8, "amethyst_block", "Transfer mode", "mode_transfer"),
        background(9), watch(10), background(11), watch(12), background(13), watch(14), background(15),
        button(16, "barrier", "Cannot confirm", "confirm", "Insert valid items"),
        button(17, "arrow", "Next page", "next"),
    ])
    slots.extend(button(i, "book", "Recipe", "reference") for i in range(18, 27))
    slot_snbt = ",".join(slots)
    create = f"""
scoreboard players set #found sae.tmp 1
execute unless score version fancyui.master matches 1.. run return run tellraw @s {{"text":"Super Awesome Enchanting requires the included FancyUI compatibility datapack.","color":"red"}}
setblock ~ ~ ~ minecraft:chest
execute unless entity @e[type=marker,tag=sae.workstation,distance=..1] run summon marker ~ ~0.5 ~ {{Tags:["sae.workstation","fancyui","fancyui.container"]}}
execute as @n[type=marker,tag=sae.workstation,distance=..1] run data modify entity @s data set value {{container:"minecraft:chest",container_data:{{CustomName:{{text:"Super Awesome Enchanting"}}}},on_break:"sae:workstation/on_break",slots:[{slot_snbt}],sae:{{mode:"enchant",category:"Armor",page:0}}}}
execute as @n[type=marker,tag=sae.workstation,distance=..1] run function sae:workstation/register
execute as @n[type=marker,tag=sae.workstation,distance=..1] at @s run function fancyui:initialize_all
summon block_display ~ ~ ~ {{Tags:["sae.workstation.display"],block_state:{{id:"minecraft:enchanting_table"}},transformation:{{translation:[-0.001f,0f,-0.001f],left_rotation:[0f,0f,0f,1f],scale:[1.002f,1.18f,1.002f],right_rotation:[0f,0f,0f,1f]}}}}
execute as @n[type=marker,tag=sae.workstation,distance=..1] at @s run function sae:workstation/render
"""
    write_text(fn / "workstation/place/create.mcfunction", create)

    write_text(fn / "workstation/tick.mcfunction", """
execute if block ~ ~-1 ~ minecraft:hopper run data modify block ~ ~-1 ~ TransferCooldown set value 20
execute if block ~ ~1 ~ minecraft:hopper run data modify block ~ ~1 ~ TransferCooldown set value 20
execute if block ~1 ~ ~ minecraft:hopper run data modify block ~1 ~ ~ TransferCooldown set value 20
execute if block ~-1 ~ ~ minecraft:hopper run data modify block ~-1 ~ ~ TransferCooldown set value 20
execute if block ~ ~ ~1 minecraft:hopper run data modify block ~ ~ ~1 TransferCooldown set value 20
execute if block ~ ~ ~-1 minecraft:hopper run data modify block ~ ~ ~-1 TransferCooldown set value 20
tag @e[type=hopper_minecart,distance=..2] add sae.hopper_blocked
execute as @e[type=hopper_minecart,distance=..2] run data modify entity @s Enabled set value false
execute if entity @s[tag=sae.session] run function sae:workstation/session/check_owner
""")

    write_text(fn / "workstation/session/check_owner.mcfunction", """
scoreboard players set #online sae.tmp 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a store result score @s sae.uuid0 run data get entity @s UUID[0]
execute as @a store result score @s sae.uuid1 run data get entity @s UUID[1]
execute as @a store result score @s sae.uuid2 run data get entity @s UUID[2]
execute as @a store result score @s sae.uuid3 run data get entity @s UUID[3]
execute as @a if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run scoreboard players set #online sae.tmp 1
execute if score #online sae.tmp matches 0 run function sae:escrow/store
""")

    write_text(fn / "workstation/input_changed.mcfunction", """
scoreboard players set successful_call fancyui.master 0
execute unless entity @s[tag=sae.session] if data storage fancyui:data callback_data{slot:10} if data block ~ ~ ~ Items[{Slot:10b}] run function sae:workstation/session/claim
execute if entity @s[tag=sae.session] run function sae:workstation/session/verify_actor
execute unless data block ~ ~ ~ Items[{Slot:10b}] unless data block ~ ~ ~ Items[{Slot:12b}] unless data block ~ ~ ~ Items[{Slot:14b}] run function sae:workstation/session/release
function sae:workstation/render
""")
    write_text(fn / "workstation/session/claim.mcfunction", """
tag @s add sae.session
execute store result score @s sae.uuid0 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[0]
execute store result score @s sae.uuid1 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[1]
execute store result score @s sae.uuid2 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[2]
execute store result score @s sae.uuid3 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[3]
function sae:workstation/session/snapshot
""")
    write_text(fn / "workstation/session/verify_actor.mcfunction", """
scoreboard players set #actor_ok sae.tmp 0
execute store result score #actor0 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[0]
execute store result score #actor1 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[1]
execute store result score #actor2 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[2]
execute store result score #actor3 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[3]
execute if score #actor0 sae.tmp = @s sae.uuid0 if score #actor1 sae.tmp = @s sae.uuid1 if score #actor2 sae.tmp = @s sae.uuid2 if score #actor3 sae.tmp = @s sae.uuid3 run scoreboard players set #actor_ok sae.tmp 1
execute if score #actor_ok sae.tmp matches 1 run function sae:workstation/session/snapshot
execute if score #actor_ok sae.tmp matches 0 run function sae:workstation/session/conflict
""")
    write_text(fn / "workstation/session/snapshot.mcfunction", """
data remove entity @s data.sae.snapshot
execute if data block ~ ~ ~ Items[{Slot:10b}] run data modify entity @s data.sae.snapshot.target set from block ~ ~ ~ Items[{Slot:10b}]
execute if data block ~ ~ ~ Items[{Slot:12b}] run data modify entity @s data.sae.snapshot.catalyst set from block ~ ~ ~ Items[{Slot:12b}]
execute if data block ~ ~ ~ Items[{Slot:14b}] run data modify entity @s data.sae.snapshot.destination set from block ~ ~ ~ Items[{Slot:14b}]
""")
    write_text(fn / "workstation/session/release.mcfunction", """
tag @s remove sae.session
data remove entity @s data.sae.owner
data remove entity @s data.sae.snapshot
""")
    write_text(fn / "workstation/session/conflict.mcfunction", """
execute if data storage fancyui:data callback_data{slot:10} run function sae:workstation/drop_slot/10
execute if data storage fancyui:data callback_data{slot:12} run function sae:workstation/drop_slot/12
execute if data storage fancyui:data callback_data{slot:14} run function sae:workstation/drop_slot/14
function sae:escrow/store
tellraw @a[distance=..8] [{"text":"[Enchanting] ","color":"dark_aqua"},{"text":"The operation was cancelled because another player changed the Workstation.","color":"red"}]
""")

    for slot in (10, 12, 14):
        write_text(fn / f"workstation/drop_slot/{slot}.mcfunction", f"""
execute unless data block ~ ~ ~ Items[{{Slot:{slot}b}}] run return 0
summon item ~ ~1 ~ {{Tags:["sae.workstation_return"]}}
data modify entity @n[type=item,tag=sae.workstation_return,distance=..3] Item set from block ~ ~ ~ Items[{{Slot:{slot}b}}]
tag @n[type=item,tag=sae.workstation_return,distance=..3] remove sae.workstation_return
item replace block ~ ~ ~ container.{slot} with air
""")

    write_text(fn / "workstation/button.mcfunction", """
scoreboard players set successful_call fancyui.master 0
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_enchant"} run data modify entity @s data.sae.mode set value "enchant"
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_transfer"} run data modify entity @s data.sae.mode set value "transfer"
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_armor"} run data merge entity @s {data:{sae:{category:"Armor",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_melee"} run data merge entity @s {data:{sae:{category:"Melee",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_ranged"} run data merge entity @s {data:{sae:{category:"Ranged",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_tools"} run data merge entity @s {data:{sae:{category:"Tools",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_movement"} run data merge entity @s {data:{sae:{category:"Movement and water",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_curses"} run data merge entity @s {data:{sae:{category:"Curses",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"previous"} run function sae:workstation/reference/previous
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"next"} run function sae:workstation/reference/next
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"confirm"} run function sae:workstation/confirm
function sae:workstation/render
""")
    write_text(fn / "workstation/reference/previous.mcfunction", """
execute store result score #page sae.tmp run data get entity @s data.sae.page
scoreboard players remove #page sae.tmp 1
execute if score #page sae.tmp matches ..-1 run scoreboard players set #page sae.tmp 0
execute store result entity @s data.sae.page int 1 run scoreboard players get #page sae.tmp
""")
    write_text(fn / "workstation/reference/next.mcfunction", """
execute store result score #page sae.tmp run data get entity @s data.sae.page
scoreboard players add #page sae.tmp 1
execute unless data entity @s {data:{sae:{category:"Melee"}}} unless data entity @s {data:{sae:{category:"Ranged"}}} run scoreboard players set #page sae.tmp 0
execute if score #page sae.tmp matches 2.. run scoreboard players set #page sae.tmp 0
execute store result entity @s data.sae.page int 1 run scoreboard players get #page sae.tmp
""")

    write_text(fn / "workstation/render.mcfunction", """
function sae:workstation/preview
function sae:workstation/reference/render
""")

    write_text(fn / "workstation/on_break.mcfunction", """
scoreboard players set successful_call fancyui.master 0
function sae:workstation/unregister
kill @e[type=item,distance=..2,predicate=fancyui:ui/safety/is_fixed]
kill @e[type=item,distance=..2,nbt={Item:{id:"minecraft:chest"}}]
summon item ~ ~ ~ {Item:{id:"minecraft:enchanting_table",count:1}}
kill @e[type=block_display,tag=sae.workstation.display,distance=..1]
kill @s
""")

    write_text(fn / "uninstall.mcfunction", """
execute unless entity @s[type=player] run return run tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua"},{"text":"Run /function sae:uninstall as an in-game administrator, not from the server console.","color":"red"}]
execute as @a at @s run function sae:escrow/return
function sae:uninstall/registry_start
function sae:uninstall/drain_escrow
kill @e[type=item,predicate=fancyui:ui/safety/is_fixed]
tellraw @s [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Workstations were restored. Any offline-owner escrow was returned here. Remove the datapack before restarting.","color":"yellow"}]
""")
    write_text(fn / "workstation/uninstall_one.mcfunction", """
function sae:workstation/drop_slot/10
function sae:workstation/drop_slot/12
function sae:workstation/drop_slot/14
setblock ~ ~ ~ minecraft:enchanting_table
kill @e[type=block_display,tag=sae.workstation.display,distance=..1]
kill @s
""")

    write_text(fn / "workstation/register.mcfunction", """
execute store result score #registry_id sae.tmp run data get storage sae:registry next_id
scoreboard players add #registry_id sae.tmp 1
execute store result storage sae:registry next_id int 1 run scoreboard players get #registry_id sae.tmp
scoreboard players operation @s sae.tmp = #registry_id sae.tmp
data modify storage sae:registry pending set value {id:0,x:0,y:0,z:0,dimension:"minecraft:overworld"}
execute store result storage sae:registry pending.id int 1 run scoreboard players get #registry_id sae.tmp
execute store result storage sae:registry pending.x int 1 run data get entity @s Pos[0]
execute store result storage sae:registry pending.y int 1 run data get entity @s Pos[1]
execute store result storage sae:registry pending.z int 1 run data get entity @s Pos[2]
execute if dimension minecraft:the_nether run data modify storage sae:registry pending.dimension set value "minecraft:the_nether"
execute if dimension minecraft:the_end run data modify storage sae:registry pending.dimension set value "minecraft:the_end"
data modify storage sae:registry entries append from storage sae:registry pending
data remove storage sae:registry pending
""")
    write_text(fn / "workstation/unregister.mcfunction", """
scoreboard players operation #remove_id sae.tmp = @s sae.tmp
data remove storage sae:registry kept
function sae:workstation/unregister_scan
""")
    write_text(fn / "workstation/unregister_scan.mcfunction", """
execute unless data storage sae:registry entries[0] run return run function sae:workstation/unregister_finish
data modify storage sae:registry candidate set from storage sae:registry entries[0]
data remove storage sae:registry entries[0]
execute store result score #candidate_id sae.tmp run data get storage sae:registry candidate.id
execute unless score #candidate_id sae.tmp = #remove_id sae.tmp run data modify storage sae:registry kept append from storage sae:registry candidate
data remove storage sae:registry candidate
function sae:workstation/unregister_scan
""")
    write_text(fn / "workstation/unregister_finish.mcfunction", """
data modify storage sae:registry entries set from storage sae:registry kept
data remove storage sae:registry kept
""")
    write_text(fn / "uninstall/registry_start.mcfunction", """
data remove storage sae:registry uninstalling
data modify storage sae:registry uninstalling set from storage sae:registry entries
function sae:uninstall/registry_scan
""")
    write_text(fn / "uninstall/registry_scan.mcfunction", """
execute unless data storage sae:registry uninstalling[0] run return run data remove storage sae:registry entries
data modify storage sae:registry pending set from storage sae:registry uninstalling[0]
data remove storage sae:registry uninstalling[0]
function sae:uninstall/restore_macro with storage sae:registry pending
data remove storage sae:registry pending
function sae:uninstall/registry_scan
""")
    write_text(fn / "uninstall/restore_macro.mcfunction", """
$execute store success score #was_forceloaded sae.tmp in $(dimension) positioned $(x) $(y) $(z) run forceload query ~ ~
$execute in $(dimension) positioned $(x) $(y) $(z) run forceload add ~ ~
$execute in $(dimension) positioned $(x) $(y) $(z) as @e[type=marker,tag=sae.workstation,distance=..1,limit=1] at @s run function sae:workstation/uninstall_one
$execute in $(dimension) positioned $(x) $(y) $(z) unless entity @e[type=marker,tag=sae.workstation,distance=..1,limit=1] run setblock ~ ~ ~ minecraft:enchanting_table
$execute if score #was_forceloaded sae.tmp matches 0 in $(dimension) positioned $(x) $(y) $(z) run forceload remove ~ ~
""")
    write_text(fn / "uninstall/drain_escrow.mcfunction", """
execute unless data storage sae:escrow entries[0] run return 0
data modify storage sae:escrow returning set from storage sae:escrow entries[0]
data remove storage sae:escrow entries[0]
function sae:uninstall/spawn_escrow_items
data remove storage sae:escrow returning
function sae:uninstall/drain_escrow
""")
    write_text(fn / "uninstall/spawn_escrow_items.mcfunction", """
execute unless data storage sae:escrow returning.items[0] run return 0
summon item ~ ~1 ~ {Tags:["sae.uninstall_return"]}
data modify entity @n[type=item,tag=sae.uninstall_return,distance=..3] Item set from storage sae:escrow returning.items[0]
tag @n[type=item,tag=sae.uninstall_return,distance=..3] remove sae.uninstall_return
data remove storage sae:escrow returning.items[0]
function sae:uninstall/spawn_escrow_items
""")

    direct_slots = (
        [f"inventory.{i}" for i in range(27)]
        + [f"hotbar.{i}" for i in range(9)]
        + ["armor.head", "armor.chest", "armor.legs", "armor.feet", "weapon.offhand", "player.cursor"]
    )
    maintenance_lines = []
    for slot in direct_slots:
        maintenance_lines.append(f"execute if items entity @s {slot} #sae:netherite_equipment run item modify entity @s {slot} sae:maintenance/add_unbreakable")
        maintenance_lines.append(f"execute if items entity @s {slot} *[minecraft:enchantments~[{{enchantments:\"minecraft:mending\"}}]] run item modify entity @s {slot} sae:maintenance/repair_unbreakable")
        maintenance_lines.append(f"execute if items entity @s {slot} *[minecraft:repair_cost] run item modify entity @s {slot} sae:maintenance/clear_repair_cost")
    write_text(fn / "maintenance/tick.mcfunction", "execute as @a run function sae:maintenance/player")
    write_text(fn / "maintenance/player.mcfunction", "\n".join(maintenance_lines))
    write_json(DATA / "sae/item_modifier/maintenance/add_unbreakable.json", {
        "type": "minecraft:sequence",
        "functions": [
            {"type": "minecraft:set_enchantments", "enchantments": {"minecraft:mending": 1}, "add": False},
            {"type": "minecraft:set_components", "components": {"minecraft:damage": 0}},
        ],
    })
    write_json(DATA / "sae/item_modifier/maintenance/repair_unbreakable.json", {"type": "minecraft:set_components", "components": {"minecraft:damage": 0}})
    write_json(DATA / "sae/item_modifier/maintenance/clear_repair_cost.json", {"type": "minecraft:set_components", "components": {"minecraft:repair_cost": 0}})

    # Escrow is a persistent list of snapshots. Returned stacks spawn owner-bound at login.
    write_text(fn / "escrow/store.mcfunction", """
data modify storage sae:escrow pending set value {owner:[I;0,0,0,0],items:[]}
execute store result storage sae:escrow pending.owner[0] int 1 run scoreboard players get @s sae.uuid0
execute store result storage sae:escrow pending.owner[1] int 1 run scoreboard players get @s sae.uuid1
execute store result storage sae:escrow pending.owner[2] int 1 run scoreboard players get @s sae.uuid2
execute store result storage sae:escrow pending.owner[3] int 1 run scoreboard players get @s sae.uuid3
execute if data entity @s data.sae.snapshot.target run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.target
execute if data entity @s data.sae.snapshot.catalyst run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.catalyst
execute if data entity @s data.sae.snapshot.destination run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.destination
execute if data storage sae:escrow pending.items[0] run data modify storage sae:escrow entries append from storage sae:escrow pending
item replace block ~ ~ ~ container.10 with air
item replace block ~ ~ ~ container.12 with air
item replace block ~ ~ ~ container.14 with air
data remove storage sae:escrow pending
function sae:workstation/session/release
""")
    write_text(fn / "escrow/on_death.mcfunction", """
execute as @e[type=marker,tag=sae.workstation,tag=sae.session] at @s run function sae:workstation/session/check_owner_death
""")
    write_text(fn / "workstation/session/check_owner_death.mcfunction", """
scoreboard players set #dead sae.tmp 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a[scores={sae.deaths=1..}] store result score @s sae.uuid0 run data get entity @s UUID[0]
execute as @a[scores={sae.deaths=1..}] store result score @s sae.uuid1 run data get entity @s UUID[1]
execute as @a[scores={sae.deaths=1..}] store result score @s sae.uuid2 run data get entity @s UUID[2]
execute as @a[scores={sae.deaths=1..}] store result score @s sae.uuid3 run data get entity @s UUID[3]
execute as @a[scores={sae.deaths=1..}] if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run scoreboard players set #dead sae.tmp 1
execute if score #dead sae.tmp matches 1 run function sae:escrow/store
""")
    write_text(fn / "escrow/return.mcfunction", """
execute store result score @s sae.uuid0 run data get entity @s UUID[0]
execute store result score @s sae.uuid1 run data get entity @s UUID[1]
execute store result score @s sae.uuid2 run data get entity @s UUID[2]
execute store result score @s sae.uuid3 run data get entity @s UUID[3]
data remove storage sae:escrow kept
function sae:escrow/scan
""")
    write_text(fn / "escrow/scan.mcfunction", """
execute unless data storage sae:escrow entries[0] run return run function sae:escrow/finish_scan
data modify storage sae:escrow returning set from storage sae:escrow entries[0]
data remove storage sae:escrow entries[0]
execute store result score #owner0 sae.tmp run data get storage sae:escrow returning.owner[0]
execute store result score #owner1 sae.tmp run data get storage sae:escrow returning.owner[1]
execute store result score #owner2 sae.tmp run data get storage sae:escrow returning.owner[2]
execute store result score #owner3 sae.tmp run data get storage sae:escrow returning.owner[3]
scoreboard players set #escrow_match sae.tmp 0
execute if score #owner0 sae.tmp = @s sae.uuid0 if score #owner1 sae.tmp = @s sae.uuid1 if score #owner2 sae.tmp = @s sae.uuid2 if score #owner3 sae.tmp = @s sae.uuid3 run scoreboard players set #escrow_match sae.tmp 1
execute if score #escrow_match sae.tmp matches 1 run function sae:escrow/return_entry
execute unless score #escrow_match sae.tmp matches 1 run data modify storage sae:escrow kept append from storage sae:escrow returning
data remove storage sae:escrow returning
function sae:escrow/scan
""")
    write_text(fn / "escrow/return_entry.mcfunction", """
function sae:escrow/spawn_items
tellraw @s [{"text":"[Enchanting] ","color":"dark_aqua"},{"text":"Your interrupted Workstation items were returned.","color":"green"}]
""")
    write_text(fn / "escrow/finish_scan.mcfunction", """
data modify storage sae:escrow entries set from storage sae:escrow kept
data remove storage sae:escrow kept
""")
    write_text(fn / "escrow/spawn_items.mcfunction", """
execute unless data storage sae:escrow returning.items[0] run return 0
summon item ~ ~1 ~ {Tags:["sae.escrow_return"],PickupDelay:0s}
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Item set from storage sae:escrow returning.items[0]
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Owner set from entity @s UUID
tag @n[type=item,tag=sae.escrow_return,distance=..3] remove sae.escrow_return
data remove storage sae:escrow returning.items[0]
function sae:escrow/spawn_items
""")

    # Preview and Catalyst operations.
    write_text(fn / "workstation/preview.mcfunction", """
scoreboard players set #valid sae.tmp 0
scoreboard players set #candidates sae.tmp 0
scoreboard players set #cost sae.tmp 0
data remove entity @s data.sae.pending
data remove entity @s data.sae.enchantment
data remove entity @s data.sae.next
data remove entity @s data.sae.valid
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function sae:transfer/preview
execute unless data entity @s {data:{sae:{mode:"transfer"}}} if items block ~ ~ ~ container.10 minecraft:book run function sae:enchant/preview/book
execute unless data entity @s {data:{sae:{mode:"transfer"}}} if items block ~ ~ ~ container.10 minecraft:enchanted_book run function sae:enchant/preview/book
execute unless data entity @s {data:{sae:{mode:"transfer"}}} unless items block ~ ~ ~ container.10 minecraft:book unless items block ~ ~ ~ container.10 minecraft:enchanted_book run function sae:enchant/preview/equipment
execute if score #candidates sae.tmp matches 1 run scoreboard players set #valid sae.tmp 1
execute if score #candidates sae.tmp matches 2.. run scoreboard players set #valid sae.tmp 0
execute store result entity @s data.sae.valid int 1 run scoreboard players get #valid sae.tmp
execute store result entity @s data.sae.cost int 1 run scoreboard players get #cost sae.tmp
function sae:workstation/preview/control
""")

    equipment_dispatch = []
    for enchantment, (catalyst, required, _) in CATALYSTS.items():
        supported = load_enchantment(enchantment)["supported_items"]
        equipment_dispatch.append(
            f"execute if items block ~ ~ ~ container.12 minecraft:{catalyst} if items block ~ ~ ~ container.10 {supported} run function sae:enchant/preview/equipment/{enchantment}"
        )
    write_text(fn / "enchant/preview/equipment.mcfunction", "\n".join([
        "execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count",
        "execute unless score #target_count sae.tmp matches 1 run return 0",
        *equipment_dispatch,
    ]))

    exclusive_groups = []
    for path in sorted((VANILLA / "tags/enchantment/exclusive_set").glob("*.json")):
        values = [v.removeprefix("minecraft:") for v in json.loads(path.read_text(encoding="utf-8"))["values"]]
        if path.stem == "bow":
            values = [v for v in values if v != "mending"]
        exclusive_groups.append(values)

    display_names = {e: ("Unbreakable" if e == "mending" else e.replace("_curse", "").replace("_", " ").title()) for e in CATALYSTS}
    for enchantment, (catalyst, required, _) in CATALYSTS.items():
        conflicts = next((group for group in exclusive_groups if enchantment in group), [])
        lines = [
            f"execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:12b}}].count",
            f"execute unless score #catalyst_count sae.tmp matches {required}.. run return 0",
        ]
        for conflict in conflicts:
            if conflict != enchantment:
                lines.append(f'execute if data block ~ ~ ~ Items[{{Slot:10b}}].components."minecraft:enchantments"."minecraft:{conflict}" run return 0')
        lines.extend([
            "scoreboard players set #current sae.tmp 0",
            f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:10b}}].components."minecraft:enchantments"."minecraft:{enchantment}"',
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run return 0",
            "scoreboard players operation #next sae.tmp = #current sae.tmp",
            "scoreboard players add #next sae.tmp 1",
            "scoreboard players add #candidates sae.tmp 1",
            "scoreboard players operation #cost sae.tmp = #next sae.tmp",
            f'data modify entity @s data.sae.enchantment set value "minecraft:{enchantment}"',
            "execute store result entity @s data.sae.next int 1 run scoreboard players get #next sae.tmp",
            f'data modify entity @s data.sae.label set value "{display_names[enchantment]}"',
            f'data modify entity @s data.sae.curse set value {str(enchantment in {"binding_curse", "vanishing_curse"}).lower()}',
        ])
        write_text(fn / f"enchant/preview/equipment/{enchantment}.mcfunction", "\n".join(lines))

    catalyst_groups: dict[str, list[str]] = {}
    for enchantment, (catalyst, _, _) in CATALYSTS.items():
        catalyst_groups.setdefault(catalyst, []).append(enchantment)
    book_dispatch = [
        "execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count",
        "execute unless score #target_count sae.tmp matches 1 run return 0",
    ]
    for catalyst in catalyst_groups:
        book_dispatch.append(f"execute if items block ~ ~ ~ container.12 minecraft:{catalyst} run function sae:enchant/preview/book/{catalyst}")
    write_text(fn / "enchant/preview/book.mcfunction", "\n".join(book_dispatch))

    for catalyst, enchantments in catalyst_groups.items():
        required = CATALYSTS[enchantments[0]][1]
        lines = [
            "execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count",
            f"execute unless score #catalyst_count sae.tmp matches {required}.. run return 0",
        ]
        lines.extend(f"function sae:enchant/preview/book_candidate/{e}" for e in enchantments)
        lines.extend([
            "execute unless data entity @s data.sae.pending run return 0",
            "scoreboard players set #candidates sae.tmp 1",
            'data modify entity @s data.sae.label set value "Book upgrade"',
            "data modify entity @s data.sae.curse set value false",
        ])
        if any(e in {"binding_curse", "vanishing_curse"} for e in enchantments):
            lines[-1] = "data modify entity @s data.sae.curse set value true"
        write_text(fn / f"enchant/preview/book/{catalyst}.mcfunction", "\n".join(lines))

    for enchantment in CATALYSTS:
        component = "minecraft:stored_enchantments"
        lines = [
            "scoreboard players set #current sae.tmp 0",
            f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:10b}}].components."{component}"."minecraft:{enchantment}"',
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run return 0",
            "scoreboard players operation #next sae.tmp = #current sae.tmp",
            "scoreboard players add #next sae.tmp 1",
            f'execute store result entity @s data.sae.pending."minecraft:{enchantment}" int 1 run scoreboard players get #next sae.tmp',
            "execute if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp",
        ]
        write_text(fn / f"enchant/preview/book_candidate/{enchantment}.mcfunction", "\n".join(lines))

    write_text(fn / "workstation/preview/control.mcfunction", """
data modify storage sae:runtime control set from block ~ ~ ~ Items[{Slot:16b}]
execute if score #valid sae.tmp matches 1 run function sae:workstation/preview/control_valid
execute unless score #valid sae.tmp matches 1 run function sae:workstation/preview/control_invalid
data modify block ~ ~ ~ Items[{Slot:16b}] set from storage sae:runtime control
data remove storage sae:runtime control
""")
    write_text(fn / "workstation/preview/control_invalid.mcfunction", """
data modify storage sae:runtime control.id set value "minecraft:barrier"
data modify storage sae:runtime control.components."minecraft:custom_name" set value {text:"Cannot confirm",color:"red",italic:false}
data modify storage sae:runtime control.components."minecraft:lore" set value [{text:"Insert valid inputs or resolve the conflict",color:"gray",italic:false}]
""")
    write_text(fn / "workstation/preview/control_valid.mcfunction", """
data modify storage sae:runtime macro.cost set from entity @s data.sae.cost
data modify storage sae:runtime macro.label set from entity @s data.sae.label
data modify storage sae:runtime control.id set value "minecraft:lime_dye"
function sae:workstation/preview/control_valid_macro with storage sae:runtime macro
execute if data entity @s data.sae{curse:true} run function sae:workstation/preview/control_curse
""")
    write_text(fn / "workstation/preview/control_valid_macro.mcfunction", """
$data modify storage sae:runtime control.components."minecraft:custom_name" set value {text:"Apply $(label)",color:"green",italic:false}
$data modify storage sae:runtime control.components."minecraft:lore" set value [{text:"Cost: $(cost) levels",color:"gray",italic:false},{text:"Click to confirm",color:"yellow",italic:false}]
""")
    write_text(fn / "workstation/preview/control_curse.mcfunction", """
data modify storage sae:runtime control.id set value "minecraft:red_dye"
data modify storage sae:runtime control.components."minecraft:custom_name" set value {text:"Apply Curse",color:"red",italic:false}
data modify storage sae:runtime control.components."minecraft:lore" set value [{text:"Grindstones cannot remove this enchantment",color:"dark_red",italic:false},{text:"Click to confirm",color:"yellow",italic:false}]
""")

    write_text(fn / "workstation/confirm.mcfunction", """
execute unless entity @s[tag=sae.session] run return run tellraw @a[tag=fancyui.button.clicker] {"text":"Insert a target item first.","color":"red"}
function sae:workstation/session/check_clicker
execute unless score #actor_ok sae.tmp matches 1 run return run tellraw @a[tag=fancyui.button.clicker] {"text":"This Workstation belongs to another player.","color":"red"}
function sae:workstation/preview
execute unless data entity @s data.sae{valid:1} run return run tellraw @a[tag=fancyui.button.clicker] {"text":"The inputs no longer describe a valid operation.","color":"red"}
execute as @a[tag=fancyui.button.clicker] store result score #levels sae.tmp run experience query @s levels
execute unless entity @a[tag=fancyui.button.clicker,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return run tellraw @a[tag=fancyui.button.clicker] {"text":"You do not have enough levels.","color":"red"}
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function sae:transfer/apply
execute unless data entity @s {data:{sae:{mode:"transfer"}}} run function sae:enchant/apply
function sae:workstation/session/snapshot
function sae:workstation/render
""")
    write_text(fn / "workstation/session/check_clicker.mcfunction", """
scoreboard players set #actor_ok sae.tmp 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a[tag=fancyui.button.clicker] store result score @s sae.uuid0 run data get entity @s UUID[0]
execute as @a[tag=fancyui.button.clicker] store result score @s sae.uuid1 run data get entity @s UUID[1]
execute as @a[tag=fancyui.button.clicker] store result score @s sae.uuid2 run data get entity @s UUID[2]
execute as @a[tag=fancyui.button.clicker] store result score @s sae.uuid3 run data get entity @s UUID[3]
execute as @a[tag=fancyui.button.clicker] if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run scoreboard players set #actor_ok sae.tmp 1
""")
    write_text(fn / "enchant/apply.mcfunction", """
execute if data entity @s data.sae.pending run function sae:enchant/apply_book
execute unless data entity @s data.sae.pending run function sae:enchant/apply_equipment
function sae:workstation/consume_catalyst
function sae:workstation/charge_levels
""")
    write_text(fn / "enchant/apply_book.mcfunction", """
data modify block ~ ~ ~ Items[{Slot:10b}].id set value "minecraft:enchanted_book"
execute unless data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" set value {}
data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" merge from entity @s data.sae.pending
execute if data entity @s data.sae.pending."minecraft:mending" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:damage" set value 0
""")
    write_text(fn / "enchant/apply_equipment.mcfunction", """
data modify storage sae:runtime macro.enchantment set from entity @s data.sae.enchantment
data modify storage sae:runtime macro.next set from entity @s data.sae.next
function sae:enchant/apply_equipment_macro with storage sae:runtime macro
execute if data entity @s {data:{sae:{enchantment:"minecraft:mending"}}} run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:damage" set value 0
""")
    write_text(fn / "enchant/apply_equipment_macro.mcfunction", """
execute unless data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments" set value {}
$data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."$(enchantment)" set value $(next)
""")
    write_text(fn / "workstation/consume_catalyst.mcfunction", """
execute store result score #count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
scoreboard players set #consume sae.tmp 1
execute if data entity @s {data:{sae:{enchantment:"minecraft:infinity"}}} run scoreboard players set #consume sae.tmp 64
execute if data entity @s data.sae.pending."minecraft:infinity" run scoreboard players set #consume sae.tmp 64
scoreboard players operation #count sae.tmp -= #consume sae.tmp
execute if score #count sae.tmp matches ..0 run item replace block ~ ~ ~ container.12 with air
execute if score #count sae.tmp matches 1.. store result storage sae:runtime macro.count int 1 run scoreboard players get #count sae.tmp
execute if score #count sae.tmp matches 1.. run function sae:workstation/set_catalyst_count with storage sae:runtime macro
""")
    write_text(fn / "workstation/set_catalyst_count.mcfunction", "$data modify block ~ ~ ~ Items[{Slot:12b}].count set value $(count)")
    write_text(fn / "workstation/charge_levels.mcfunction", """
execute if entity @a[tag=fancyui.button.clicker,gamemode=creative] run return 0
execute store result storage sae:runtime macro.cost int 1 run scoreboard players get #cost sae.tmp
function sae:workstation/charge_levels_macro with storage sae:runtime macro
""")
    write_text(fn / "workstation/charge_levels_macro.mcfunction", "$experience add @a[tag=fancyui.button.clicker] -$(cost) levels")

    # Transfer preserves the destination stack and moves the complete vanilla enchantment map.
    transfer_preview = [
        "execute store result score #source_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count",
        "execute store result score #destination_count sae.tmp run data get block ~ ~ ~ Items[{Slot:14b}].count",
        "execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count",
        "execute unless score #source_count sae.tmp matches 1 run return 0",
        "execute unless score #destination_count sae.tmp matches 1 run return 0",
        "execute unless score #catalyst_count sae.tmp matches 1.. run return 0",
        "execute unless items block ~ ~ ~ container.12 minecraft:amethyst_block run return 0",
        "execute if items block ~ ~ ~ container.10 minecraft:book run return 0",
        "execute if items block ~ ~ ~ container.10 minecraft:enchanted_book run return 0",
        "scoreboard players set #source_enchants sae.tmp 0",
    ]
    for enchantment in CATALYSTS:
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:10b}}].components."minecraft:enchantments"."minecraft:{enchantment}" run scoreboard players add #source_enchants sae.tmp 1'
        )
    transfer_preview.extend([
        "execute unless score #source_enchants sae.tmp matches 1.. run return 0",
        "scoreboard players set #destination_ok sae.tmp 1",
    ])
    for enchantment in CATALYSTS:
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:14b}}].components."minecraft:enchantments"."minecraft:{enchantment}" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0'
        )
        if enchantment != "mending":
            transfer_preview.append(
                f'execute if data block ~ ~ ~ Items[{{Slot:14b}}].components."minecraft:enchantments"."minecraft:{enchantment}" run scoreboard players set #destination_ok sae.tmp 0'
            )
    transfer_preview.extend([
        "execute unless score #destination_ok sae.tmp matches 1 run return 0",
        "scoreboard players set #category_match sae.tmp 0",
        "execute if items block ~ ~ ~ container.14 minecraft:book run scoreboard players set #category_match sae.tmp 1",
    ])
    for category in CATEGORIES:
        transfer_preview.append(
            f"execute if items block ~ ~ ~ container.10 #sae:transfer/{category} if items block ~ ~ ~ container.14 #sae:transfer/{category} run scoreboard players set #category_match sae.tmp 1"
        )
    transfer_preview.extend([
        "execute unless score #category_match sae.tmp matches 1 run return 0",
        "scoreboard players set #compatible sae.tmp 1",
        "execute if items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/preview_valid",
    ])
    for enchantment in CATALYSTS:
        supported = load_enchantment(enchantment)["supported_items"]
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:10b}}].components."minecraft:enchantments"."minecraft:{enchantment}" unless items block ~ ~ ~ container.14 {supported} run scoreboard players set #compatible sae.tmp 0'
        )
    transfer_preview.append("execute if score #compatible sae.tmp matches 1 run function sae:transfer/preview_valid")
    write_text(fn / "transfer/preview.mcfunction", "\n".join(transfer_preview))
    write_text(fn / "transfer/preview_valid.mcfunction", """
scoreboard players set #candidates sae.tmp 1
scoreboard players set #cost sae.tmp 5
data modify entity @s data.sae.label set value "all enchantments"
data modify entity @s data.sae.transfer_valid set value true
""")
    write_text(fn / "transfer/apply.mcfunction", """
execute if items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/apply_book
execute unless items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/apply_equipment
item replace block ~ ~ ~ container.10 with air
function sae:workstation/consume_transfer_catalyst
function sae:workstation/charge_levels
tellraw @a[tag=fancyui.button.clicker] {"text":"All enchantments transferred; the source item was consumed.","color":"green"}
""")
    write_text(fn / "transfer/apply_book.mcfunction", """
data modify block ~ ~ ~ Items[{Slot:14b}].id set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{Slot:14b}].components."minecraft:stored_enchantments" set from block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"
""")
    write_text(fn / "transfer/apply_equipment.mcfunction", """
execute unless data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments" set value {}
data modify block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments" merge from block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:mending" run data modify block ~ ~ ~ Items[{Slot:14b}].components."minecraft:damage" set value 0
""")
    write_text(fn / "workstation/consume_transfer_catalyst.mcfunction", """
execute store result score #count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
scoreboard players remove #count sae.tmp 1
execute if score #count sae.tmp matches ..0 run item replace block ~ ~ ~ container.12 with air
execute if score #count sae.tmp matches 1.. store result storage sae:runtime macro.count int 1 run scoreboard players get #count sae.tmp
execute if score #count sae.tmp matches 1.. run function sae:workstation/set_catalyst_count with storage sae:runtime macro
""")

    # Reference pages reuse the nine fixed button slots; they are informational controls.
    pages_by_category: dict[str, list[list[str]]] = {}
    for category in ["Armor", "Melee", "Ranged", "Tools", "Movement and water", "Curses"]:
        names = [name for name, (_, _, group) in CATALYSTS.items() if group == category]
        pages_by_category[category] = [names[i:i + 9] for i in range(0, len(names), 9)] or [[]]

    reference_dispatch: list[str] = []
    for category, pages in pages_by_category.items():
        for page_index, enchantments in enumerate(pages):
            function_name = category.lower().replace(" ", "_")
            reference_dispatch.append(
                f'execute if data entity @s {{data:{{sae:{{category:"{category}",page:{page_index}}}}}}} run function sae:workstation/reference/{function_name}_{page_index}'
            )
            lines: list[str] = []
            for offset in range(9):
                slot = 18 + offset
                if offset < len(enchantments):
                    enchantment = enchantments[offset]
                    catalyst, required, _ = CATALYSTS[enchantment]
                    name = display_names[enchantment]
                    catalyst_name = catalyst.replace("_", " ").title()
                    lines.extend([
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].id set value "minecraft:{catalyst}"',
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_name" set value {{text:"{name}",color:"aqua",italic:false}}',
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:lore" set value [{{text:"{required} × {catalyst_name} per tier",color:"gray",italic:false}}]',
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_data".sae.enchantment set value "minecraft:{enchantment}"',
                    ])
                else:
                    lines.extend([
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].id set value "minecraft:gray_stained_glass_pane"',
                        f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_name" set value {{text:" ",italic:false}}',
                        f'data remove block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:lore"',
                        f'data remove block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_data".sae.enchantment',
                    ])
            write_text(fn / f"workstation/reference/{function_name}_{page_index}.mcfunction", "\n".join(lines))
    # Clamp page when changing to a category with fewer pages.
    reference_dispatch.append("execute unless data entity @s data.sae.category run data modify entity @s data.sae.category set value \"Armor\"")
    reference_dispatch.append("execute unless data entity @s data.sae.page run data modify entity @s data.sae.page set value 0")
    reference_dispatch.append("function sae:workstation/reference/filter")
    write_text(fn / "workstation/reference/render.mcfunction", "\n".join(reference_dispatch))

    filter_lines = [
        "execute unless data block ~ ~ ~ Items[{Slot:10b}] run return 0",
        "execute if items block ~ ~ ~ container.10 minecraft:book run return 0",
        "execute if items block ~ ~ ~ container.10 minecraft:enchanted_book run return 0",
    ]
    for slot in range(18, 27):
        for enchantment in CATALYSTS:
            supported = load_enchantment(enchantment)["supported_items"]
            filter_lines.append(
                f'execute if data block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_data".sae{{enchantment:"minecraft:{enchantment}"}} unless items block ~ ~ ~ container.10 {supported} run function sae:workstation/reference/hide_{slot}'
            )
        write_text(fn / f"workstation/reference/hide_{slot}.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].id set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_name" set value {{text:"Not compatible",color:"dark_gray",italic:false}}
data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:lore" set value [{{text:"This recipe does not apply to the inserted item",color:"gray",italic:false}}]
""")
    write_text(fn / "workstation/reference/filter.mcfunction", "\n".join(filter_lines))

    write_json(DATA / "minecraft/tags/function/load.json", {"values": ["sae:load"]})
    write_json(DATA / "minecraft/tags/function/tick.json", {"values": ["sae:tick"]})
    write_json(DATA / "sae/advancement/place_workstation.json", {
        "criteria": {
            "placed": {
                "trigger": "minecraft:placed_block",
                "conditions": {"location": {"type": "minecraft:match_block", "blocks": "minecraft:enchanting_table"}},
            }
        },
        "rewards": {"function": "sae:workstation/place/start"},
    })


def main() -> None:
    if not VANILLA.exists() or not FANCYUI.exists():
        raise SystemExit("Missing .cache vanilla data or the private FancyUI dependency")
    if DATA.exists():
        shutil.rmtree(DATA)
    install_metadata()
    maximums = install_enchantments()
    install_item_tags()
    install_loot(maximums)
    install_recipe()
    install_runtime(maximums)
    print(f"Generated {len(CATALYSTS)} catalysts, {len(maximums)} enchantments, and {len(LOOT_TABLE_POOLS)} loot overrides")


if __name__ == "__main__":
    main()
