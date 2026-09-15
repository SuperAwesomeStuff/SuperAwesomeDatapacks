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
        f'{{Slot:{slot}b,type:"button",components:{{"minecraft:item_model":"minecraft:{item}",'
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
    target_slot = 10
    destination_slot = 11
    transfer_preview_slot = 13
    transfer_mode_slot = 18
    option_slots = [*range(3, 9), *range(12, 18), *range(21, 27)]

    write_text(fn / "load.mcfunction", """
scoreboard objectives add sae.tmp dummy
scoreboard objectives add sae.clock dummy
scoreboard objectives add sae.uuid0 dummy
scoreboard objectives add sae.uuid1 dummy
scoreboard objectives add sae.uuid2 dummy
scoreboard objectives add sae.uuid3 dummy
scoreboard objectives add sae.deaths deathCount
scoreboard objectives add sae.cooldown dummy
scoreboard objectives add sae.timer dummy
scoreboard objectives add sae.vanilla trigger
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
scoreboard players remove @a[scores={sae.cooldown=1..}] sae.cooldown 1
execute as @a at @s run function sae:escrow/return
scoreboard players enable @a sae.vanilla
execute as @a[scores={sae.vanilla=1..}] at @s run function sae:workstation/restore_vanilla/start
scoreboard players set @a[scores={sae.vanilla=1..}] sae.vanilla 0
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
    write_text(fn / "workstation/restore_vanilla/start.mcfunction", """
scoreboard players set #found sae.tmp 0
execute as @n[type=marker,tag=sae.workstation,distance=..6] at @s run function sae:workstation/restore_vanilla/apply
execute if score #found sae.tmp matches 0 run tellraw @s [{"text":"No workstation found. ","color":"red"},{"text":"Stand within six blocks of a Super Awesome Enchanting table and try again.","color":"gray"}]
""")
    write_text(fn / "workstation/restore_vanilla/apply.mcfunction", """
scoreboard players set #found sae.tmp 1
playsound minecraft:block.fire.extinguish block @a[distance=..8] ~ ~ ~ 0.7 1.2
function sae:workstation/unregister
function sae:workstation/uninstall_one
""")

    slots: list[str] = [
        background(0),
        button(1, "enchanting_table", "Target", "label"),
        button(2, "gray_stained_glass_pane", " ", "empty"),
        button(9, "gray_stained_glass_pane", " ", "empty"),
        watch(target_slot),
        watch(destination_slot),
        button(18, "amethyst_shard", "Switch to Transfer", "mode_toggle"),
        button(19, "arrow", "Page", "page_toggle"),
        button(20, "gray_stained_glass_pane", " ", "empty"),
    ]
    slots.extend(button(slot, "gray_stained_glass_pane", " ", "empty") for slot in option_slots)
    slot_snbt = ",".join(slots)
    create = f"""
scoreboard players set #found sae.tmp 1
execute unless score version fancyui.master matches 1.. run return run tellraw @s {{"text":"Super Awesome Enchanting requires the included FancyUI compatibility datapack.","color":"red"}}
setblock ~ ~ ~ minecraft:chest
execute unless entity @e[type=marker,tag=sae.workstation,distance=..1] run summon marker ~ ~0.5 ~ {{Tags:["sae.workstation","fancyui","fancyui.container"]}}
execute as @n[type=marker,tag=sae.workstation,distance=..1] run data modify entity @s data set value {{container:"minecraft:chest",container_data:{{CustomName:{{text:"Super Awesome Enchanting"}}}},on_break:"sae:workstation/on_break",slots:[{slot_snbt}],sae:{{mode:"enchant",page:0}}}}
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
execute if score @s sae.timer matches 1.. run scoreboard players remove @s sae.timer 1
execute if score @s sae.timer matches 0 run data remove entity @s data.sae.armed
execute if entity @s[tag=sae.session] if score #clock sae.clock matches 0 run function sae:workstation/render
execute if entity @s[tag=sae.session] if score #clock sae.clock matches 10 run function sae:workstation/render
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

    write_text(fn / "workstation/input_changed.mcfunction", f"""
scoreboard players set successful_call fancyui.master 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
execute unless entity @s[tag=sae.session] if data storage fancyui:data callback_data{{slot:{target_slot}}} if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}] run function sae:workstation/session/claim
execute unless entity @s[tag=sae.session] if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} if data storage fancyui:data callback_data{{slot:{destination_slot}}} if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run function sae:workstation/session/claim
execute if entity @s[tag=sae.session] run function sae:workstation/session/verify_actor
execute if data entity @s {{data:{{sae:{{mode:"enchant"}}}}}} unless data block ~ ~ ~ Items[{{Slot:{target_slot}b}}] run function sae:workstation/session/release
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} unless data block ~ ~ ~ Items[{{Slot:{target_slot}b}}] unless data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run function sae:workstation/session/release
data modify entity @s data.sae.page set value 0
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
    write_text(fn / "workstation/session/snapshot.mcfunction", f"""
data remove entity @s data.sae.snapshot
execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}] run data modify entity @s data.sae.snapshot.target set from block ~ ~ ~ Items[{{Slot:{target_slot}b}}]
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run data modify entity @s data.sae.snapshot.destination set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}]
""")
    write_text(fn / "workstation/session/release.mcfunction", """
tag @s remove sae.session
data remove entity @s data.sae.owner
data remove entity @s data.sae.snapshot
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
""")
    write_text(fn / "workstation/session/conflict.mcfunction", f"""
execute if data storage fancyui:data callback_data{{slot:{target_slot}}} run function sae:workstation/drop_slot/{target_slot}
execute if data storage fancyui:data callback_data{{slot:{destination_slot}}} run function sae:workstation/drop_slot/{destination_slot}
function sae:escrow/store
tellraw @a[distance=..8] [{{"text":"[Enchanting] ","color":"dark_aqua"}},{{"text":"The operation was cancelled because another player changed the Workstation.","color":"red"}}]
""")

    for slot in (target_slot, destination_slot):
        write_text(fn / f"workstation/drop_slot/{slot}.mcfunction", f"""
