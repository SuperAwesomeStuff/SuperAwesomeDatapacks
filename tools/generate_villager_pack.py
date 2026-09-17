from __future__ import annotations

import json
import math
import shutil
from pathlib import Path
from typing import Any

# Book prices follow the enchanting pack's catalyst costs.
from generate_enchanting_pack import CATALYSTS


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "SuperAwesomeVillagers"
DATA = PACK / "data"
README = PACK / "README.md"
VANILLA = ROOT / ".cache/minecraft/26.3/vanilla/data/minecraft"

NS = "sav"

# Trades are never exhausted. Restocking cannot be disabled in 26.3, but with no
# uses left to restore it has nothing to do.
MAX_USES = 100_000

# Merchant experience. Zero keeps villagers at level 1 forever, which is what we
# want now that every offer lives in the level_1 trade set.
MERCHANT_XP = 0

# The 68 trade set IDs the game consults are hardcoded. New ones do nothing.
LEVELS = (1, 2, 3, 4, 5)


# Every trade is written in lowest terms: 1 Emerald for 16 Cobblestone, never
# 4 for 64. trade() reduces anything that slips through.

# Buyer catalogs: (emeralds_given, item_wanted, count_wanted)
FISHERMAN_BUYS: list[tuple[int, str, int]] = [
    (1, "birch_log", 32),
    (4, "diamond", 1),
    (32, "netherite_scrap", 1),
    (32, "heart_of_the_sea", 1),
    (8, "echo_shard", 1),
    (64, "enchanted_golden_apple", 1),
    (64, "nether_star", 1),
    (64, "dragon_egg", 1),
    (1, "raw_copper", 8),
    (1, "lapis_lazuli", 8),
    (1, "quartz", 8),
    (1, "raw_iron", 4),
    (1, "raw_gold", 2),
    (1, "cod", 16),
    (1, "salmon", 16),
    (1, "pufferfish", 8),
    (1, "tropical_fish", 8),
]

# Every stackable resource purchase costs this much; the output quantity is what
# communicates value. Quantities stay on the ladder 16/8/4/2/1.
STANDARD_PRICE = 1

# Wheat and Baked Potatoes are not bought: Hay Bales and furnaces turn
# villager-harvested crops back into unmarked goods. See VILLAGER_CROPS.
FARMER_BUYS: list[tuple[int, str, int]] = [
    # Bone Meal from Cleric Bones must not grow crops worth more than it cost.
    # Beetroot gains less from each use, so it is rated at half the others.
    (1, "carrot", 16),
    (1, "potato", 16),
    (1, "beetroot", 8),
    (1, "nether_wart", 16),
    (1, "apple", 8),
    (1, "chorus_fruit", 16),
    (1, "pumpkin_pie", 8),
    # Grown from Sniffer seeds. A harvested plant returns no seed, so every
    # sale costs a Sniffer dig.
    (1, "torchflower", 2),
    (1, "pitcher_plant", 2),
]

# Crops a Farmer villager harvests, mapped to their crop block. When a villager
# breaks the block, the crop drops as "Haram <crop>" with uncommon rarity. The
# Farmer only accepts common ones, so villager-run farms earn no Emeralds.
# A trade's component check ignores extra components, so the mark has to change
# one every item already has rather than add a new one.
VILLAGER_CROPS = {"carrot": "carrots", "potato": "potatoes", "beetroot": "beetroots"}
UNMARKED = {"minecraft:rarity": "common"}

BUTCHER_BUYS: list[tuple[int, str, int]] = [
    (1, "beef", 4),
    (1, "cooked_beef", 3),
    (1, "mutton", 4),
    (1, "cooked_mutton", 3),
    (1, "rabbit", 2),
    (2, "cooked_rabbit", 3),
    (1, "rabbit_hide", 4),
]

MASON_LADDER: dict[int, list[str]] = {
    16: [
        "cobblestone", "cobbled_deepslate", "stone", "deepslate", "dirt", "gravel",
        "granite", "diorite", "andesite", "tuff", "netherrack", "basalt", "blackstone",
        "end_stone",
    ],
    8: [
        "smooth_stone", "sand", "red_sand", "clay", "soul_sand", "soul_soil",
        "dripstone_block", "calcite", "glass", "terracotta", "nether_bricks",
        "prismarine", "purpur_block", "bricks",
        # Purely decorative, so priced generously. No recipe turns the block
        # back into Quartz, so it cannot loop through the Fisherman.
        "quartz_block", "resin_bricks",
        # Needs Silk Touch to collect in bulk.
        "ice",
    ],
    4: ["glowstone"],
    2: ["obsidian"],
}

