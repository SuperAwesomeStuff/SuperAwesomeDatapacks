from __future__ import annotations

import json
import math
import shutil
from pathlib import Path
from typing import Any


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


# Buyer catalogs: (emeralds_given, item_wanted, count_wanted)
FISHERMAN_BUYS: list[tuple[int, str, int]] = [
    (2, "birch_log", 64),
    (16, "diamond", 1),
    (32, "ancient_debris", 1),
    (32, "heart_of_the_sea", 1),
    (8, "echo_shard", 1),
    (4, "raw_copper", 32),
    (4, "lapis_lazuli", 32),
    (4, "raw_iron", 16),
    (4, "raw_gold", 8),
    (4, "cod", 64),
    (4, "salmon", 64),
    (4, "pufferfish", 32),
    (4, "tropical_fish", 32),
]

# Every stackable resource purchase costs this much; the output quantity is what
# communicates value. Quantities stay on the ladder 64/48/32/24/16/8/4/2/1.
STANDARD_PRICE = 4

FARMER_BUYS: list[tuple[int, str, int]] = [
    (2, "wheat", 64),
    (2, "carrot", 64),
    (2, "potato", 64),
    (2, "beetroot", 64),
    (2, "nether_wart", 32),
    (2, "apple", 16),
    (2, "chorus_fruit", 32),
    (2, "baked_potato", 32),
    (2, "pumpkin_pie", 16),
]

BUTCHER_BUYS: list[tuple[int, str, int]] = [
    (2, "beef", 8),
    (2, "cooked_beef", 6),
    (2, "mutton", 8),
    (2, "cooked_mutton", 6),
    (2, "rabbit", 4),
    (2, "cooked_rabbit", 3),
    (2, "rabbit_hide", 8),
]

MASON_LADDER: dict[int, list[str]] = {
    64: [
        "cobblestone", "cobbled_deepslate", "dirt", "gravel", "granite", "diorite",
        "andesite", "tuff", "netherrack", "basalt", "blackstone", "end_stone",
    ],
    48: ["stone", "deepslate"],
    32: [
        "smooth_stone", "sand", "red_sand", "clay", "soul_sand", "soul_soil",
        "dripstone_block", "calcite",
    ],
    24: ["glass", "terracotta", "nether_bricks", "prismarine", "purpur_block"],
    16: ["glowstone"],
    8: ["obsidian"],
}

# Brewing ingredients that cannot be farmed easily, plus the Overworld mob drops
# that otherwise require building a farm. Rabbit Hide is absent because the
# Butcher buys it; Bone sits at 32 rather than 64 because Bone Meal grows crops
# the Farmer buys.
CLERIC_LADDER: dict[int, list[str]] = {
    64: ["string", "rotten_flesh", "feather", "flint"],
    32: ["bone", "gunpowder", "spider_eye", "ink_sac"],
    16: ["slime_ball", "glow_ink_sac", "blaze_powder"],
    8: ["rabbit_foot", "phantom_membrane"],
    4: ["ghast_tear"],
}

ENDER_PEARL_PRICE = 8
MAP_PRICE = 16

DYE_COLOURS = [
    "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray",
    "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black",
]

# Seeds for the equipment price derivation: the Emerald value of one unit of
# each base material, taken from the rates this pack already publishes.
BASE_VALUES: dict[str, float] = {
    "emerald": 1.0,
    "iron_ingot": STANDARD_PRICE / 16,
    "gold_ingot": STANDARD_PRICE / 8,
    "copper_ingot": STANDARD_PRICE / 32,
    "diamond": 16.0,
    "lapis_lazuli": STANDARD_PRICE / 32,
    "string": STANDARD_PRICE / 64,
    "flint": STANDARD_PRICE / 64,
    "feather": STANDARD_PRICE / 64,
    "leather": STANDARD_PRICE / 32,
    "cobblestone": STANDARD_PRICE / 64,
    "glass": STANDARD_PRICE / 24,
    "obsidian": STANDARD_PRICE / 8,
    "amethyst_shard": STANDARD_PRICE / 32,
    "redstone": STANDARD_PRICE / 64,
    "coal": STANDARD_PRICE / 64,
    "gunpowder": STANDARD_PRICE / 32,
}

# Items with no crafting recipe, so nothing to derive a price from.
HAND_PRICED_EQUIPMENT: dict[str, int] = {
    "saddle": 8,
    "leather_horse_armor": 8,
}

