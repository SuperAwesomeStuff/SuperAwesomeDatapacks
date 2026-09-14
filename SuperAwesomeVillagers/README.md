# Super Awesome Villagers

Super Awesome Villagers replaces Minecraft's random, limited Villager trades with deterministic profession catalogs. Trading becomes a predictable secondary route to resources for players who would rather earn Emeralds through one activity than gather every material directly.

**Status:** In design. There is no playable release yet.

**Target:** Minecraft Java Edition 26.3.

## Goals

- Keep Villager trading secondary to normal gathering and progression.
- Make inconvenient bulk resources easier to obtain without turning Villagers into progression skips.
- Give every profession a complete, predictable catalog without trade rerolling.
- Keep the economy understandable enough that players can compare trades without a calculator.
- Work as a standalone data pack.

## Core trade rules

- Every Villager of the same profession has the same complete catalog.
- Every offer is available as soon as a Villager takes a profession. Profession tiers and trade unlocks are removed.
- Trades have unlimited uses and do not restock.
- Prices are fixed. Demand, curing, reputation, and Hero of the Village do not change them.
- Custom trades grant no player XP. Exact-value exchanges could otherwise become a free XP loop.
- Professions, workstations, breeding, and the physical parts of Villager play remain close to vanilla. This pack changes the economy rather than dictating whether players build villages or trading halls.

## Economic structure

Farmers, Fishermen, and Butchers are buyer professions. They give players Emeralds for goods. The remaining professions are vendors that take Emeralds in exchange for resources or equipment.

No combination of trades and crafting recipes should produce a profitable loop. Birch Logs are the deliberate exception to the usual buy-low and sell-high spread because they are the economy's reference good.

Emerald income should normally require a non-renewable resource or recurring player involvement. Holding an input while AFK does not count as involvement. Farming is a limited exception: selected automated crops and prepared foods may still earn one Emerald when the rate is low enough.

The reference rate is:

> 4 Emeralds = 64 Birch Logs = 64 ordinary bulk blocks

A Fisherman buys 64 Birch Logs for 4 Emeralds. A Fletcher sells 64 of any raw Log or Stem type for 4 Emeralds. One stack of Birch Logs can therefore be exchanged for one stack of another wood type.

Villagers do not buy larger tree types because a tree-capitator data pack makes them too productive. They also do not sell Planks, Stripped Logs, Wood, Hyphae, Bamboo Blocks, or other simple derivatives. Players can make those from the base material.

## Standard resource purchases

Every stackable resource purchase costs 4 Emeralds. The output quantity communicates the resource's value. Quantities should use the readable ladder `64, 48, 32, 24, 16, 8, 4, 2, 1` whenever possible.

| Output for 4 Emeralds | Resources |
| ---: | --- |
| 64 | Logs and Stems, Cobblestone, Cobbled Deepslate, Dirt, Gravel, Granite, Diorite, Andesite, Tuff, Netherrack, Basalt, Blackstone |
| 48 | Stone, Deepslate |
| 32 | Smooth Stone, Sand, Red Sand, Clay Blocks |
| 24 | Glass, Terracotta, Nether Bricks |
| 16 | Glowstone |
| 8 | Obsidian |

The following intended resources still need output quantities:

| Cost | Resource | Output |
| --- | --- | ---: |
| 4 Emeralds | End Stone | To be decided |
| 4 Emeralds | Dripstone Blocks | To be decided |
| 4 Emeralds | Calcite | To be decided |
| 4 Emeralds | Prismarine | To be decided |
| 4 Emeralds | Soul Sand | To be decided |
| 4 Emeralds | Soul Soil | To be decided |
| 4 Emeralds | Purpur | To be decided |

Emerald Blocks may replace large stacks of Emeralds for trades that cost more than 64 Emeralds. They should be used only when the price requires it. Books, equipment, Maps, and Potions keep individual prices because output quantities cannot express their value.

## Buyer professions

### Farmer

Farmers buy selected crops and prepared foods. Cheap automated goods may be included at a low rate. Extremely productive goods such as Cocoa Beans are omitted because even one Emerald per stack would overvalue them.

| Farmer gives | Player gives | Status |
| ---: | ---: | --- |
| 1 Emerald | 64 Wheat | Current design |
| 1 Emerald | 64 Carrots | Current design |
| 1 Emerald | 64 Potatoes | Current design |
| 1 Emerald | 64 Beetroot | Current design |
| 1 Emerald | 32 Nether Wart | Current design |
| 1 Emerald | 16 Apples | Current design |
| 1 Emerald | 32 Chorus Fruit | Current design |
| 1 Emerald | 32 Baked Potatoes | Current design |
| 1 Emerald | 16 Pumpkin Pies | Current design |
| 1 Emerald | Cake | Quantity to be decided |

Bread is not included.

### Fisherman