execute unless data block ~ ~ ~ Items[{{Slot:{slot}b}}] run return 0
summon item ~ ~1 ~ {{Item:{{id:"minecraft:stone",count:1}},Tags:["sae.workstation_return"]}}
data modify entity @n[type=item,tag=sae.workstation_return,distance=..3] Item set from block ~ ~ ~ Items[{{Slot:{slot}b}}]
tag @n[type=item,tag=sae.workstation_return,distance=..3] remove sae.workstation_return
item replace block ~ ~ ~ container.{slot} with air
scoreboard players set modified_slot fancyui.master {slot}
function fancyui:manual_removal
""")

    write_text(fn / "workstation/button.mcfunction", """
scoreboard players set successful_call fancyui.master 0
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_toggle"} run function sae:workstation/mode_toggle
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"page_toggle"} run function sae:workstation/page_toggle
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"enchant_option"} run function sae:workstation/select_option
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"transfer_take"} run function sae:workstation/transfer_take
function sae:workstation/render
""")
    write_text(fn / "workstation/control/check_owner.mcfunction", """
scoreboard players set #actor_ok sae.tmp 1
execute if entity @s[tag=sae.session] run function sae:workstation/session/check_clicker
execute unless score #actor_ok sae.tmp matches 1 run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute unless score #actor_ok sae.tmp matches 1 run function sae:workstation/control/reject_non_owner
""")
    write_text(fn / "workstation/control/reject_non_owner.mcfunction", """
function sae:workstation/session/tag_owner
tellraw @a[tag=fancyui.button.clicker] [{"text":"This Workstation belongs to ","color":"red"},{"selector":"@a[tag=sae.owner]","color":"yellow"},{"text":".","color":"red"}]
tag @a remove sae.owner
""")
    write_text(fn / "workstation/mode_toggle.mcfunction", f"""
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run return run function sae:workstation/set_mode_enchant
function sae:workstation/destination_guard/hide
data modify entity @s data.sae.mode set value "transfer"
data modify entity @s data.sae.page set value 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
""")
    write_text(fn / "workstation/destination_guard/show.mcfunction", f"""
execute if items block ~ ~ ~ container.{destination_slot} *[minecraft:custom_data~{{sae:{{destination_guard:true}}}}] run return 0
execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run return 0
item replace block ~ ~ ~ container.{destination_slot} from block ~ ~ ~ container.0
data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:custom_data".fancyui.Slot set value {destination_slot}b
data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:custom_data".sae set value {{destination_guard:true}}
scoreboard players set modified_slot fancyui.master {destination_slot}
function fancyui:manual_placement
""")
    write_text(fn / "workstation/destination_guard/hide.mcfunction", f"""
execute unless items block ~ ~ ~ container.{destination_slot} *[minecraft:custom_data~{{sae:{{destination_guard:true}}}}] run return 0
item replace block ~ ~ ~ container.{destination_slot} with air
scoreboard players set modified_slot fancyui.master {destination_slot}
function fancyui:manual_removal
""")
    write_text(fn / "workstation/set_mode_enchant.mcfunction", """
data modify entity @s data.sae.mode set value "enchant"
data modify entity @s data.sae.page set value 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
""")
    write_text(fn / "workstation/page_toggle.mcfunction", """
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute unless data entity @s data.sae.book_target run return 0
execute if data entity @s {data:{sae:{page:1}}} run return run function sae:workstation/set_page_zero
data modify entity @s data.sae.page set value 1
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
""")
    write_text(fn / "workstation/set_page_zero.mcfunction", """
data modify entity @s data.sae.page set value 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
""")

    write_text(fn / "workstation/render.mcfunction", """
function sae:workstation/session/tag_owner
function sae:workstation/options/render
tag @a remove sae.owner
""")
    write_text(fn / "workstation/session/tag_owner.mcfunction", """