# Brewing ingredients that cannot be farmed easily, plus the Overworld mob drops
# that otherwise require building a farm. Rabbit Hide is absent because the
# Butcher buys it; Bone sits at 4 rather than 16 because Bone Meal grows crops
# the Farmer buys.
CLERIC_LADDER: dict[int, list[str]] = {
    16: ["string", "rotten_flesh", "feather", "flint", "redstone", "sculk_vein"],
    8: ["gunpowder", "spider_eye", "ink_sac", "sculk"],
    4: ["bone", "slime_ball", "glow_ink_sac", "blaze_powder"],
    2: ["rabbit_foot", "phantom_membrane"],
    1: ["ghast_tear"],
}

SHEPHERD_LADDER: dict[int, list[str]] = {
    4: [f"{colour}_wool" for colour in (
        "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray",
        "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black",
    )],
}
SHEPHERD_LADDER[8] = [wool.removesuffix("_wool") + "_dye" for wool in SHEPHERD_LADDER[4]]

LEATHERWORKER_LADDER: dict[int, list[str]] = {8: ["leather"]}

# Redstone components the Cleric sells, priced from their recipes. Cheap parts
# come in bulk, so a Lever is 8 for 1 Emerald rather than 1 Emerald each.
REDSTONE = [
    "redstone_torch", "redstone_block", "repeater", "comparator", "observer",
    "piston", "sticky_piston", "slime_block", "dispenser", "dropper", "crafter",
    "hopper", "lever", "stone_button", "stone_pressure_plate",
    "light_weighted_pressure_plate", "heavy_weighted_pressure_plate", "tripwire_hook",
    "daylight_detector", "target", "trapped_chest", "note_block", "redstone_lamp",
    "copper_bulb", "lightning_rod", "tnt", "rail", "powered_rail", "detector_rail",
    "activator_rail", "minecart", "calibrated_sculk_sensor",
]

MAP_PRICE = 16

# Quantities a bulk purchase can hand out for 1 Emerald.
LADDER = (16, 8, 4, 2, 1)

# Convenience premium on anything priced from its materials.
PREMIUM = 1.25

# Seeds for price derivation: the Emerald value of one unit of a material.
# main() adds every rate the pack publishes, so this table only holds values
# no trade states directly.
BASE_VALUES: dict[str, float] = {
    "emerald": 1.0,
    # Smelted from the raw ores the Fisherman buys.
    "iron_ingot": STANDARD_PRICE / 4,
    "gold_ingot": STANDARD_PRICE / 2,
    "copper_ingot": STANDARD_PRICE / 8,
    # One step back from a block a vendor sells: 4 Shards make Prismarine,
    # 4 Pointed Dripstone make a Dripstone Block, 4 Dust make Glowstone, and a
    # Blaze Rod makes 2 Blaze Powder.
    "prismarine_shard": STANDARD_PRICE / 32,
    "pointed_dripstone": STANDARD_PRICE / 32,
    "glowstone_dust": STANDARD_PRICE / 16,
    "blaze_rod": STANDARD_PRICE / 2,
    # The Farmer no longer buys Wheat, but the Target's Hay Bale needs a value.
    # Kept at the old Farmer rate.
    "wheat": STANDARD_PRICE / 32,
    # Hand-set so enchanting catalysts have a price. Values are what gathering
    # costs, not the Wandering Trader's convenience price for the few it sells.
    "amethyst_shard": STANDARD_PRICE / 8,
    "coal": STANDARD_PRICE / 16,
    "sponge": 2.0,
    "nautilus_shell": 2.0,
    "turtle_scute": 2.0,
    "breeze_rod": 1.0,
    "blue_ice": 1.0,
}

# Emerald value of each currency a trade can ask for. A trade slot holds one
# stack, so prices above 64 Emeralds are quoted in Emerald Blocks.
CURRENCY: dict[str, int] = {"emerald": 1, "emerald_block": 9}

# Smith catalogs list their one-off items first, then each material tier in
# the creative inventory's order, which is also cheapest to dearest.
EQUIPMENT_TIERS = ("copper", "iron", "golden", "diamond")
ARMOR_PIECES = ("helmet", "chestplate", "leggings", "boots")
TOOL_PIECES = ("pickaxe", "axe", "shovel", "hoe")
WEAPON_PIECES = ("sword", "axe")

# These IDs are also blocks, but the block is the planted crop. Players treat
# the traded good as an item.
NOT_BLOCKS = {"wheat", "nether_wart"}

# Single items with no crafting recipe, so nothing to derive a price from.
HAND_PRICED: dict[str, int] = {
    "saddle": 8,
    "leather_horse_armor": 8,
    # End access should be buyable but expensive.
    "ender_pearl": 8,
    "sculk_sensor": 2,
    "sculk_shrieker": 4,
    "sculk_catalyst": 8,
}