The Fisherman is the general exchange profession. It buys Birch Logs, fish, mined valuables, and selected goods earned through active gathering or exploration.

| Fisherman gives | Player gives | Status |
| ---: | ---: | --- |
| 4 Emeralds | 64 Birch Logs | Current design |
| 16 Emeralds | 1 Diamond | Current design |
| 1 Emerald | 16 Cod | Proposed rate |
| 1 Emerald | 16 Salmon | Proposed rate |
| 1 Emerald | 8 Pufferfish | Proposed rate |
| 1 Emerald | 8 Tropical Fish | Proposed rate |

Mining trades should use forms that automatic farms do not produce. Raw Copper, Raw Iron, Raw Gold, Diamonds, and selected Ore blocks are candidates. Farmable processed metals, Coal, and Redstone should not become easy Emerald sources. The exact mining and exploration catalog remains open.

### Butcher

The Butcher buys animal products that practical automatic farms cannot produce cheaply. Leather, Porkchops, Chicken, Feathers, and Eggs are excluded as Emerald sources. Cooking earns a modest premium.

| Butcher gives | Player gives | Status |
| ---: | ---: | --- |
| 1 Emerald | 8 Raw Beef | Proposed rate |
| 1 Emerald | 6 Steak | Proposed rate |
| 1 Emerald | 8 Raw Mutton | Proposed rate |
| 1 Emerald | 6 Cooked Mutton | Proposed rate |
| 1 Emerald | 4 Raw Rabbit | Proposed rate |
| 1 Emerald | 3 Cooked Rabbit | Proposed rate |
| 1 Emerald | 8 Rabbit Hide | Proposed rate |

## Vendor professions

| Profession | Catalog role |
| --- | --- |
| Fletcher | Raw Logs and Stems, plus ranged equipment |
| Mason | Natural and selected smelted building materials |
| Shepherd | Wool and basic dye materials |
| Leatherworker | Functional leather goods; whether it sells raw Leather is unresolved |
| Cleric | Brewing ingredients and Potions |
| Cartographer | Maps and navigation items |
| Armorer | Unenchanted Armor |
| Toolsmith | Unenchanted Tools |
| Weaponsmith | Unenchanted Weapons |
| Librarian | Lowest-tier enchanted Books |

Catalogs prefer base materials over simple crafting variants. A processed block receives its own trade only when players commonly need it in bulk and processing it is tedious. Stone, Deepslate, Smooth Stone, Glass, Terracotta, and Nether Bricks are the initial smelting exceptions. Purpur Blocks are an explicit building-material exception.

Finished equipment is another exception. Villagers sell it unenchanted so they do not bypass Super Awesome Enchanting's catalyst system when both packs are installed. Prices should equal the material cost plus roughly a 25 percent convenience premium.

## Librarians

Librarians keep enchanted Books as an alternate route into enchanting.

- Every Librarian has the complete deterministic Book catalog from the start.
- Librarians sell the lowest tier of every enchantment except curses.
- When this pack runs alone, the catalog includes Mending.
- When Super Awesome Enchanting is installed, that pack removes Mending from Villager trades because it replaces Mending with Unbreakable.
- Librarians never sell Unbreakable.
- Books combine through vanilla Anvil rules. Reaching a high tier therefore requires exponentially more tier-I Books.
- Each Book has an individual price. Combining Books to an enchantment's maximum tier should cost substantially more than reaching it with catalysts.
- One-tier enchantments need direct prices based on their catalyst and usefulness because they do not incur a combining penalty.

## Open design work

- Verify that Java Edition 26.3 can enforce unlimited uses and remove demand and every discount reliably.
- Choose the Cake-to-Emerald exchange rate.
- Playtest the proposed Butcher rates.
- Decide whether the Leatherworker sells raw Leather. Hoglin farms prevent Villagers from buying it, but selling it to players does not create Emeralds.
- Complete the Fisherman's mining and exploration catalog and choose its rates.
- Set outputs for End Stone, Dripstone Blocks, Calcite, Prismarine, Soul Sand, Soul Soil, and Purpur.
- Complete the Fletcher, Shepherd, Leatherworker, Cleric, and Cartographer catalogs.
- Decide whether Armorers, Toolsmiths, and Weaponsmiths sell Diamond equipment immediately or stop at Iron.
- Price equipment, Maps, Potions, and every enchanted Book.
- Test whether the vanilla trading interface remains usable when a Librarian exposes the complete enchantment catalog at once.
- Audit every trade and crafting combination for profitable loops.

## Relationship to other packs

Super Awesome Villagers works without any other pack in this repository. Its deterministic trade economy does not require Super Awesome Enchanting.

When both are installed, equipment vendors still sell unenchanted gear, Librarians provide low-tier Books as the expensive alternative to catalysts, and Super Awesome Enchanting removes the standalone Mending trade.