tag @a remove sae.owner
execute unless entity @s[tag=sae.session] run return 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run tag @s add sae.owner
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
    write_text(fn / "workstation/uninstall_one.mcfunction", f"""
function sae:workstation/drop_slot/{target_slot}
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run function sae:workstation/drop_slot/{destination_slot}
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
summon item ~ ~1 ~ {Item:{id:"minecraft:stone",count:1},Tags:["sae.uninstall_return"]}
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
    write_text(fn / "escrow/store.mcfunction", f"""
data modify storage sae:escrow pending set value {{owner:[I;0,0,0,0],items:[]}}
execute store result storage sae:escrow pending.owner[0] int 1 run scoreboard players get @s sae.uuid0
execute store result storage sae:escrow pending.owner[1] int 1 run scoreboard players get @s sae.uuid1
execute store result storage sae:escrow pending.owner[2] int 1 run scoreboard players get @s sae.uuid2
execute store result storage sae:escrow pending.owner[3] int 1 run scoreboard players get @s sae.uuid3
execute if data entity @s data.sae.snapshot.target run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.target
execute if data entity @s data.sae.snapshot.destination run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.destination
execute if data storage sae:escrow pending.items[0] run data modify storage sae:escrow entries append from storage sae:escrow pending
item replace block ~ ~ ~ container.{target_slot} with air
scoreboard players set modified_slot fancyui.master {target_slot}
function fancyui:manual_removal
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run item replace block ~ ~ ~ container.{destination_slot} with air
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run scoreboard players set modified_slot fancyui.master {destination_slot}
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run function fancyui:manual_removal
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
summon item ~ ~1 ~ {Item:{id:"minecraft:stone",count:1},Tags:["sae.escrow_return"],PickupDelay:0s}
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Item set from storage sae:escrow returning.items[0]
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Owner set from entity @s UUID
tag @n[type=item,tag=sae.escrow_return,distance=..3] remove sae.escrow_return
data remove storage sae:escrow returning.items[0]
function sae:escrow/spawn_items
""")

    # Item-first Workstation UI. FancyUI slot roles are fixed at initialization;
    # modes therefore restyle the same controls rather than rebuilding the chest.
    exclusive_groups = []
    for path in sorted((VANILLA / "tags/enchantment/exclusive_set").glob("*.json")):
        values = [v.removeprefix("minecraft:") for v in json.loads(path.read_text(encoding="utf-8"))["values"]]
        if path.stem == "bow":
            values = [v for v in values if v != "mending"]
        exclusive_groups.append(values)

    display_names = {
        enchantment: (
            "Unbreakable"
            if enchantment == "mending"
            else enchantment.replace("_curse", "").replace("_", " ").title()
        )
        for enchantment in CATALYSTS
    }
    curse_enchantments = {"binding_curse", "vanishing_curse"}

    def enchantment_order(value: str) -> tuple[bool, str]:
        return value in curse_enchantments, display_names[value]

    catalyst_groups: dict[str, list[str]] = {}
    for enchantment, (catalyst, _, _) in CATALYSTS.items():
        catalyst_groups.setdefault(catalyst, []).append(enchantment)
    roman = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
    distinct_catalysts = sorted(catalyst_groups)

    # Count only the owner's main inventory and hotbar. Slot -106 (offhand),
    # armor, cursor, and nested containers are intentionally excluded.
    for catalyst in distinct_catalysts:
        lines = ["scoreboard players set #catalyst_count sae.tmp 0"]
        for inventory_slot in range(36):
            lines.extend([
                "scoreboard players set #slot_count sae.tmp 0",
                f'execute as @a[tag=sae.owner] store result score #slot_count sae.tmp run data get entity @s Inventory[{{Slot:{inventory_slot}b,id:"minecraft:{catalyst}"}}].count',
                "scoreboard players operation #catalyst_count sae.tmp += #slot_count sae.tmp",
            ])
        write_text(fn / f"workstation/inventory/count/{catalyst}.mcfunction", "\n".join(lines))

    def clear_button_lines(slot: int) -> list[str]:
        return [
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"',
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_name" set value {{text:" ",italic:false}}',
            f'data remove block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:lore"',
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_data".sae set value {{action:"empty"}}',
        ]

    clear_options: list[str] = []
    for slot in option_slots:
        clear_options.extend(clear_button_lines(slot))
    write_text(fn / "workstation/options/clear.mcfunction", "\n".join(clear_options))

    for index, slot in enumerate(option_slots):
        write_text(fn / f"workstation/options/place/{slot}.mcfunction", "\n".join([
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:item_model" set from storage sae:runtime option.id',
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_name" set from storage sae:runtime option.name',
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:lore" set from storage sae:runtime option.lore',
            f'data modify block ~ ~ ~ Items[{{Slot:{slot}b}}].components."minecraft:custom_data".sae set from storage sae:runtime option.data',
        ]))
    place_dispatch = [
        f"execute if score #option_index sae.tmp matches {index} run function sae:workstation/options/place/{slot}"
        for index, slot in enumerate(option_slots)
    ]
    place_dispatch.append("scoreboard players add #option_index sae.tmp 1")
    write_text(fn / "workstation/options/place.mcfunction", "\n".join(place_dispatch))

    write_text(fn / "workstation/options/add_cost_lore.mcfunction", "\n".join(
        f'execute if score #cost sae.tmp matches {level} run data modify storage sae:runtime option.lore append value {{text:"Cost: {level} level{'' if level == 1 else 's'}",color:"gray",italic:false}}'
        for level in range(1, 6)
    ))
    write_text(fn / "workstation/options/add_missing_lore.mcfunction", """
scoreboard players operation #missing sae.tmp = #required sae.tmp
scoreboard players operation #missing sae.tmp -= #catalyst_count sae.tmp
execute store result storage sae:runtime macro.missing int 1 run scoreboard players get #missing sae.tmp
function sae:workstation/options/add_missing_lore_macro with storage sae:runtime macro
""")
    write_text(fn / "workstation/options/add_missing_lore_macro.mcfunction", '$data modify storage sae:runtime option.lore append value [{text:"Missing: ",color:"red",italic:false},{text:"$(missing)",color:"red",italic:false},{text:" Catalyst",color:"red",italic:false}]')

    write_text(fn / "workstation/options/style_availability.mcfunction", """
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value "dark_gray"
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Unavailable",color:"red",italic:false}
execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Click to apply",color:"yellow",italic:false}
""")

    equipment_dispatch: list[str] = ["scoreboard players set #option_index sae.tmp 0"]
    for enchantment in sorted(CATALYSTS, key=enchantment_order):
        catalyst, required, _ = CATALYSTS[enchantment]
        supported = load_enchantment(enchantment)["supported_items"]
        name = display_names[enchantment]
        catalyst_name = catalyst.replace("_", " ").title()
        conflicts = [value for value in next((group for group in exclusive_groups if enchantment in group), []) if value != enchantment]
        equipment_dispatch.append(
            f"execute if items block ~ ~ ~ container.{target_slot} {supported} run function sae:workstation/options/equipment/{enchantment}"
        )
        lines = [
            f'data modify storage sae:runtime option set value {{id:"minecraft:{catalyst}",name:{{text:"{name}",color:"aqua",italic:false}},lore:[{{text:"Catalyst: {required} × {catalyst_name}",color:"gray",italic:false}}],data:{{action:"enchant_option",option:"{enchantment}"}}}}',
            "scoreboard players set #available sae.tmp 1",
            "scoreboard players set #current sae.tmp 0",
            f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}"',
            "scoreboard players operation #next sae.tmp = #current sae.tmp",
            "scoreboard players add #next sae.tmp 1",
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run scoreboard players set #next sae.tmp {maximums[enchantment]}",
        ]
        for level in range(1, maximums[enchantment] + 1):
            lines.append(
                f'execute if score #next sae.tmp matches {level} run data modify storage sae:runtime option.name set value {{text:"{name} {roman[level]}",color:"aqua",italic:false}}'
            )
        lines.extend([
            "scoreboard players operation #cost sae.tmp = #next sae.tmp",
            "function sae:workstation/options/add_cost_lore",
            f'execute if score #current sae.tmp matches {maximums[enchantment]}.. run data modify storage sae:runtime option.lore append value {{text:"Maximum tier reached",color:"red",italic:false}}',
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run scoreboard players set #available sae.tmp 0",
        ])
        for conflict in conflicts:
            conflict_name = display_names.get(conflict, conflict.replace("_", " ").title())
            lines.extend([
                f'execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{conflict}" run data modify storage sae:runtime option.lore append value {{text:"Conflicts with {conflict_name}",color:"red",italic:false}}',
                f'execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{conflict}" run scoreboard players set #available sae.tmp 0',
            ])
        lines.extend([
            f"scoreboard players set #required sae.tmp {required}",
            f"function sae:workstation/inventory/count/{catalyst}",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0",
            "scoreboard players set #levels sae.tmp 0",
            "execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels",
            "scoreboard players set #level_ok sae.tmp 0",
            "execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1",
            "execute if entity @a[tag=sae.owner,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1",
            "execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"Insufficient levels\",color:\"red\",italic:false}",
            "execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0",
        ])
        if enchantment in {"binding_curse", "vanishing_curse"}:
            lines.extend([
                'data modify storage sae:runtime option.lore append value {text:"Grindstones cannot remove this",color:"dark_red",italic:false}',
                "execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"First click arms this curse\",color:\"yellow\",italic:false}",
                f'execute if score #available sae.tmp matches 1 if data entity @s data.sae.armed{{kind:"curse",choice:"minecraft:{enchantment}"}} if score @s sae.timer matches 1.. run data modify storage sae:runtime option.lore[-1] set value {{text:"Click again to apply curse",color:"red",italic:false}}',
            ])
        else:
            lines.append("function sae:workstation/options/style_availability")
        if enchantment in {"binding_curse", "vanishing_curse"}:
            lines.extend([
                "execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value \"dark_gray\"",
                "execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"Unavailable\",color:\"red\",italic:false}",
            ])
        lines.append("function sae:workstation/options/place")
        write_text(fn / f"workstation/options/equipment/{enchantment}.mcfunction", "\n".join(lines))
    equipment_dispatch.append("execute if score #option_index sae.tmp matches 0 run function sae:workstation/options/instruction_unsupported")
    write_text(fn / "workstation/options/equipment.mcfunction", "\n".join(equipment_dispatch))

    # Book choices are grouped by Catalyst and ordered by their first result name.
    ordered_book_groups = sorted(
        catalyst_groups.items(),
        key=lambda entry: (
            any(value in curse_enchantments for value in entry[1]),
            display_names[sorted(entry[1], key=enchantment_order)[0]],
        ),
    )
    for page, page_groups in enumerate([ordered_book_groups[:18], ordered_book_groups[18:]]):
        lines = ["scoreboard players set #option_index sae.tmp 0"]
        lines.extend(f"function sae:workstation/options/book/{catalyst}" for catalyst, _ in page_groups)
        write_text(fn / f"workstation/options/book_page_{page}.mcfunction", "\n".join(lines))

    for catalyst, raw_enchantments in ordered_book_groups:
        enchantments = sorted(raw_enchantments, key=enchantment_order)
        required = CATALYSTS[enchantments[0]][1]
        catalyst_name = catalyst.replace("_", " ").title()
        option_name = ", ".join(display_names[value] for value in enchantments)
        lines = [
            f'data modify storage sae:runtime option set value {{id:"minecraft:{catalyst}",name:{{text:"{option_name}",color:"aqua",italic:false}},lore:[{{text:"Catalyst: {required} × {catalyst_name}",color:"gray",italic:false}}],data:{{action:"enchant_option",book:1b,catalyst:"{catalyst}"}}}}',
            "scoreboard players set #available sae.tmp 1",
            "scoreboard players set #any sae.tmp 0",
            "scoreboard players set #cost sae.tmp 0",
        ]
        for enchantment in enchantments:
            name = display_names[enchantment]
            lines.extend([
                "scoreboard players set #current sae.tmp 0",
                f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:stored_enchantments"."minecraft:{enchantment}"',
                "scoreboard players operation #next sae.tmp = #current sae.tmp",
                "scoreboard players add #next sae.tmp 1",
                f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run scoreboard players set #next sae.tmp {maximums[enchantment]}",
                f"execute unless score #current sae.tmp matches {maximums[enchantment]}.. run scoreboard players set #any sae.tmp 1",
                f"execute unless score #current sae.tmp matches {maximums[enchantment]}.. if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp",
            ])
            for level in range(1, maximums[enchantment] + 1):
                lines.append(
                    f'execute if score #next sae.tmp matches {level} run data modify storage sae:runtime option.lore append value {{text:"{name} {roman[level]}",color:"gray",italic:false}}'
                )
        lines.extend([
            "function sae:workstation/options/add_cost_lore",
            "execute unless score #any sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"Every result is at maximum tier\",color:\"red\",italic:false}",
            "execute unless score #any sae.tmp matches 1 run scoreboard players set #available sae.tmp 0",
            f"scoreboard players set #required sae.tmp {required}",
            f"function sae:workstation/inventory/count/{catalyst}",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0",
            "scoreboard players set #levels sae.tmp 0",
            "execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels",
            "scoreboard players set #level_ok sae.tmp 0",
            "execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1",
            "execute if entity @a[tag=sae.owner,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1",
            "execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"Insufficient levels\",color:\"red\",italic:false}",
            "execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0",
        ])
        if any(value in {"binding_curse", "vanishing_curse"} for value in enchantments):
            lines.extend([
                'data modify storage sae:runtime option.lore append value {text:"Grindstones cannot remove this",color:"dark_red",italic:false}',
                "execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"First click arms this curse\",color:\"yellow\",italic:false}",
                f'execute if score #available sae.tmp matches 1 if data entity @s data.sae.armed{{kind:"curse",choice:"{catalyst}"}} if score @s sae.timer matches 1.. run data modify storage sae:runtime option.lore[-1] set value {{text:"Click again to apply curse",color:"red",italic:false}}',
                "execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value \"dark_gray\"",
                "execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:\"Unavailable\",color:\"red\",italic:false}",
            ])
        else:
            lines.append("function sae:workstation/options/style_availability")
        lines.append("function sae:workstation/options/place")
        write_text(fn / f"workstation/options/book/{catalyst}.mcfunction", "\n".join(lines))

    write_text(fn / "workstation/options/instruction_empty.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:item_model" set value "minecraft:book"
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:custom_name" set value {{text:"Insert equipment or a Book",color:"yellow",italic:false}}
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:lore" set value [{{text:"Available enchantments will appear here",color:"gray",italic:false}}]
""")
    write_text(fn / "workstation/options/instruction_stack.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:item_model" set value "minecraft:barrier"
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:custom_name" set value {{text:"Insert exactly one item",color:"red",italic:false}}
""")
    write_text(fn / "workstation/options/instruction_unsupported.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:item_model" set value "minecraft:barrier"
data modify block ~ ~ ~ Items[{{Slot:{option_slots[0]}b}}].components."minecraft:custom_name" set value {{text:"This item cannot be enchanted",color:"red",italic:false}}
""")

    write_text(fn / "workstation/options/render.mcfunction", f"""
function sae:workstation/options/clear
data remove entity @s data.sae.book_target
execute if data entity @s {{data:{{sae:{{mode:"transfer"}}}}}} run return run function sae:transfer/render
function sae:workstation/options/render_enchant_controls
scoreboard players set #target_count sae.tmp 0
execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].count
execute if score #target_count sae.tmp matches 0 run return run function sae:workstation/options/instruction_empty
execute unless score #target_count sae.tmp matches 1 run return run function sae:workstation/options/instruction_stack
execute if items block ~ ~ ~ container.{target_slot} minecraft:book run data modify entity @s data.sae.book_target set value true
execute if items block ~ ~ ~ container.{target_slot} minecraft:enchanted_book run data modify entity @s data.sae.book_target set value true
execute if data entity @s data.sae.book_target run function sae:workstation/options/render_book_page_control
execute if data entity @s {{data:{{sae:{{book_target:true,page:1}}}}}} run return run function sae:workstation/options/book_page_1
execute if data entity @s data.sae.book_target run return run function sae:workstation/options/book_page_0
function sae:workstation/options/equipment
""")
    write_text(fn / "workstation/options/render_enchant_controls.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:custom_name" set value {{text:" ",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:1b}}].components."minecraft:item_model" set value "minecraft:enchanting_table"
