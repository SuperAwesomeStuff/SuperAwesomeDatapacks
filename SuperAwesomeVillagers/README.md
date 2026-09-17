# Super Awesome Villagers

Super Awesome Villagers replaces Minecraft's random, limited Villager trades with deterministic profession catalogs. Trading becomes a predictable secondary route to resources for players who would rather earn Emeralds through one activity than gather every material directly.

**Status:** In design. The first playtest build is being assembled.

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
- Trades have effectively unlimited uses.
- Prices are fixed. Demand, curing, and reputation do not change them.
- Professions, workstations, breeding, and the physical parts of Villager play remain close to vanilla. This pack changes the economy rather than dictating whether players build villages or trading halls.
- Wandering Traders are left vanilla. They are rare enough, and small enough in stock, to sit outside the fixed economy.

### Rules the data pack format cannot enforce

Java Edition 26.3 drives trades through the `villager_trade` and `trade_set` registries. Three intended rules have no field behind them, so the pack works around them instead.

**Restocking** cannot be disabled. Because `max_uses` is set high enough that no trade is ever exhausted, restocking has nothing left to restore and is invisible in play.

**The Hero of the Village discount** is a term in the price formula independent of `reputation_discount`, with no data pack control. Since a discount on a fixed-price economy creates profitable loops, the effect is removed from the player and replaced with a direct reward: **4 Emeralds per raid wave cleared**. The reward is deliberately a good chest rather than an income stream.

**Player experience from trading** is likewise not controllable from a data pack, so trades grant experience as they do in vanilla. No trade in this pack is an exact-value round trip, so there is no free experience loop.

## Economic structure

Farmers, Fishermen, and Butchers are buyer professions. They give players Emeralds for goods. The remaining professions are vendors that take Emeralds in exchange for resources or equipment.

No combination of trades and crafting recipes should produce a profitable loop. Every good is either bought or sold, never both, and where a good can be crafted into something the pack buys, the spread is set wide enough to absorb it.

Emerald income should normally require a non-renewable resource or recurring player involvement. Holding an input while AFK does not count as involvement. Farming is a limited exception: selected automated crops and prepared foods still earn Emeralds when the rate is low enough.

The reference rate is:

> 4 Emeralds = 64 Birch Logs = 64 ordinary bulk blocks

Birch Logs are the economy's reference good: they anchor what a stack of ordinary bulk material is worth. Like every other good, Birch carries a normal spread. A Fletcher sells 64 Logs of any type for 4 Emeralds, while a Fisherman buys 64 Birch Logs for 2. Two stacks of Birch therefore buy one stack of another wood type, and returning wood to the Fisherman is always a loss.

Villagers do not buy larger tree types because a tree-capitator data pack makes them too productive. They also do not sell Planks, Stripped Logs, Wood, Hyphae, Bamboo Blocks, or other simple derivatives. Players can make those from the base material.

## Standard resource purchases

Every stackable resource purchase costs 4 Emeralds. The output quantity communicates the resource's value. Quantities use the readable ladder `64, 48, 32, 24, 16, 8, 4, 2, 1`.

| Output for 4 Emeralds | Resources |
| ---: | --- |
| 64 | Logs and Stems, Cobblestone, Cobbled Deepslate, Dirt, Gravel, Granite, Diorite, Andesite, Tuff, Netherrack, Basalt, Blackstone, End Stone |
| 48 | Stone, Deepslate |
| 32 | Smooth Stone, Sand, Red Sand, Clay Blocks, Soul Sand, Soul Soil, Dripstone Blocks, Calcite |
| 24 | Glass, Terracotta, Nether Bricks, Prismarine, Purpur |
| 16 | Glowstone |
| 8 | Obsidian |

Two documented exceptions to the 4-Emerald standard:

- **Emerald Blocks** may replace large stacks of Emeralds for trades that cost more than 64 Emeralds, and only when the price requires it.
- **Ender Pearls** cost 8 Emeralds each. The ladder cannot express a price this high for a single stackable item, and the price is deliberate: a full set of Eyes of Ender costs roughly 96 Emeralds, so buying your way to the End is possible but expensive.

Books, equipment, and Maps keep individual prices because output quantities cannot express their value.

## Buyer professions

### Farmer

Farmers buy selected crops and prepared foods. Cheap automated goods are included at a low rate. Extremely productive goods such as Cocoa Beans are omitted because even one Emerald per stack would overvalue them.

<!-- generated:farmer -->
| Farmer gives | Player gives | Status |
| ---: | ---: | --- |
| 2 Emeralds | 64 Wheat | Proposed rate |
| 2 Emeralds | 64 Carrot | Proposed rate |
| 2 Emeralds | 64 Potato | Proposed rate |
| 2 Emeralds | 64 Beetroot | Proposed rate |
| 2 Emeralds | 32 Nether Wart | Proposed rate |
| 2 Emeralds | 16 Apple | Proposed rate |
| 2 Emeralds | 32 Chorus Fruit | Proposed rate |
| 2 Emeralds | 32 Baked Potato | Proposed rate |
| 2 Emeralds | 16 Pumpkin Pie | Proposed rate |
<!-- /generated:farmer -->

Bread is not included. Cake is not included either: its only non-automatable input is Milk, which has no cooldown and no cost, so any rate that respected the effort involved would have outpaced every other food trade.

### Fisherman

The Fisherman is the general exchange profession. It buys Birch Logs, fish, and mined valuables.

<!-- generated:fisherman -->
| Fisherman gives | Player gives | Status |
| ---: | ---: | --- |
| 2 Emeralds | 64 Birch Logs | Current design |
| 16 Emeralds | 1 Diamond | Current design |
| 32 Emeralds | 1 Ancient Debris | Current design |
| 32 Emeralds | 1 Heart of the Sea | Current design |
| 8 Emeralds | 1 Echo Shard | Current design |
| 4 Emeralds | 32 Raw Copper | Current design |
| 4 Emeralds | 32 Lapis Lazuli | Current design |
| 4 Emeralds | 16 Raw Iron | Current design |
| 4 Emeralds | 8 Raw Gold | Current design |
| 4 Emeralds | 64 Cod | Proposed rate |
| 4 Emeralds | 64 Salmon | Proposed rate |
| 4 Emeralds | 32 Pufferfish | Proposed rate |
| 4 Emeralds | 32 Tropical Fish | Proposed rate |
<!-- /generated:fisherman -->

Mining trades use only forms that automatic farms cannot produce. Raw Copper, Raw Iron, and Raw Gold qualify because no farm yields ore in raw form and no recipe converts a metal back. Lapis Lazuli qualifies because nothing drops it. Coal is excluded because Wither Skeleton farms produce it, Redstone because Witch farms do, and Amethyst because budding blocks do.

Ancient Debris is the only genuinely non-renewable item on the list, and it is priced at two Diamonds in the expectation that players will sell it rather than use it.

### Butcher

The Butcher buys animal products that practical automatic farms cannot produce cheaply. Leather, Porkchops, Chicken, Feathers, and Eggs are excluded as Emerald sources. Cooking earns a modest premium.

<!-- generated:butcher -->
| Butcher gives | Player gives | Status |
| ---: | ---: | --- |
| 2 Emeralds | 8 Beef | Proposed rate |
| 2 Emeralds | 6 Cooked Beef | Proposed rate |
| 2 Emeralds | 8 Mutton | Proposed rate |
| 2 Emeralds | 6 Cooked Mutton | Proposed rate |
| 2 Emeralds | 4 Rabbit | Proposed rate |
| 2 Emeralds | 3 Cooked Rabbit | Proposed rate |
| 2 Emeralds | 8 Rabbit Hide | Proposed rate |
<!-- /generated:butcher -->

## Vendor professions