# Book pricing. Multi-tier enchantments are cheap because anvil combining
# supplies the real cost curve; single-tier enchantments have no combining
# penalty, so the shelf price is the final price.
BOOK_PRICE_MULTI_TIER = 8
BOOK_PRICE_SINGLE_TIER = 64

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
) -> dict[str, Any]:
    given: dict[str, Any] = {"id": f"minecraft:{gives}", "count": gives_count}
    if components:
        given["components"] = components
    return {
        "wants": {"id": f"minecraft:{wants}", "count": wants_count},
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


def install_profession(profession: str, trades: dict[str, dict[str, Any]]) -> None:
    """Write a profession's trades and pin the whole catalog to level 1."""
    for name, value in trades.items():
        write_json(DATA / NS / "villager_trade" / profession / f"{name}.json", value)

    # Vanilla trade sets always point at a tag rather than an inline list, so we
    # publish our own tag in the sav namespace. Overriding the minecraft: tag
    # would merge with vanilla's entries instead of replacing them.
    ids = [f"{NS}:{profession}/{name}" for name in trades]
    write_json(DATA / NS / "tags/villager_trade" / profession / "level_1.json", {"values": ids})
    write_json(DATA / NS / "tags/villager_trade" / profession / "empty.json", {"values": []})

    write_json(DATA / "minecraft/trade_set" / profession / "level_1.json", {
        "trades": f"#{NS}:{profession}/level_1",
        "amount": len(ids),
    })

    # Levels still exist in the engine. Emptying them removes trade unlocks
    # without fighting the level system itself.
    for level in LEVELS[1:]:
        write_json(DATA / "minecraft/trade_set" / profession / f"level_{level}.json", {
            "trades": f"#{NS}:{profession}/empty",
            "amount": 0,
        })


def install_fisherman() -> list[tuple[int, str, int]]:
    trades = {
        f"buy_{item}": trade(item, count, "emerald", emeralds)
        for emeralds, item, count in FISHERMAN_BUYS
    }
    install_profession("fisherman", trades)
    return FISHERMAN_BUYS


def enchantments_by_tier() -> tuple[list[str], list[str]]:
    source = VANILLA / "enchantment"
    multi: list[str] = []
    single: list[str] = []
    for path in sorted(source.glob("*.json")):
        name = path.stem
        if name in BOOK_EXCLUDED:
            continue
        definition = json.loads(path.read_text(encoding="utf-8"))
        target = single if definition.get("max_level", 1) == 1 else multi
        target.append(name)
    return multi, single


def install_librarian() -> tuple[list[str], list[str]]:
    multi, single = enchantments_by_tier()
    trades: dict[str, dict[str, Any]] = {}
    for enchantment, price in [(e, BOOK_PRICE_MULTI_TIER) for e in multi] + [
        (e, BOOK_PRICE_SINGLE_TIER) for e in single
    ]:
        trades[f"book_{enchantment}"] = trade(
            "emerald",
            price,
            "enchanted_book",
            1,
            components={
                "minecraft:stored_enchantments": {f"minecraft:{enchantment}": 1},
            },
        )
    install_profession("librarian", trades)
    return multi, single


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
            options = resolve_item_tag(ingredient) if ingredient.startswith("#") else [ingredient]
            costs = [material_cost(o, index, seen | {item}) for o in options]
            total += min(costs, default=float("inf"))
        best = min(best, total / count)
    return best


def equipment_price(item: str, index: dict[str, list[dict[str, Any]]]) -> int:
    """Material cost plus a 25 percent convenience premium, floored at 1 Emerald
    and rounded up. Most cheap gear therefore lands at exactly 1."""
    if item in HAND_PRICED_EQUIPMENT:
        return HAND_PRICED_EQUIPMENT[item]
    cost = material_cost(f"minecraft:{item}", index)
    if cost == float("inf"):
        raise SystemExit(f"No recipe path to a base material for {item}")
    return max(1, math.ceil(cost * 1.25))


def install_buyer(profession: str, rows: list[tuple[int, str, int]]) -> None:
    install_profession(profession, {
        f"buy_{item}": trade(item, count, "emerald", emeralds)
        for emeralds, item, count in rows
    })


def ladder_trades(ladder: dict[int, list[str]]) -> dict[str, dict[str, Any]]:
    """Every stackable purchase costs 4 Emeralds; the output quantity carries
    the value."""
    return {
        f"sell_{item}": trade("emerald", STANDARD_PRICE, item, output)
        for output, items in ladder.items()
        for item in items
    }


def install_vendors(index: dict[str, list[dict[str, Any]]]) -> dict[str, list[tuple[str, int]]]:
    priced: dict[str, list[tuple[str, int]]] = {}

    def equipment(profession: str, items: list[str]) -> dict[str, dict[str, Any]]:
        out: dict[str, dict[str, Any]] = {}
        for item in items:
            price = equipment_price(item, index)
            priced.setdefault(profession, []).append((item, price))
            out[f"sell_{item}"] = trade("emerald", price, item, 1)
        return out

    # The tag also carries stripped variants, Wood and Hyphae. Players can make
    # those from the base material, so only raw Logs and Stems are sold.
    logs = sorted({
        item.removeprefix("minecraft:")
        for item in resolve_item_tag("#minecraft:logs")
        if not item.removeprefix("minecraft:").startswith("stripped_")
        and not item.endswith(("_wood", "_hyphae"))
    })
    install_profession("fletcher", {
        **ladder_trades({64: logs + ["arrow"]}),
        **equipment("fletcher", ["bow", "crossbow"]),
    })

    install_profession("mason", ladder_trades(MASON_LADDER))

    install_profession("shepherd", ladder_trades({
        16: [f"{colour}_wool" for colour in DYE_COLOURS],
        32: [f"{colour}_dye" for colour in DYE_COLOURS],
    }))

    install_profession("leatherworker", {
        **ladder_trades({32: ["leather"]}),
        **equipment("leatherworker", [
            "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots",
            "saddle", "leather_horse_armor",
        ]),
    })

    install_profession("cleric", {
        **ladder_trades(CLERIC_LADDER),
        # The one stackable purchase off the 4-Emerald standard. End access
        # should be buyable but expensive.
        "sell_ender_pearl": trade("emerald", ENDER_PEARL_PRICE, "ender_pearl", 1),
    })

    install_profession("cartographer", {
        **explorer_map_trades(),
        **equipment("cartographer", ["compass", "spyglass"]),
    })

    install_profession("armorer", equipment("armorer", [
        "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots", "shield",
    ]))
    install_profession("toolsmith", equipment("toolsmith", [
        "iron_pickaxe", "iron_axe", "iron_shovel", "iron_hoe",
        "shears", "flint_and_steel", "bucket",
    ]))
    install_profession("weaponsmith", equipment("weaponsmith", ["iron_sword", "iron_axe"]))

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


def sync_readme(
    fisherman: list[tuple[int, str, int]],
    books: tuple[list[str], list[str]],
    priced: dict[str, list[tuple[str, int]]],
) -> None:
    """The README is the playtest rulebook, so the generator owns its tables."""
    text = README.read_text(encoding="utf-8")
    for name, body in {
        "fisherman": fisherman_table(fisherman),
        "books": book_summary(books),
        "farmer": buyer_table("Farmer", FARMER_BUYS),
        "butcher": buyer_table("Butcher", BUTCHER_BUYS),
        "equipment": equipment_table(priced),
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
}
PLURALS = {"birch_log", "diamond", "echo_shard"}


def title(item: str, count: int = 1) -> str:
    name = DISPLAY_NAMES.get(item) or " ".join(part.capitalize() for part in item.split("_"))
    if count > 1 and item in PLURALS:
        name += "s"
    return name


def fisherman_table(rows: list[tuple[int, str, int]]) -> str:
    proposed = {"cod", "salmon", "pufferfish", "tropical_fish"}
    lines = [
        "| Fisherman gives | Player gives | Status |",
        "| ---: | ---: | --- |",
    ]
    for emeralds, item, count in rows:
        status = "Proposed rate" if item in proposed else "Current design"
        lines.append(f"| {emeralds} Emeralds | {count} {title(item, count)} | {status} |")
    return "\n".join(lines)


def buyer_table(profession: str, rows: list[tuple[int, str, int]]) -> str:
    lines = [
        f"| {profession} gives | Player gives | Status |",
        "| ---: | ---: | --- |",
    ]
    for emeralds, item, count in rows:
        lines.append(f"| {emeralds} Emeralds | {count} {title(item, count)} | Proposed rate |")
    return "\n".join(lines)


def equipment_table(priced: dict[str, list[tuple[str, int]]]) -> str:
    lines = ["| Profession | Item | Price |", "| --- | --- | ---: |"]
    for profession in sorted(priced):
        for item, price in sorted(priced[profession], key=lambda row: (-row[1], row[0])):
            plural = "Emerald" if price == 1 else "Emeralds"
            lines.append(f"| {title(profession)} | {title(item)} | {price} {plural} |")
    return "\n".join(lines)


def book_summary(books: tuple[list[str], list[str]]) -> str:
    multi, single = books
    return (
        f"The catalog is {len(multi) + len(single)} Books: "
        f"{len(multi)} multi-tier enchantments at {BOOK_PRICE_MULTI_TIER} Emeralds "
        f"and {len(single)} single-tier enchantments at {BOOK_PRICE_SINGLE_TIER} Emeralds. "
        "Curses and Mending are excluded."
    )


def main() -> None:
    if not VANILLA.exists():
        raise SystemExit("Missing .cache vanilla data")
    if DATA.exists():
        shutil.rmtree(DATA)

    # Every Log and Stem is sold at the same rate, which is what gives Planks
    # and Sticks a value for the equipment derivation.
    for log in resolve_item_tag("#minecraft:logs"):
        BASE_VALUES.setdefault(log.removeprefix("minecraft:"), STANDARD_PRICE / 64)

    install_metadata()
    fisherman = install_fisherman()
    books = install_librarian()
    install_buyer("farmer", FARMER_BUYS)
    install_buyer("butcher", BUTCHER_BUYS)
    priced = install_vendors(recipe_index())
    install_raid_reward()
    sync_readme(fisherman, books, priced)
    multi, single = books
    print(
        f"Generated {len(fisherman)} Fisherman trades and "
        f"{len(multi) + len(single)} Librarian Books"
    )


if __name__ == "__main__":
    main()