# Never sold. Super Awesome Enchanting overrides minecraft:enchantment/mending
# so that the ID means Unbreakable, and trade sets are static JSON with no way
# to test for another pack's presence.
BOOK_EXCLUDED = {"mending", "binding_curse", "vanishing_curse"}


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def trade(
    wants: str,
    wants_count: int,
    gives: str,
    gives_count: int,
    components: dict[str, Any] | None = None,
    wants_components: dict[str, Any] | None = None,
) -> dict[str, Any]:
    divisor = math.gcd(wants_count, gives_count)
    wants_count //= divisor
    gives_count //= divisor
    given: dict[str, Any] = {"id": f"minecraft:{gives}", "count": gives_count}
    if components:
        given["components"] = components
    wanted: dict[str, Any] = {"id": f"minecraft:{wants}", "count": wants_count}
    if wants_components:
        wanted["components"] = wants_components
    return {
        "wants": wanted,
        "gives": given,
        "max_uses": MAX_USES,
        "xp": MERCHANT_XP,
        # Collapses the demand term and the reputation term of the price formula
        # to nothing. It does not touch Hero of the Village; see raid_reward().
        "reputation_discount": 0.0,
    }


def install_metadata() -> None:
    write_json(PACK / "pack.mcmeta", {
        "pack": {
            "description": "Super Awesome Villagers for Minecraft Java 26.3",
            "min_format": 121,
            "max_format": 121,
        }
    })


def emerald_cost(price: int) -> tuple[str, int]:
    if price <= 64:
        return "emerald", price
    return "emerald_block", math.ceil(price / CURRENCY["emerald_block"])


def is_currency(item: dict[str, Any]) -> bool:
    return item["id"].removeprefix("minecraft:") in CURRENCY


def unit_price(entry: dict[str, Any]) -> float:
    """Emeralds per unit of the good changing hands, whichever way it moves."""
    wants, gives = entry["wants"], entry["gives"]
    money, good = (gives, wants) if is_currency(gives) else (wants, gives)
    return CURRENCY[money["id"].removeprefix("minecraft:")] * money["count"] / good["count"]


BLOCKS: set[str] = set()


def load_blocks() -> None:
    report = json.loads((VANILLA.parents[1] / "reports/blocks.json").read_text(encoding="utf-8"))
    BLOCKS.update(key.removeprefix("minecraft:") for key in report)
    BLOCKS.difference_update(NOT_BLOCKS)