data modify block ~ ~ ~ Items[{{Slot:1b}}].components."minecraft:custom_name" set value {{text:"Target",color:"white",italic:false}}
function sae:workstation/destination_guard/show
function sae:workstation/options/clear_transfer_chrome
function sae:workstation/options/clear_page_control
function sae:workstation/options/clear_transfer_control
data modify block ~ ~ ~ Items[{{Slot:18b}}].components."minecraft:item_model" set value "minecraft:amethyst_shard"
data modify block ~ ~ ~ Items[{{Slot:18b}}].components."minecraft:custom_name" set value {{text:"Switch to Transfer",color:"white",italic:false}}
data modify block ~ ~ ~ Items[{{Slot:18b}}].components."minecraft:lore" set value [{{text:"Move all enchantments to a compatible item",color:"gray",italic:false}}]
data modify block ~ ~ ~ Items[{{Slot:18b}}].components."minecraft:custom_data".sae set value {{action:"mode_toggle"}}
""")
    transfer_chrome_clear: list[str] = []
    for slot in (2, 9):
        transfer_chrome_clear.extend(clear_button_lines(slot))
    write_text(fn / "workstation/options/clear_transfer_chrome.mcfunction", "\n".join(transfer_chrome_clear))
    write_text(fn / "workstation/options/clear_page_control.mcfunction", "\n".join(clear_button_lines(19)))
    write_text(fn / "workstation/options/clear_transfer_control.mcfunction", "\n".join(clear_button_lines(20)))
    write_text(fn / "workstation/options/render_book_page_control.mcfunction", """