| Profession | Catalog role |
| --- | --- |
| Fletcher | Raw Logs and Stems, plus ranged equipment |
| Mason | Natural and selected smelted building materials |
| Shepherd | Wool and dyes |
| Leatherworker | Leather and functional leather goods |
| Cleric | Brewing ingredients and Overworld mob drops |
| Cartographer | Maps and navigation items |
| Armorer | Unenchanted Armor |
| Toolsmith | Unenchanted Tools |
| Weaponsmith | Unenchanted Weapons |
| Librarian | Lowest-tier enchanted Books |

Catalogs prefer base materials over simple crafting variants. A processed block receives its own trade only when players commonly need it in bulk and processing it is tedious. Stone, Deepslate, Smooth Stone, Glass, Terracotta, and Nether Bricks are the initial smelting exceptions. Purpur Blocks are an explicit building-material exception.

### Fletcher

Raw Logs and Stems at 64 for 4 Emeralds, plus Arrows at 64 for 4 Emeralds. Arrows are included despite Skeleton farms producing them, because selling them creates no Emeralds and bulk Arrows are exactly the tedious-but-cheap good a vendor exists for.

Bows and Crossbows are priced as equipment. Tipped Arrows are excluded: the Cleric sells ingredients rather than Potions, so a brewing-derived good would have no Potion behind it. Spectral Arrows are excluded because the Mason already sells Glowstone.

### Shepherd

All sixteen colors of Wool and all sixteen Dyes. Carpet, Beds, and Banners are excluded as trivial crafts from Wool.

### Leatherworker

Saddle, Leather Horse Armor, and the four Leather armor pieces, plus raw Leather. Selling Leather creates no Emeralds and the Butcher deliberately does not buy it, so there is no cycle. Leather is genuinely tedious for anyone without a Hoglin farm.

### Cleric

Brewing ingredients that cannot be farmed easily: Blaze Powder, Ghast Tear, Rabbit's Foot, and Phantom Membrane. Fermented Spider Eye, Magma Cream, and Glistering Melon are excluded as one-step crafts from goods the pack already sells. Nether Wart is excluded because the Farmer buys it.

The Cleric also sells Overworld mob drops, which are otherwise the hardest category to obtain without building a farm:

| Output for 4 Emeralds | Drop |
| ---: | --- |
| 64 | String, Rotten Flesh, Feather, Flint |
| 32 | Bone, Gunpowder, Spider Eye, Ink Sac |
| 16 | Slime Ball, Glow Ink Sac |

Ender Pearls are sold at 8 Emeralds each under the exception above.

Rabbit Hide is excluded because the Butcher buys it. Bones are priced at 32 rather than 64 because Bone Meal grows crops the Farmer buys. At this rate the round trip loses heavily, but it is the closest thing in the pack to a cycle and should be rechecked if the Wheat rate ever changes.

The Cleric does not sell Potions. Brewing them from the ingredients above is the intended route.

### Cartographer

Explorer Maps for each structure type at 16 Emeralds each, plus Compass and Spyglass priced as equipment. The Recovery Compass is excluded because the Fisherman buys Echo Shards.

### Armorer, Toolsmith, and Weaponsmith

Finished equipment, always unenchanted, so that Villagers do not bypass Super Awesome Enchanting's catalyst system when both packs are installed.

Prices are derived rather than hand-set: the material cost of the item, resolved through vanilla crafting recipes down to base materials, plus roughly a 25 percent convenience premium, floored at 1 Emerald and rounded up to whole Emeralds. A Bow and a set of Leather armor therefore cost 1 Emerald each, which is honest — they are convenience, not progression.