def by_price(trades: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Items before blocks, each cheapest first. The sort is stable, so equal
    prices keep catalog order."""
    def key(entry: dict[str, Any]) -> tuple[bool, float]:
        good = entry["wants"] if is_currency(entry["gives"]) else entry["gives"]
        return good["id"].removeprefix("minecraft:") in BLOCKS, unit_price(entry)

    return dict(sorted(trades.items(), key=lambda pair: key(pair[1])))


def offer_filter(entry: dict[str, Any]) -> dict[str, Any]:
    """SNBT that picks exactly this trade out of a villager's Offers.Recipes."""
    gives = entry["gives"]
    if is_currency(gives):
        match: dict[str, Any] = {"buy": {"id": entry["wants"]["id"]}}
    elif "components" in gives:
        match = {"sell": {"components": gives["components"]}}
    else:
        match = {"sell": {"id": gives["id"]}}
    return match


# Every catalog in its intended in-game order, filled by install_profession().
CATALOGS: dict[str, dict[str, dict[str, Any]]] = {}


def offer_nbt(entry: dict[str, Any]) -> dict[str, Any]:
    """A trade as the villager stores it in Offers.Recipes. Fields left at
    their codec default are omitted, matching what the game writes."""
    return {
        "buy": entry["wants"],
        "sell": entry["gives"],
        "maxUses": entry["max_uses"],
        "xp": entry["xp"],
    }


def snbt(value: Any) -> str:
    return json.dumps(value, separators=(",", ":"))


def install_stocking() -> None:
    """A trade set hands out its trades in random order, and only when a player
    first opens the trade screen. To show a fixed order, each villager's offers
    are written in catalog order the tick it takes a profession, before anyone
    can open them.

    Explorer Maps depend on where the villager stands, so they cannot be
    written as constants. They are made the way a trade would make them: the
    vanilla item modifier is run against the villager's own hand."""
    write_json(DATA / "minecraft/tags/function/load.json", {"values": [f"{NS}:load"]})
    write_json(DATA / "minecraft/tags/function/tick.json", {"values": [f"{NS}:stock/tick"]})
    write_text(DATA / NS / "function/load.mcfunction", "\n".join([
        "scoreboard objectives add sav.stock dummy",
        f"schedule function {NS}:stock/audit 1s replace",
    ]))
    write_text(DATA / NS / "function/stock/tick.mcfunction", "\n".join([
        f"execute as @e[type=minecraft:villager,tag=!sav.stocked] at @s run function {NS}:stock/villager",
        # A Wandering Trader never changes job, so it needs no audit.
        f"execute as @e[type=minecraft:wandering_trader,tag=!sav.stocked] at @s "
        f"run function {NS}:stock/wandering_trader",
    ]))
    # Changing profession clears a villager's offers, so a stocked villager
    # without any has lost its job and must be stocked again.
    write_text(DATA / NS / "function/stock/audit.mcfunction", "\n".join([
        f"schedule function {NS}:stock/audit 1s replace",
        "execute as @e[type=minecraft:villager,tag=sav.stocked] "
        "unless data entity @s Offers.Recipes[0] run tag @s remove sav.stocked",
    ]))

    villager = [
        "data modify storage sav:stock profession set value \"\"",
        "data modify storage sav:stock profession set from entity @s VillagerData.profession",
    ]
    for profession, trades in CATALOGS.items():
        if profession != "wandering_trader":
            villager.append(
                f'execute if data storage sav:stock {{profession:"minecraft:{profession}"}} '
                f"run return run function {NS}:stock/{profession}"
            )
        fixed = [offer_nbt(e) for e in trades.values() if "given_item_modifier" not in e]
        lines = [
            "tag @s add sav.stocked",
            # Offers already exist when the villager predates the pack or a
            # player got there first. Those are reordered rather than replaced.
            f"execute if data entity @s Offers.Recipes[0] run return run function {NS}:sort/{profession}",
        ]
        if len(fixed) == len(trades):
            lines.append(f"data modify entity @s Offers set value {snbt({'Recipes': fixed})}")
        else:
            lines.append("data modify storage sav:stock recipes set value []")
            for name, entry in trades.items():
                if "given_item_modifier" not in entry:
                    lines.append(f"data modify storage sav:stock recipes append value {snbt(offer_nbt(entry))}")
                    continue
                write_json(DATA / NS / "item_modifier" / profession / f"{name}.json", {
                    "type": "minecraft:sequence",
                    "functions": entry["given_item_modifier"],
                })
                offer = offer_nbt(entry)
                lines += [
                    f"item replace entity @s weapon.mainhand with {entry['gives']['id']}",
                    f"item modify entity @s weapon.mainhand {NS}:{profession}/{name}",
                    # The modifier discards the map when no structure is in range.
                    "execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes "
                    f"append value {snbt({**offer, 'sell': {}})}",
                    "execute if items entity @s weapon.mainhand * run data modify storage sav:stock "
                    "recipes[-1].sell set from entity @s equipment.mainhand",
                ]
            lines += [
                "item replace entity @s weapon.mainhand with minecraft:air",
                "data modify entity @s Offers.Recipes set from storage sav:stock recipes",
            ]
        write_text(DATA / NS / "function/stock" / f"{profession}.mcfunction", "\n".join(lines))

        sort = ["data modify storage sav:stock offers set from entity @s Offers.Recipes",
                "data modify storage sav:stock sorted set value []"]
        sort += [
            f"data modify storage sav:stock sorted append from storage sav:stock offers[{snbt(offer_filter(e))}]"
            for e in trades.values()
        ]
        sort += [
            # Offers from outside the catalog, such as vanilla ones on a villager
            # that predates the pack, are left alone rather than dropped.
            "execute store result score #offers sav.stock run data get storage sav:stock offers",
            "execute store result score #sorted sav.stock run data get storage sav:stock sorted",
            "execute unless score #offers sav.stock = #sorted sav.stock run return 0",
            "data modify entity @s Offers.Recipes set from storage sav:stock sorted",
        ]
        write_text(DATA / NS / "function/sort" / f"{profession}.mcfunction", "\n".join(sort))
    write_text(DATA / NS / "function/stock/villager.mcfunction", "\n".join(villager))


def install_profession(profession: str, trades: dict[str, dict[str, Any]]) -> None:
    """Write a profession's trades and pin the whole catalog to level 1.
    Trades must already be in their in-game order."""
    write_catalog(profession, trades)
    write_json(DATA / "minecraft/trade_set" / profession / "level_1.json", {
        "trades": f"#{NS}:{profession}/all",
        "amount": len(trades),
    })

    # Levels still exist in the engine. Emptying them removes trade unlocks
    # without fighting the level system itself.
    for level in LEVELS[1:]:
        write_json(DATA / "minecraft/trade_set" / profession / f"level_{level}.json", {
            "trades": f"#{NS}:{profession}/empty",
            "amount": 0,
        })


def write_catalog(merchant: str, trades: dict[str, dict[str, Any]]) -> None:
    """Write trades plus an all and an empty tag for trade sets to point at."""
    CATALOGS[merchant] = trades
    for name, value in trades.items():
        write_json(DATA / NS / "villager_trade" / merchant / f"{name}.json", value)

    # Vanilla trade sets always point at a tag rather than an inline list, so we
    # publish our own tag in the sav namespace. Overriding the minecraft: tag
    # would merge with vanilla's entries instead of replacing them.
    ids = [f"{NS}:{merchant}/{name}" for name in trades]
    write_json(DATA / NS / "tags/villager_trade" / merchant / "all.json", {"values": ids})
    write_json(DATA / NS / "tags/villager_trade" / merchant / "empty.json", {"values": []})


def install_wandering_trader() -> None:
    """Vanilla's Wandering Trader catalog, minus anything a Villager already
    trades, offered in full at fixed prices. Run after every Villager catalog.

    Its buying trades all go. Water and Milk Buckets refill for free, and the
    rest undercut the Farmer or sit above the cost of their Cleric-bought
    ingredients, so each one is an Emerald loop."""
    serviced = {
        side["id"]
        for trades in CATALOGS.values()
        for entry in trades.values()
        for side in (entry["wants"], entry["gives"])
        if not is_currency(side)
    }
    trades: dict[str, dict[str, Any]] = {}
    for path in sorted((VANILLA / "villager_trade/wandering_trader").glob("*.json")):
        vanilla = json.loads(path.read_text(encoding="utf-8"))
        wants, gives = vanilla["wants"], vanilla["gives"]
        if wants["id"] != "minecraft:emerald" or gives["id"] in serviced:
            continue
        item = gives["id"].removeprefix("minecraft:")
        entry = trade("emerald", wants.get("count", 1), item, gives.get("count", 1))
        if "given_item_modifier" in vanilla:
            modifier = vanilla["given_item_modifier"]
            entry["given_item_modifier"] = modifier if isinstance(modifier, list) else [modifier]
        trades[f"sell_{item}"] = entry

    write_catalog("wandering_trader", by_price(trades))
    # The three trade set IDs the Wandering Trader consults are hardcoded.
    write_json(DATA / "minecraft/trade_set/wandering_trader/common.json", {
        "trades": f"#{NS}:wandering_trader/all",
        "amount": len(trades),
    })
    for name in ("uncommon", "buying"):
        write_json(DATA / "minecraft/trade_set/wandering_trader" / f"{name}.json", {
            "trades": f"#{NS}:wandering_trader/empty",
            "amount": 0,
        })


def book_price(enchantment: str, index: dict[str, list[dict[str, Any]]]) -> int:
    """A tier-I Book costs what Super Awesome Enchanting charges for one tier:
    the catalyst's value plus the usual premium. Combining Books on an Anvil
    stays the dearer route to high tiers."""
    catalyst, required, _ = CATALYSTS[enchantment]
    cost = material_cost(f"minecraft:{catalyst}", index)
    if cost == float("inf"):
        raise SystemExit(f"No value for the {enchantment} catalyst {catalyst}")
    return max(1, math.ceil(cost * required * PREMIUM))


def install_librarian(index: dict[str, list[dict[str, Any]]]) -> None:
    vanilla = {path.stem for path in (VANILLA / "enchantment").glob("*.json")}
    missing = vanilla - BOOK_EXCLUDED - CATALYSTS.keys()
    if missing:
        raise SystemExit(f"Super Awesome Enchanting has no catalyst for {sorted(missing)}")
    trades: dict[str, dict[str, Any]] = {}
    for enchantment in sorted(vanilla - BOOK_EXCLUDED):
        currency, count = emerald_cost(book_price(enchantment, index))
        trades[f"book_{enchantment}"] = trade(
            currency,
            count,
            "enchanted_book",
            1,
            components={
                "minecraft:stored_enchantments": {f"minecraft:{enchantment}": 1},
            },
        )
    install_profession("librarian", by_price(trades))


def install_raid_reward() -> None:
    """Hero of the Village has no data pack control and its discount opens
    profitable loops in a fixed-price economy, so the effect is swapped for a
    flat payout. The badge level tracks raid difficulty, so it stands in for
    waves cleared."""
    for amplifier in range(5):
        write_json(DATA / NS / "predicate" / f"raid_level_{amplifier + 1}.json", {
            # The predicate registry keys on "type" in 26.3, not "condition".
            "type": "minecraft:entity_properties",
            "entity": "this",
            "predicate": {
                "effects": {
                    "minecraft:hero_of_the_village": {"amplifier": amplifier},
                }
            },
        })

    lines = [
        f"execute if predicate {NS}:raid_level_{level} "
        f"run give @s minecraft:emerald {4 * level}"
        for level in range(1, 6)
    ]
    lines.append("effect clear @s minecraft:hero_of_the_village")
    lines.append(f"advancement revoke @s only {NS}:raid_reward")
    write_text(DATA / NS / "function" / "raid_reward.mcfunction", "\n".join(lines))

    write_json(DATA / NS / "advancement" / "raid_reward.json", {
        "criteria": {
            "won_raid": {"trigger": "minecraft:hero_of_the_village"},
        },
        "rewards": {"function": f"{NS}:raid_reward"},
    })


def resolve_item_tag(spec: str, seen: frozenset[str] = frozenset()) -> list[str]:
    """Flatten a #tag reference into concrete item IDs."""
    if not spec.startswith("#"):
        return [spec if ":" in spec else f"minecraft:{spec}"]
    identifier = spec[1:]
    namespace, path = identifier.split(":", 1) if ":" in identifier else ("minecraft", identifier)
    if identifier in seen or namespace != "minecraft":
        return []
    source = VANILLA / "tags/item" / f"{path}.json"
    if not source.exists():
        return []
    values = json.loads(source.read_text(encoding="utf-8"))["values"]
    out: list[str] = []
    for value in values:
        entry = value["id"] if isinstance(value, dict) else value
        out.extend(resolve_item_tag(entry, seen | {identifier}))
    return out


def recipe_index() -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for path in sorted((VANILLA / "recipe").glob("*.json")):
        recipe = json.loads(path.read_text(encoding="utf-8"))
        if recipe.get("type") not in ("minecraft:crafting_shaped", "minecraft:crafting_shapeless"):
            continue
        result = recipe.get("result", {}).get("id")
        if result:
            index.setdefault(result, []).append(recipe)
    return index


def ingredients_of(recipe: dict[str, Any]) -> list[str]:
    if recipe["type"] == "minecraft:crafting_shapeless":
        return [i["item"] if isinstance(i, dict) else i for i in recipe["ingredients"]]
    key = recipe["key"]
    out: list[str] = []
    for row in recipe["pattern"]:
        for symbol in row:
            if symbol != " ":
                entry = key[symbol]
                out.append(entry["item"] if isinstance(entry, dict) else entry)
    return out


def material_cost(item: str, index: dict[str, list[dict[str, Any]]], seen: frozenset[str] = frozenset()) -> float:
    """Emerald value of an item, resolved through vanilla crafting recipes down
    to the base materials this pack actually sells."""
    short = item.removeprefix("minecraft:")
    if short in BASE_VALUES:
        return BASE_VALUES[short]
    if item in seen or item not in index:
        return float("inf")
    best = float("inf")
    for recipe in index[item]:
        count = recipe.get("result", {}).get("count", 1)
        total = 0.0
        for ingredient in ingredients_of(recipe):
            # An ingredient is an item, a #tag, or a list of either.
            choices = ingredient if isinstance(ingredient, list) else [ingredient]
            options = [o for choice in choices for o in resolve_item_tag(choice)]
            costs = [material_cost(o, index, seen | {item}) for o in options]
            total += min(costs, default=float("inf"))
        best = min(best, total / count)
    return best


def premium_value(item: str, index: dict[str, list[dict[str, Any]]]) -> float:
    cost = material_cost(f"minecraft:{item}", index)
    if cost == float("inf"):
        raise SystemExit(f"No recipe path to a base material for {item}")
    return cost * PREMIUM


def equipment_price(item: str, index: dict[str, list[dict[str, Any]]]) -> int:
    """Material cost plus a 25 percent convenience premium, floored at 1 Emerald
    and rounded up. Most cheap gear therefore lands at exactly 1."""
    if item in HAND_PRICED:
        return HAND_PRICED[item]
    return max(1, math.ceil(premium_value(item, index)))


def bulk_trade(item: str, index: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    """Like equipment, but anything worth less than an Emerald is sold as the
    largest ladder quantity 1 Emerald still covers."""
    value = premium_value(item, index)
    if value >= 1:
        return trade(*emerald_cost(math.ceil(value)), item, 1)
    return trade("emerald", 1, item, max(n for n in LADDER if n * value <= 1))


def publish_values() -> None:
    """Every rate the pack states becomes a base value for derived prices.
    Explicit BASE_VALUES entries win."""
    for log in resolve_item_tag("#minecraft:logs"):
        BASE_VALUES.setdefault(log.removeprefix("minecraft:"), STANDARD_PRICE / 16)
    for ladder in (MASON_LADDER, CLERIC_LADDER, SHEPHERD_LADDER, LEATHERWORKER_LADDER):
        for count, items in ladder.items():
            for item in items:
                BASE_VALUES.setdefault(item, STANDARD_PRICE / count)
    for rows in (FISHERMAN_BUYS, FARMER_BUYS, BUTCHER_BUYS):
        for emeralds, item, count in rows:
            BASE_VALUES.setdefault(item, emeralds / count)
    for item, price in HAND_PRICED.items():
        BASE_VALUES.setdefault(item, float(price))


def install_buyer(profession: str, rows: list[tuple[int, str, int]]) -> None:
    install_profession(profession, by_price({
        f"buy_{item}": trade(
            item, count, "emerald", emeralds,
            wants_components=UNMARKED if item in VILLAGER_CROPS else None,
        )
        for emeralds, item, count in rows
    }))


def install_villager_crops() -> None:
    """Vanilla crop loot tables, with every drop of the crop itself marked when
    the block was broken by a villager. Seeds and Poisonous Potatoes are not
    traded, so they are left alone."""
    by_villager = {
        "type": "minecraft:entity_properties",
        "entity": "this",
        "predicate": {"minecraft:entity_type": "minecraft:villager"},
    }
    for item, block in VILLAGER_CROPS.items():
        table = json.loads((VANILLA / "loot_table/blocks" / f"{block}.json").read_text(encoding="utf-8"))
        marked = 0
        for pool in table["pools"]:
            for entry in pool["entries"]:
                for option in entry.get("children", [entry]):
                    if option.get("name") != f"minecraft:{item}":
                        continue
                    modifier = option.get("modifier", [])
                    option["modifier"] = [
                        *(modifier if isinstance(modifier, list) else [modifier]),
                        {
                            "type": "minecraft:set_components",
                            "condition": by_villager,
                            "components": {"minecraft:rarity": "uncommon"},
                        },
                        {
                            "type": "minecraft:set_name",
                            "condition": by_villager,
                            "target": "item_name",
                            "name": ["Haram ", {"translate": f"item.minecraft.{item}"}],
                        },
                    ]
                    marked += 1
        if not marked:
            raise SystemExit(f"No {item} drop found in the vanilla {block} loot table")
        write_json(DATA / "minecraft/loot_table/blocks" / f"{block}.json", table)


def ladder_trades(ladder: dict[int, list[str]]) -> dict[str, dict[str, Any]]:
    """Every stackable purchase costs 1 Emerald; the output quantity carries
    the value."""
    return {
        f"sell_{item}": trade("emerald", STANDARD_PRICE, item, output)
        for output, items in ladder.items()
        for item in items
    }


def install_vendors(index: dict[str, list[dict[str, Any]]]) -> set[str]:
    """Returns the professions whose catalogs include derived equipment."""
    priced: set[str] = set()

    def equipment(profession: str, items: list[str]) -> dict[str, dict[str, Any]]:
        priced.add(profession)
        out: dict[str, dict[str, Any]] = {}
        for item in items:
            currency, count = emerald_cost(equipment_price(item, index))
            out[f"sell_{item}"] = trade(currency, count, item, 1)
        return out

    def smith(profession: str, extras: list[str], pieces: tuple[str, ...]) -> dict[str, dict[str, Any]]:
        return {
            **by_price(equipment(profession, extras)),
            **equipment(profession, [f"{tier}_{piece}" for tier in EQUIPMENT_TIERS for piece in pieces]),
        }

    # The tag also carries stripped variants, Wood and Hyphae. Players can make
    # those from the base material, so only raw Logs and Stems are sold.
    logs = sorted({
        item.removeprefix("minecraft:")
        for item in resolve_item_tag("#minecraft:logs")
        if not item.removeprefix("minecraft:").startswith("stripped_")
        and not item.endswith(("_wood", "_hyphae"))
    })
    install_profession("fletcher", by_price({
        **ladder_trades({16: logs + ["arrow"]}),
        **equipment("fletcher", ["bow", "crossbow"]),
    }))

    install_profession("mason", by_price(ladder_trades(MASON_LADDER)))

    install_profession("shepherd", by_price(ladder_trades(SHEPHERD_LADDER)))

    install_profession("leatherworker", by_price({
        **ladder_trades(LEATHERWORKER_LADDER),
        **equipment("leatherworker", [
            "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots",
            "saddle", "leather_horse_armor",
        ]),
    }))

    install_profession("cleric", by_price({
        **ladder_trades(CLERIC_LADDER),
        **equipment("cleric", ["ender_pearl", "sculk_sensor", "sculk_shrieker", "sculk_catalyst"]),
        **{f"sell_{item}": bulk_trade(item, index) for item in REDSTONE},
    }))

    install_profession("cartographer", by_price({
        **explorer_map_trades(),
        **equipment("cartographer", ["compass", "spyglass"]),
    }))

    install_profession("armorer", smith("armorer", ["shield"], ARMOR_PIECES))
    install_profession("toolsmith", smith(
        "toolsmith", ["shears", "flint_and_steel", "bucket"], TOOL_PIECES,
    ))
    install_profession("weaponsmith", smith("weaponsmith", [], WEAPON_PIECES))

    return priced


def explorer_map_trades() -> dict[str, dict[str, Any]]:
    """Reuse vanilla's own exploration_map modifiers rather than hardcoding
    structure IDs, but at a flat price and without the Compass requirement."""
    out: dict[str, dict[str, Any]] = {}
    for path in sorted((VANILLA / "villager_trade/cartographer").rglob("*.json")):
        vanilla = json.loads(path.read_text(encoding="utf-8"))
        modifier = vanilla.get("given_item_modifier")
        if not modifier or not any(m.get("type") == "minecraft:exploration_map" for m in modifier):
            continue
        name = vanilla["gives"]["id"].removeprefix("minecraft:")
        entry = trade("emerald", MAP_PRICE, name, 1)
        entry["given_item_modifier"] = modifier
        out[f"sell_{name}"] = entry
    return out


def sync_readme(priced: set[str]) -> None:
    """The README is the playtest rulebook, so the generator owns its tables."""
    text = README.read_text(encoding="utf-8")
    for name, body in {
        "fisherman": buyer_table("fisherman", {
            "cod", "salmon", "pufferfish", "tropical_fish", "diamond", "quartz",
            "enchanted_golden_apple", "nether_star", "dragon_egg",
        }),
        "books": book_table(),
        "farmer": buyer_table("farmer"),
        "butcher": buyer_table("butcher"),
        "cleric": vendor_table("cleric"),
        "wandering_trader": vendor_table("wandering_trader"),
        "equipment": equipment_table(priced - {"cleric"}),
    }.items():
        opening = f"<!-- generated:{name} -->"
        closing = f"<!-- /generated:{name} -->"
        start = text.find(opening)
        end = text.find(closing)
        if start == -1 or end == -1:
            raise SystemExit(f"README is missing the {name} markers")
        text = text[: start + len(opening)] + "\n" + body + "\n" + text[end:]
    README.write_text(text, encoding="utf-8")


# Items whose display name does not fall out of the ID, and items the tables
# pluralize when a trade asks for more than one.
DISPLAY_NAMES = {
    "heart_of_the_sea": "Heart of the Sea",
    "flint_and_steel": "Flint and Steel",
    "rabbit_foot": "Rabbit's Foot",
    "tnt": "TNT",
    "bane_of_arthropods": "Bane of Arthropods",
    "luck_of_the_sea": "Luck of the Sea",
    "lily_of_the_valley": "Lily of the Valley",
}
PLURALS = {"birch_log", "diamond", "echo_shard", "torchflower", "pitcher_plant", "nether_star"}


def title(item: str, count: int = 1) -> str:
    name = DISPLAY_NAMES.get(item) or " ".join(part.capitalize() for part in item.split("_"))
    if count > 1 and item in PLURALS:
        name += "s"
    return name


def money(item: dict[str, Any]) -> str:
    count = item["count"]
    return f"{count} {title(item['id'].removeprefix('minecraft:'))}{'' if count == 1 else 's'}"


def buyer_table(profession: str, proposed: set[str] | None = None) -> str:
    """Rows follow the in-game offer order. Without a proposed set, every rate
    is still proposed."""
    lines = [
        f"| {title(profession)} gives | Player gives | Status |",
        "| ---: | ---: | --- |",
    ]
    for entry in CATALOGS[profession].values():
        item = entry["wants"]["id"].removeprefix("minecraft:")
        count = entry["wants"]["count"]
        status = "Proposed rate" if proposed is None or item in proposed else "Current design"
        lines.append(f"| {money(entry['gives'])} | {count} {title(item, count)} | {status} |")
    return "\n".join(lines)


def equipment_table(priced: set[str]) -> str:
    """Every single-item vendor trade, in the in-game offer order."""
    lines = ["| Profession | Item | Price |", "| --- | --- | ---: |"]
    for profession in sorted(priced):
        for entry in CATALOGS[profession].values():
            gives = entry["gives"]
            if gives["count"] != 1 or "given_item_modifier" in entry:
                continue
            item = gives["id"].removeprefix("minecraft:")
            lines.append(f"| {title(profession)} | {title(item)} | {money(entry['wants'])} |")
    return "\n".join(lines)


def vendor_table(profession: str) -> str:
    """Every offer a vendor makes, in the in-game offer order."""
    lines = ["| Price | Player gets |", "| ---: | ---: |"]
    for entry in CATALOGS[profession].values():
        gives = entry["gives"]
        lines.append(f"| {money(entry['wants'])} | {gives['count']} {title(gives['id'].removeprefix('minecraft:'))} |")
    return "\n".join(lines)


def book_table() -> str:
    """Book prices beside the catalyst they are derived from."""
    lines = ["| Book | Catalyst per tier | Price |", "| --- | --- | ---: |"]
    for entry in CATALOGS["librarian"].values():
        (enchantment,) = entry["gives"]["components"]["minecraft:stored_enchantments"]
        name = enchantment.removeprefix("minecraft:")
        catalyst, required, _ = CATALYSTS[name]
        lines.append(f"| {title(name)} I | {required} {title(catalyst)} | {money(entry['wants'])} |")
    return "\n".join(lines)


def main() -> None:
    if not VANILLA.exists():
        raise SystemExit("Missing .cache vanilla data")
    if DATA.exists():
        shutil.rmtree(DATA)

    publish_values()
    load_blocks()
    index = recipe_index()
    install_metadata()
    install_buyer("fisherman", FISHERMAN_BUYS)
    install_librarian(index)
    install_buyer("farmer", FARMER_BUYS)
    install_villager_crops()
    install_buyer("butcher", BUTCHER_BUYS)
    priced = install_vendors(index)
    install_wandering_trader()
    install_raid_reward()
    install_stocking()
    sync_readme(priced)
    print(", ".join(f"{len(trades)} {profession}" for profession, trades in CATALOGS.items()))


if __name__ == "__main__":
    main()