data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:item_model" set value "minecraft:arrow"
data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_data".sae set value {action:"page_toggle"}
execute if data entity @s {data:{sae:{page:0}}} run data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_name" set value {text:"Next — Page 1/2",color:"white",italic:false}
execute if data entity @s {data:{sae:{page:1}}} run data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_name" set value {text:"Previous — Page 2/2",color:"white",italic:false}
""")

    # Selection validation is independent from rendering and always rechecks live
    # target, inventory, conflicts, tiers, and experience before mutation.
    write_text(fn / "workstation/select_option.mcfunction", """
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute if entity @a[tag=fancyui.button.clicker,scores={sae.cooldown=1..}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
tag @a remove sae.owner
tag @a[tag=fancyui.button.clicker] add sae.owner
scoreboard players set #valid sae.tmp 0
data remove entity @s data.sae.pending
data remove entity @s data.sae.enchantment
data remove entity @s data.sae.catalyst
data remove entity @s data.sae.curse
function sae:enchant/validate_selection
tag @a remove sae.owner
execute unless score #valid sae.tmp matches 1 run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute if data entity @s data.sae{curse:true} run return run function sae:workstation/select_curse
function sae:workstation/apply_selection
""")
    validation_dispatch: list[str] = []
    for enchantment in CATALYSTS:
        validation_dispatch.append(
            f'execute if data storage fancyui:data button.components."minecraft:custom_data".sae{{option:"{enchantment}"}} run function sae:enchant/validate/equipment/{enchantment}'
        )
    for catalyst in distinct_catalysts:
        validation_dispatch.append(
            f'execute if data storage fancyui:data button.components."minecraft:custom_data".sae{{book:1b,catalyst:"{catalyst}"}} run function sae:enchant/validate/book/{catalyst}'
        )
    write_text(fn / "enchant/validate_selection.mcfunction", "\n".join(validation_dispatch))

    for enchantment, (catalyst, required, _) in CATALYSTS.items():
        supported = load_enchantment(enchantment)["supported_items"]
        conflicts = [value for value in next((group for group in exclusive_groups if enchantment in group), []) if value != enchantment]
        lines = [
            f"execute unless items block ~ ~ ~ container.{target_slot} {supported} run return 0",
            "scoreboard players set #target_count sae.tmp 0",
            f"execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].count",
            "execute unless score #target_count sae.tmp matches 1 run return 0",
        ]
        lines.extend(
            f'execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{conflict}" run return 0'
            for conflict in conflicts
        )
        lines.extend([
            "scoreboard players set #current sae.tmp 0",
            f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}"',
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run return 0",
            "scoreboard players operation #cost sae.tmp = #current sae.tmp",
            "scoreboard players add #cost sae.tmp 1",
            f"scoreboard players set #required sae.tmp {required}",
            f"function sae:workstation/inventory/count/{catalyst}",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run return 0",
            "scoreboard players set #levels sae.tmp 0",
            "execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels",
            "execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0",
            "scoreboard players set #valid sae.tmp 1",
            f'data modify entity @s data.sae.enchantment set value "minecraft:{enchantment}"',
            f'data modify entity @s data.sae.catalyst set value "{catalyst}"',
            f"data modify entity @s data.sae.next set value {maximums[enchantment]}",
            "execute store result entity @s data.sae.next int 1 run scoreboard players get #cost sae.tmp",
            f'data modify entity @s data.sae.curse set value {str(enchantment in {"binding_curse", "vanishing_curse"}).lower()}',
        ])
        write_text(fn / f"enchant/validate/equipment/{enchantment}.mcfunction", "\n".join(lines))

    for enchantment in CATALYSTS:
        lines = [
            "scoreboard players set #current sae.tmp 0",
            f'execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:stored_enchantments"."minecraft:{enchantment}"',
            f"execute if score #current sae.tmp matches {maximums[enchantment]}.. run return 0",
            "scoreboard players operation #next sae.tmp = #current sae.tmp",
            "scoreboard players add #next sae.tmp 1",
            f'execute store result entity @s data.sae.pending."minecraft:{enchantment}" int 1 run scoreboard players get #next sae.tmp',
            "execute if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp",
        ]
        write_text(fn / f"enchant/validate/book_candidate/{enchantment}.mcfunction", "\n".join(lines))
    for catalyst, enchantments in catalyst_groups.items():
        required = CATALYSTS[enchantments[0]][1]
        lines = [
            f"execute unless items block ~ ~ ~ container.{target_slot} minecraft:book unless items block ~ ~ ~ container.{target_slot} minecraft:enchanted_book run return 0",
            "scoreboard players set #target_count sae.tmp 0",
            f"execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].count",
            "execute unless score #target_count sae.tmp matches 1 run return 0",
            "scoreboard players set #cost sae.tmp 0",
        ]
        lines.extend(f"function sae:enchant/validate/book_candidate/{value}" for value in enchantments)
        lines.extend([
            "execute unless data entity @s data.sae.pending run return 0",
            f"scoreboard players set #required sae.tmp {required}",
            f"function sae:workstation/inventory/count/{catalyst}",
            "execute if score #catalyst_count sae.tmp < #required sae.tmp run return 0",
            "scoreboard players set #levels sae.tmp 0",
            "execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels",
            "execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0",
            "scoreboard players set #valid sae.tmp 1",
            f'data modify entity @s data.sae.catalyst set value "{catalyst}"',
            f'data modify entity @s data.sae.curse set value {str(any(value in {"binding_curse", "vanishing_curse"} for value in enchantments)).lower()}',
        ])
        write_text(fn / f"enchant/validate/book/{catalyst}.mcfunction", "\n".join(lines))

    write_text(fn / "workstation/select_curse.mcfunction", """
scoreboard players set #armed_match sae.tmp 0
function sae:workstation/select_curse_match
execute if score #armed_match sae.tmp matches 1 if score @s sae.timer matches 1.. run return run function sae:workstation/apply_selection
data modify entity @s data.sae.armed set value {kind:"curse",choice:""}
data modify entity @s data.sae.armed.choice set from entity @s data.sae.catalyst
execute if data entity @s data.sae.enchantment run data modify entity @s data.sae.armed.choice set from entity @s data.sae.enchantment
scoreboard players set @s sae.timer 60
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.7 0.7
""")
    curse_matches = []
    for value in ["binding_curse", "vanishing_curse"]:
        curse_matches.append(
            f'execute if data entity @s data.sae.armed{{choice:"minecraft:{value}"}} if data entity @s data.sae{{enchantment:"minecraft:{value}"}} run scoreboard players set #armed_match sae.tmp 1'
        )
        curse_matches.append(
            f'execute if data entity @s data.sae.armed{{choice:"{CATALYSTS[value][0]}"}} if data entity @s data.sae{{catalyst:"{CATALYSTS[value][0]}"}} run scoreboard players set #armed_match sae.tmp 1'
        )
    write_text(fn / "workstation/select_curse_match.mcfunction", "\n".join(curse_matches))

    write_text(fn / "workstation/apply_selection.mcfunction", f"""
execute if data entity @s data.sae.pending run function sae:enchant/apply_book
execute unless data entity @s data.sae.pending run function sae:enchant/apply_equipment
scoreboard players set modified_slot fancyui.master {target_slot}
function fancyui:manual_placement
function sae:workstation/consume_selected_catalyst
function sae:workstation/charge_levels
scoreboard players set @a[tag=fancyui.button.clicker] sae.cooldown 6
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 1 1
function sae:workstation/session/snapshot
""")
    write_text(fn / "transfer/deliver.mcfunction", """
execute as @e[type=marker,tag=fancyui.container] at @s if data entity @s data.sae.pending_delivery run function sae:transfer/deliver_one
""")
    write_text(fn / "transfer/deliver_one.mcfunction", f"""
function sae:workstation/session/tag_owner
scoreboard players set #delivered sae.tmp 0
execute if entity @a[tag=sae.owner,limit=1] unless items entity @a[tag=sae.owner,limit=1] player.cursor * run function sae:transfer/deliver_cursor
execute if score #delivered sae.tmp matches 0 run function sae:transfer/deliver_drop
item replace block ~ ~ ~ container.{destination_slot} with air
scoreboard players set modified_slot fancyui.master {destination_slot}
function fancyui:manual_removal
data remove entity @s data.sae.pending_delivery
tag @a remove sae.owner
function sae:workstation/session/release
function sae:workstation/render
""")
    write_text(fn / "transfer/deliver_cursor.mcfunction", f"""
item replace entity @a[tag=sae.owner,limit=1] player.cursor from block ~ ~ ~ container.{destination_slot}
scoreboard players set #delivered sae.tmp 1
""")
    write_text(fn / "transfer/deliver_drop.mcfunction", f"""
summon item ~ ~1 ~ {{Item:{{id:"minecraft:stone",count:1}},Tags:["sae.transfer_result"]}}
data modify entity @n[type=item,tag=sae.transfer_result,distance=..3] Item set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}]
execute if entity @a[tag=sae.owner,limit=1] run data modify entity @n[type=item,tag=sae.transfer_result,distance=..3] Owner set from entity @a[tag=sae.owner,limit=1] UUID
tag @n[type=item,tag=sae.transfer_result,distance=..3] remove sae.transfer_result
scoreboard players set #delivered sae.tmp 1
""")
    consume_dispatch = []
    for catalyst in distinct_catalysts:
        required = max(CATALYSTS[value][1] for value in catalyst_groups[catalyst])
        consume_dispatch.append(
            f'execute if data entity @s data.sae{{catalyst:"{catalyst}"}} run clear @a[tag=fancyui.button.clicker] minecraft:{catalyst} {required}'
        )
    write_text(fn / "workstation/consume_selected_catalyst.mcfunction", "\n".join(consume_dispatch))

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
    write_text(fn / "enchant/apply_book.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].id set value "minecraft:enchanted_book"
execute unless data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:stored_enchantments" run data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:stored_enchantments" set value {{}}
data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:stored_enchantments" merge from entity @s data.sae.pending
execute if data entity @s data.sae.pending."minecraft:mending" run data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:damage" set value 0
""")
    write_text(fn / "enchant/apply_equipment.mcfunction", f"""
data modify storage sae:runtime macro.enchantment set from entity @s data.sae.enchantment
data modify storage sae:runtime macro.next set from entity @s data.sae.next
function sae:enchant/apply_equipment_macro with storage sae:runtime macro
execute if data entity @s {{data:{{sae:{{enchantment:"minecraft:mending"}}}}}} run data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:damage" set value 0
""")
    write_text(fn / "enchant/apply_equipment_macro.mcfunction", f"""
execute unless data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments" set value {{}}
$data modify block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."$(enchantment)" set value $(next)
""")
    write_text(fn / "workstation/charge_levels.mcfunction", """
execute if entity @a[tag=fancyui.button.clicker,gamemode=creative] run return 0
execute store result storage sae:runtime macro.cost int 1 run scoreboard players get #cost sae.tmp
function sae:workstation/charge_levels_macro with storage sae:runtime macro
""")
    write_text(fn / "workstation/charge_levels_macro.mcfunction", "$experience add @a[tag=fancyui.button.clicker] -$(cost) levels")

    # Transfer preserves the destination stack and moves the complete enchantment map.
    transfer_preview = [
        "scoreboard players set #valid sae.tmp 0",
        'data modify entity @s data.sae.transfer_reason set value "Insert exactly one source item"',
        f"scoreboard players set #source_count sae.tmp 0",
        f"execute store result score #source_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:{target_slot}b}}].count",
        "execute unless score #source_count sae.tmp matches 1 run return 0",
        'data modify entity @s data.sae.transfer_reason set value "Insert exactly one destination item"',
        "scoreboard players set #destination_count sae.tmp 0",
        f"execute store result score #destination_count sae.tmp run data get block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].count",
        "execute unless score #destination_count sae.tmp matches 1 run return 0",
        'data modify entity @s data.sae.transfer_reason set value "Books cannot be transfer sources"',
        f"execute if items block ~ ~ ~ container.{target_slot} minecraft:book run return 0",
        f"execute if items block ~ ~ ~ container.{target_slot} minecraft:enchanted_book run return 0",
        "scoreboard players set #source_enchants sae.tmp 0",
    ]
    for enchantment in CATALYSTS:
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}" run scoreboard players add #source_enchants sae.tmp 1'
        )
    transfer_preview.extend([
        'data modify entity @s data.sae.transfer_reason set value "Source has no enchantments"',
        "execute unless score #source_enchants sae.tmp matches 1.. run return 0",
        "scoreboard players set #destination_ok sae.tmp 1",
    ])
    for enchantment in CATALYSTS:
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}" unless items block ~ ~ ~ container.{destination_slot} #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0'
        )
        if enchantment != "mending":
            transfer_preview.append(
                f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}" run scoreboard players set #destination_ok sae.tmp 0'
            )
    transfer_preview.extend([
        'data modify entity @s data.sae.transfer_reason set value "Destination is already enchanted"',
        "execute unless score #destination_ok sae.tmp matches 1 run return 0",
        "scoreboard players set #category_match sae.tmp 0",
        f"execute if items block ~ ~ ~ container.{destination_slot} minecraft:book run scoreboard players set #category_match sae.tmp 1",
    ])
    for category in CATEGORIES:
        transfer_preview.append(
            f"execute if items block ~ ~ ~ container.{target_slot} #sae:transfer/{category} if items block ~ ~ ~ container.{destination_slot} #sae:transfer/{category} run scoreboard players set #category_match sae.tmp 1"
        )
    transfer_preview.extend([
        'data modify entity @s data.sae.transfer_reason set value "Source and destination categories do not match"',
        "execute unless score #category_match sae.tmp matches 1 run return 0",
        "scoreboard players set #compatible sae.tmp 1",
        f"execute if items block ~ ~ ~ container.{destination_slot} minecraft:book run function sae:transfer/preview_valid",
    ])
    for enchantment in CATALYSTS:
        supported = load_enchantment(enchantment)["supported_items"]
        transfer_preview.append(
            f'execute if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"."minecraft:{enchantment}" unless items block ~ ~ ~ container.{destination_slot} {supported} run scoreboard players set #compatible sae.tmp 0'
        )
    transfer_preview.extend([
        'data modify entity @s data.sae.transfer_reason set value "Destination cannot accept every enchantment"',
        "execute if score #compatible sae.tmp matches 1 run function sae:transfer/preview_valid",
    ])
    write_text(fn / "transfer/preview.mcfunction", "\n".join(transfer_preview))
    write_text(fn / "transfer/preview_valid.mcfunction", """
scoreboard players set #cost sae.tmp 5
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
data modify entity @s data.sae.transfer_reason set value "Insufficient levels"
execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0
data modify entity @s data.sae.transfer_reason set value "Ready"
scoreboard players set #valid sae.tmp 1
""")
    write_text(fn / "transfer/apply.mcfunction", f"""
execute if items block ~ ~ ~ container.{destination_slot} minecraft:book run function sae:transfer/apply_book
execute unless items block ~ ~ ~ container.{destination_slot} minecraft:book run function sae:transfer/apply_equipment
scoreboard players set modified_slot fancyui.master {destination_slot}
function fancyui:manual_placement
item replace block ~ ~ ~ container.{target_slot} with air
scoreboard players set modified_slot fancyui.master {target_slot}
function fancyui:manual_removal
function sae:workstation/charge_levels
scoreboard players set @a[tag=fancyui.button.clicker] sae.cooldown 6
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 1 1
data modify entity @s data.sae.pending_delivery set value true
function sae:workstation/session/snapshot
schedule function sae:transfer/deliver 1t append
""")
    write_text(fn / "transfer/apply_book.mcfunction", f"""
data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].id set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:stored_enchantments" set from block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"
""")
    write_text(fn / "transfer/apply_equipment.mcfunction", f"""
execute unless data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments" set value {{}}
data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments" merge from block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"
execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments"."minecraft:mending" run data modify block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:damage" set value 0
""")

    transfer_preview_lines = [
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:item_model" set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].id',
        f'execute if items block ~ ~ ~ container.{destination_slot} minecraft:book run data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:item_model" set value "minecraft:enchanted_book"',
        f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:item_model" run data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:item_model" set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:item_model"',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_name" set value {{text:"Transfer result",color:"aqua",italic:false}}',
        f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:custom_name" run data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_name" set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:custom_name"',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:lore" set value []',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantments" set from block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"',
        f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantments" merge from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantments"',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantment_glint_override" set value true',
        f'execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantment_glint_override" run data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantment_glint_override" set from block ~ ~ ~ Items[{{Slot:{destination_slot}b}}].components."minecraft:enchantment_glint_override"',
        f'execute if items block ~ ~ ~ container.{destination_slot} minecraft:book run function sae:transfer/render_preview_book',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_data".sae set value {{action:"transfer_take"}}',
    ]
    write_text(fn / "transfer/render_preview_book.mcfunction", f"""
data remove block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantments"
data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:stored_enchantments" set from block ~ ~ ~ Items[{{Slot:{target_slot}b}}].components."minecraft:enchantments"
""")
    transfer_preview_lines.extend([
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:lore" append value {{text:"Source will be destroyed",color:"red",italic:false}}',
        f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:lore" append value {{text:"Cost: 5 levels",color:"gray",italic:false}}',
    ])
    write_text(fn / "transfer/render_preview.mcfunction", "\n".join(transfer_preview_lines))

    transfer_reason_names = {
        "Insert exactly one source item": "Insert one source item",
        "Insert exactly one destination item": "Insert one destination item",
        "Books cannot be transfer sources": "Books cannot be sources",
        "Source has no enchantments": "Source has no enchantments",
        "Destination is already enchanted": "Destination already enchanted",
        "Source and destination categories do not match": "Item categories do not match",
        "Destination cannot accept every enchantment": "Destination is incompatible",
        "Insufficient levels": "Insufficient levels",
    }
    reason_dispatch = []
    for index, (reason, name) in enumerate(transfer_reason_names.items()):
        reason_dispatch.append(
            f'execute if data entity @s data.sae{{transfer_reason:"{reason}"}} run function sae:transfer/control/reason_{index}'
        )
        write_text(fn / f"transfer/control/reason_{index}.mcfunction", f'data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_name" set value {{text:"{name}",color:"red",italic:false}}')
    write_text(fn / "transfer/control/reason.mcfunction", "\n".join(reason_dispatch))

    write_text(fn / "transfer/render.mcfunction", f"""
function sae:workstation/destination_guard/hide
data modify block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:custom_name" set value {{text:" ",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:0b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:1b}}].components."minecraft:item_model" set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{{Slot:1b}}].components."minecraft:custom_name" set value {{text:"Source",color:"white",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:1b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:2b}}].components."minecraft:item_model" set value "minecraft:chest"
data modify block ~ ~ ~ Items[{{Slot:2b}}].components."minecraft:custom_name" set value {{text:"Transfer item",color:"white",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:2b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:4b}}].components."minecraft:item_model" set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{{Slot:4b}}].components."minecraft:custom_name" set value {{text:"Result",color:"white",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:4b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:9b}}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{{Slot:9b}}].components."minecraft:custom_name" set value {{text:" ",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:9b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:12b}}].components."minecraft:item_model" set value "minecraft:arrow"
data modify block ~ ~ ~ Items[{{Slot:12b}}].components."minecraft:custom_name" set value {{text:"Creates",color:"gray",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:12b}}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:item_model" set value "minecraft:enchanting_table"
data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:custom_name" set value {{text:"Switch to Enchant",color:"white",italic:false}}
data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:lore" set value [{{text:"Return to item-first enchanting",color:"gray",italic:false}}]
data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:custom_data".sae set value {{action:"mode_toggle"}}
execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:item_model" set value "minecraft:barrier"
execute if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run data modify block ~ ~ ~ Items[{{Slot:{transfer_mode_slot}b}}].components."minecraft:lore" set value [{{text:"Remove the destination before switching",color:"red",italic:false}}]
function sae:workstation/options/clear_page_control
function sae:workstation/options/clear_transfer_control
data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_name" set value {{text:"Awaiting valid inputs",color:"dark_gray",italic:false}}
data remove block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:lore"
data remove block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantments"
data remove block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:stored_enchantments"
data remove block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:enchantment_glint_override"
data modify block ~ ~ ~ Items[{{Slot:{transfer_preview_slot}b}}].components."minecraft:custom_data".sae set value {{action:"empty"}}
function sae:transfer/preview
execute if score #valid sae.tmp matches 1 if data block ~ ~ ~ Items[{{Slot:{target_slot}b}}] if data block ~ ~ ~ Items[{{Slot:{destination_slot}b}}] run function sae:transfer/render_preview
execute unless score #valid sae.tmp matches 1 run function sae:transfer/control/reason
""")
    write_text(fn / "workstation/transfer_take.mcfunction", """
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute if entity @a[tag=fancyui.button.clicker,scores={sae.cooldown=1..}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
tag @a remove sae.owner
tag @a[tag=fancyui.button.clicker] add sae.owner
function sae:transfer/preview
tag @a remove sae.owner
execute unless score #valid sae.tmp matches 1 run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
function sae:transfer/apply
""")

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