<!-- generated:equipment -->
| Profession | Item | Price |
| --- | --- | ---: |
| Armorer | Iron Chestplate | 3 Emeralds |
| Armorer | Iron Leggings | 3 Emeralds |
| Armorer | Iron Boots | 2 Emeralds |
| Armorer | Iron Helmet | 2 Emeralds |
| Armorer | Shield | 1 Emerald |
| Cartographer | Compass | 2 Emeralds |
| Cartographer | Spyglass | 1 Emerald |
| Fletcher | Bow | 1 Emerald |
| Fletcher | Crossbow | 1 Emerald |
| Leatherworker | Leather Horse Armor | 8 Emeralds |
| Leatherworker | Saddle | 8 Emeralds |
| Leatherworker | Leather Chestplate | 2 Emeralds |
| Leatherworker | Leather Leggings | 2 Emeralds |
| Leatherworker | Leather Boots | 1 Emerald |
| Leatherworker | Leather Helmet | 1 Emerald |
| Toolsmith | Bucket | 1 Emerald |
| Toolsmith | Flint and Steel | 1 Emerald |
| Toolsmith | Iron Axe | 1 Emerald |
| Toolsmith | Iron Hoe | 1 Emerald |
| Toolsmith | Iron Pickaxe | 1 Emerald |
| Toolsmith | Iron Shovel | 1 Emerald |
| Toolsmith | Shears | 1 Emerald |
| Weaponsmith | Iron Axe | 1 Emerald |
| Weaponsmith | Iron Sword | 1 Emerald |
<!-- /generated:equipment -->

**Equipment stops at Iron.** Diamond gear would be internally consistent at derived prices, but it would also make Emeralds a route past caving and the Nether. The ceiling is one constant and can be raised after playtesting.

### Librarian

Librarians keep enchanted Books as an alternate route into enchanting.

- Every Librarian has the complete deterministic Book catalog from the start.
- Librarians sell the lowest tier of every enchantment except curses.
- Books combine through vanilla Anvil rules, so reaching a high tier requires exponentially more tier-I Books.
- **Multi-tier enchantments cost 8 Emeralds per Book.** Reaching Sharpness V by Anvil takes sixteen Books and 128 Emeralds plus escalating Anvil costs, comfortably worse than catalysts.
- **Single-tier enchantments cost 64 Emeralds per Book.** They incur no combining penalty, so the shelf price is the final price. At 8 Emeralds, Silk Touch and Infinity would cost two stacks of Birch and undercut their catalysts entirely.
- Librarians never sell the Mending Book, in any configuration. See below.

<!-- generated:books -->
The catalog is 40 Books: 34 multi-tier enchantments at 8 Emeralds and 6 single-tier enchantments at 64 Emeralds. Curses and Mending are excluded.
<!-- /generated:books -->

## Relationship to other packs

Super Awesome Villagers works without any other pack in this repository. Its deterministic trade economy does not require Super Awesome Enchanting.

**The Mending Book is never sold.** Super Awesome Enchanting does not delete Mending; it overrides `minecraft:enchantment/mending.json` so that the enchantment ID means Unbreakable. A Book carrying `minecraft:mending` is therefore an Unbreakable Book whenever Enchanting is installed — the most valuable enchantment in the collection, gated there behind a Netherite Ingot catalyst, available here for 64 Emeralds. Trade sets are static JSON with no runtime test for another pack's presence, so the Book cannot be included conditionally. It is omitted outright.

Standalone players are not cut off from Mending: it remains in fishing loot, chest loot, and the vanilla Enchanting Table. There is simply no shop for it.

When both packs are installed, equipment vendors still sell unenchanted gear and Librarians provide low-tier Books as the expensive alternative to catalysts.

## Open design work

- Verify that the vanilla trading interface remains usable when a Librarian exposes roughly fifty offers at once. No engine cap on recipe count is documented and the screen scrolls, but the practical limit is unrecorded. This is tested before any Book pricing work.
- Confirm end to end that a single profession behaves as intended: catalog available at level 1, no exhaustion, no demand or reputation movement, no Hero of the Village discount.
- Playtest the Proposed rates, particularly the Farmer and Butcher, which were rescaled without play data.
- Watch whether farming remains a viable Emerald route now that mining pays substantially better.
- Recheck the Bone and Wheat rates together if either moves.
