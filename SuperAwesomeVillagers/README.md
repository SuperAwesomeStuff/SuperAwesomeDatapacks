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
- Every trade is written in lowest terms: 1 Emerald for 16 Cobblestone, not 4 for 64.
- Offers appear in a fixed order. Items come before blocks, and each group runs from cheapest to most expensive. Armorers, Toolsmiths, and Weaponsmiths list their one-off items first, then equipment by tier: Copper, Iron, Gold, Diamond.
- Professions, workstations, breeding, and the physical parts of Villager play remain close to vanilla. This pack changes the economy rather than dictating whether players build villages or trading halls.
- Wandering Traders get a fixed catalog too. See [Wandering Trader](#wandering-trader).

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

> 1 Emerald = 16 Birch Logs = 16 ordinary bulk blocks

Birch Logs are the economy's reference good: they anchor what ordinary bulk material is worth. Like every other good, Birch carries a normal spread. A Fletcher sells 16 Logs of any type for 1 Emerald, while a Fisherman buys 32 Birch Logs for 1. Two Birch Logs therefore buy one Log of another wood type, and returning wood to the Fisherman is always a loss.

Villagers do not buy larger tree types because a tree-capitator data pack makes them too productive. They also do not sell Planks, Stripped Logs, Wood, Hyphae, Bamboo Blocks, or other simple derivatives. Players can make those from the base material.

## Standard resource purchases

Every stackable resource purchase costs 1 Emerald. The output quantity communicates the resource's value. Quantities use the readable ladder `16, 8, 4, 2, 1`.

| Output for 1 Emerald | Resources |
| ---: | --- |
| 16 | Logs and Stems, Cobblestone, Cobbled Deepslate, Stone, Deepslate, Dirt, Gravel, Granite, Diorite, Andesite, Tuff, Netherrack, Basalt, Blackstone, End Stone |
| 8 | Smooth Stone, Sand, Red Sand, Clay Blocks, Soul Sand, Soul Soil, Dripstone Blocks, Calcite, Glass, Terracotta, Nether Bricks, Prismarine, Purpur, Bricks, Quartz Blocks, Resin Bricks, Ice |
| 4 | Glowstone |
| 2 | Obsidian |

Two documented exceptions to the 1-Emerald standard:

- **Emerald Blocks** replace Emeralds for trades that cost more than 64 Emeralds, since one trade slot holds one stack. The price rounds up to whole Blocks. No current trade reaches this.
- **Ender Pearls** cost 8 Emeralds each. The ladder cannot express a price this high for a single stackable item, and the price is deliberate: a full set of Eyes of Ender costs roughly 96 Emeralds, so buying your way to the End is possible but expensive.

Books, equipment, and Maps keep individual prices because output quantities cannot express their value.

## Buyer professions

### Farmer

Farmers buy selected crops and prepared foods. Cheap automated goods are included at a low rate. Extremely productive goods such as Cocoa Beans are omitted because even one Emerald per stack would overvalue them.

<!-- generated:farmer -->
| Farmer gives | Player gives | Status |
| ---: | ---: | --- |
| 1 Emerald | 16 Carrot | Proposed rate |
| 1 Emerald | 16 Potato | Proposed rate |
| 1 Emerald | 16 Nether Wart | Proposed rate |
| 1 Emerald | 16 Chorus Fruit | Proposed rate |
| 1 Emerald | 8 Beetroot | Proposed rate |
| 1 Emerald | 8 Apple | Proposed rate |
| 1 Emerald | 8 Pumpkin Pie | Proposed rate |
| 1 Emerald | 2 Torchflowers | Proposed rate |
| 1 Emerald | 2 Pitcher Plants | Proposed rate |
<!-- /generated:farmer -->

**Farmers do not buy crops that villagers harvested.** When a Farmer villager breaks a Carrot, Potato, or Beetroot crop, the drop becomes "Haram Carrot" (or Potato, or Beetroot) with uncommon rarity, which shows as a yellow name. The Farmer only accepts the common kind, so villager-run crop farms earn no Emeralds. Villagers still pick up, share, and breed with marked crops as normal. Crops broken by players, water, or pistons are not marked. Marked and unmarked crops do not stack.

Wheat and Baked Potatoes are not bought, because a Hay Bale or a furnace would turn marked crops into unmarked goods.

Torchflowers and Pitcher Plants grow from Sniffer seeds. A harvested plant returns no seed, so each one sold costs a Sniffer dig, and the rate is high to match.

Bread is not included. Cake is not included either: its only non-automatable input is Milk, which has no cooldown and no cost, so any rate that respected the effort involved would have outpaced every other food trade.

### Fisherman

The Fisherman is the general exchange profession. It buys Birch Logs, fish, mined valuables, and boss and treasure rewards.

<!-- generated:fisherman -->
| Fisherman gives | Player gives | Status |
| ---: | ---: | --- |
| 1 Emerald | 16 Cod | Proposed rate |
| 1 Emerald | 16 Salmon | Proposed rate |
| 1 Emerald | 8 Raw Copper | Current design |
| 1 Emerald | 8 Lapis Lazuli | Current design |
| 1 Emerald | 8 Quartz | Proposed rate |
| 1 Emerald | 8 Pufferfish | Proposed rate |
| 1 Emerald | 8 Tropical Fish | Proposed rate |
| 1 Emerald | 4 Raw Iron | Current design |
| 1 Emerald | 2 Raw Gold | Current design |
| 4 Emeralds | 1 Diamond | Proposed rate |
| 8 Emeralds | 1 Echo Shard | Current design |
| 32 Emeralds | 1 Netherite Scrap | Current design |
| 32 Emeralds | 1 Heart of the Sea | Current design |
| 64 Emeralds | 1 Enchanted Golden Apple | Proposed rate |
| 64 Emeralds | 1 Nether Star | Proposed rate |
| 1 Emerald | 32 Birch Logs | Current design |
| 64 Emeralds | 1 Dragon Egg | Proposed rate |
<!-- /generated:fisherman -->

Mining trades use only forms that automatic farms cannot produce. Raw Copper, Raw Iron, and Raw Gold qualify because no farm yields ore in raw form and no recipe converts a metal back. Lapis Lazuli qualifies because nothing drops it. Nether Quartz is mined, and Piglin bartering yields too little of it to farm. Coal is excluded because Wither Skeleton farms produce it, Redstone because Witch farms do, and Amethyst because budding blocks do.

Netherite Scrap is the only genuinely non-renewable mined good on the list. Each Ancient Debris smelts into one Scrap, so the rate matches the old Debris trade: at 32 Emeralds it is worth eight Diamonds, in the expectation that players will sell it rather than use it.

Enchanted Golden Apples come only from loot. Each Nether Star costs a Wither fight. The Dragon Egg exists once per world, so its trade pays once.

### Butcher

The Butcher buys animal products that practical automatic farms cannot produce cheaply. Leather, Porkchops, Chicken, Feathers, and Eggs are excluded as Emerald sources. Cooking earns a modest premium.

<!-- generated:butcher -->
| Butcher gives | Player gives | Status |
| ---: | ---: | --- |
| 1 Emerald | 4 Beef | Proposed rate |
| 1 Emerald | 4 Mutton | Proposed rate |
| 1 Emerald | 4 Rabbit Hide | Proposed rate |
| 1 Emerald | 3 Cooked Beef | Proposed rate |
| 1 Emerald | 3 Cooked Mutton | Proposed rate |
| 1 Emerald | 2 Rabbit | Proposed rate |
| 2 Emeralds | 3 Cooked Rabbit | Proposed rate |
<!-- /generated:butcher -->

## Vendor professions

| Profession | Catalog role |
| --- | --- |
| Fletcher | Raw Logs and Stems, plus ranged equipment |
| Mason | Natural and selected smelted building materials, plus Ice |
| Shepherd | Wool and dyes |
| Leatherworker | Leather and functional leather goods |
| Cleric | Brewing ingredients, Overworld mob drops, Redstone components, and Sculk |
| Cartographer | Maps and navigation items |
| Armorer | Unenchanted Armor |
| Toolsmith | Unenchanted Tools |
| Weaponsmith | Unenchanted Weapons |
| Librarian | Lowest-tier enchanted Books |

Catalogs prefer base materials over simple crafting variants. A processed block receives its own trade only when players commonly need it in bulk and processing it is tedious. Stone, Deepslate, Smooth Stone, Glass, Terracotta, Nether Bricks, and Bricks are the smelting exceptions. Purpur, Quartz Blocks, and Resin Bricks are explicit building-material exceptions. Quartz Blocks are purely decorative, so they are priced generously: 8 for 1 Emerald, below the Quartz inside them. No recipe turns a Quartz Block back into Quartz, so this creates no loop through the Fisherman. Resin Bricks share the decorative rate. Ice is sold because collecting it in bulk needs Silk Touch.

### Fletcher

Raw Logs and Stems at 16 for 1 Emerald, plus Arrows at 16 for 1 Emerald. Arrows are included despite Skeleton farms producing them, because selling them creates no Emeralds and bulk Arrows are exactly the tedious-but-cheap good a vendor exists for.

Bows and Crossbows are priced as equipment. Tipped Arrows are excluded: the Cleric sells ingredients rather than Potions, so a brewing-derived good would have no Potion behind it. Spectral Arrows are excluded because the Mason already sells Glowstone.

### Shepherd

All sixteen colors of Wool and all sixteen Dyes. Carpet, Beds, and Banners are excluded as trivial crafts from Wool.

### Leatherworker

Saddle, Leather Horse Armor, and the four Leather armor pieces, plus raw Leather. Selling Leather creates no Emeralds and the Butcher deliberately does not buy it, so there is no cycle. Leather is genuinely tedious for anyone without a Hoglin farm.

### Cleric

Brewing ingredients that cannot be farmed easily: Blaze Powder, Ghast Tear, Rabbit's Foot, and Phantom Membrane. Fermented Spider Eye, Magma Cream, and Glistering Melon are excluded as one-step crafts from goods the pack already sells. Nether Wart is excluded because the Farmer buys it.

The Cleric also sells Overworld mob drops, which are otherwise the hardest category to obtain without building a farm, plus Redstone components and Sculk.

Redstone components are priced from their recipes like equipment. Anything worth less than an Emerald is sold in bulk: the largest ladder quantity that 1 Emerald still covers. Redstone Dust sits on the ladder at 16. Sculk Sensors, Shriekers, and Catalysts have no recipe and are hand-priced. Calibrated Sculk Sensors are derived and include the Echo Shard at the Fisherman's rate.

Ender Pearls are sold at 8 Emeralds each under the exception above.

<!-- generated:cleric -->
| Price | Player gets |
| ---: | ---: |
| 1 Emerald | 16 String |
| 1 Emerald | 16 Rotten Flesh |
| 1 Emerald | 16 Feather |
| 1 Emerald | 16 Flint |
| 1 Emerald | 16 Redstone |
| 1 Emerald | 8 Gunpowder |
| 1 Emerald | 8 Spider Eye |
| 1 Emerald | 8 Ink Sac |
| 1 Emerald | 4 Bone |
| 1 Emerald | 4 Slime Ball |
| 1 Emerald | 4 Glow Ink Sac |
| 1 Emerald | 4 Blaze Powder |
| 1 Emerald | 2 Rabbit's Foot |
| 1 Emerald | 2 Phantom Membrane |
| 1 Emerald | 1 Ghast Tear |
| 2 Emeralds | 1 Minecart |
| 8 Emeralds | 1 Ender Pearl |
| 1 Emerald | 16 Sculk Vein |
| 1 Emerald | 8 Sculk |
| 1 Emerald | 8 Redstone Torch |
| 1 Emerald | 8 Lever |
| 1 Emerald | 8 Stone Button |
| 1 Emerald | 8 Rail |
| 1 Emerald | 4 Stone Pressure Plate |
| 1 Emerald | 4 Tripwire Hook |
| 1 Emerald | 4 Note Block |
| 1 Emerald | 2 Repeater |
| 1 Emerald | 2 Trapped Chest |
| 1 Emerald | 2 Lightning Rod |
| 1 Emerald | 2 Detector Rail |
| 1 Emerald | 2 Activator Rail |
| 1 Emerald | 1 Redstone Block |
| 1 Emerald | 1 Comparator |
| 1 Emerald | 1 Observer |
| 1 Emerald | 1 Piston |
| 1 Emerald | 1 Dispenser |
| 1 Emerald | 1 Dropper |
| 1 Emerald | 1 Heavy Weighted Pressure Plate |
| 1 Emerald | 1 Daylight Detector |
| 1 Emerald | 1 Target |
| 1 Emerald | 1 Redstone Lamp |
| 1 Emerald | 1 Powered Rail |
| 2 Emeralds | 1 Sculk Sensor |
| 2 Emeralds | 1 Sticky Piston |
| 2 Emeralds | 1 Hopper |
| 2 Emeralds | 1 Light Weighted Pressure Plate |
| 2 Emeralds | 1 Copper Bulb |
| 2 Emeralds | 1 TNT |
| 3 Emeralds | 1 Slime Block |
| 3 Emeralds | 1 Crafter |
| 3 Emeralds | 1 Calibrated Sculk Sensor |
| 4 Emeralds | 1 Sculk Shrieker |
| 8 Emeralds | 1 Sculk Catalyst |
<!-- /generated:cleric -->

Rabbit Hide is excluded because the Butcher buys it. Bones are priced at 4 rather than 16 because Bone Meal grows crops the Farmer buys. One Emerald of Bones makes 12 Bone Meal, which grows about 9 spare Carrots or Potatoes (16 sell for an Emerald) or about 3 Beetroot (8 sell for an Emerald), so the round trip loses. It is the closest thing in the pack to a cycle and should be rechecked if the crop rates ever change.

The Cleric does not sell Potions. Brewing them from the ingredients above is the intended route.

### Cartographer

Explorer Maps for each structure type at 16 Emeralds each, plus Compass and Spyglass priced as equipment. The Recovery Compass is excluded because the Fisherman buys Echo Shards.

### Armorer, Toolsmith, and Weaponsmith

Finished equipment, always unenchanted, so that Villagers do not bypass Super Awesome Enchanting's catalyst system when both packs are installed.

Prices are derived rather than hand-set: the material cost of the item, resolved through vanilla crafting recipes down to base materials, plus roughly a 25 percent convenience premium, floored at 1 Emerald and rounded up to whole Emeralds. A Bow and a set of Leather armor therefore cost 1 Emerald each, which is honest — they are convenience, not progression.

<!-- generated:equipment -->
| Profession | Item | Price |
| --- | --- | ---: |
| Armorer | Shield | 1 Emerald |
| Armorer | Copper Helmet | 1 Emerald |
| Armorer | Copper Chestplate | 2 Emeralds |
| Armorer | Copper Leggings | 2 Emeralds |
| Armorer | Copper Boots | 1 Emerald |
| Armorer | Iron Helmet | 2 Emeralds |
| Armorer | Iron Chestplate | 3 Emeralds |
| Armorer | Iron Leggings | 3 Emeralds |
| Armorer | Iron Boots | 2 Emeralds |
| Armorer | Golden Helmet | 4 Emeralds |
| Armorer | Golden Chestplate | 5 Emeralds |
| Armorer | Golden Leggings | 5 Emeralds |
| Armorer | Golden Boots | 3 Emeralds |
| Armorer | Diamond Helmet | 25 Emeralds |
| Armorer | Diamond Chestplate | 40 Emeralds |
| Armorer | Diamond Leggings | 35 Emeralds |
| Armorer | Diamond Boots | 20 Emeralds |
| Cartographer | Spyglass | 1 Emerald |
| Cartographer | Compass | 2 Emeralds |
| Fletcher | Bow | 1 Emerald |
| Fletcher | Crossbow | 1 Emerald |
| Leatherworker | Leather Helmet | 1 Emerald |
| Leatherworker | Leather Boots | 1 Emerald |
| Leatherworker | Leather Chestplate | 2 Emeralds |
| Leatherworker | Leather Leggings | 2 Emeralds |
| Leatherworker | Saddle | 8 Emeralds |
| Leatherworker | Leather Horse Armor | 8 Emeralds |
| Toolsmith | Shears | 1 Emerald |
| Toolsmith | Flint and Steel | 1 Emerald |
| Toolsmith | Bucket | 1 Emerald |
| Toolsmith | Copper Pickaxe | 1 Emerald |
| Toolsmith | Copper Axe | 1 Emerald |
| Toolsmith | Copper Shovel | 1 Emerald |
| Toolsmith | Copper Hoe | 1 Emerald |
| Toolsmith | Iron Pickaxe | 1 Emerald |
| Toolsmith | Iron Axe | 1 Emerald |
| Toolsmith | Iron Shovel | 1 Emerald |
| Toolsmith | Iron Hoe | 1 Emerald |
| Toolsmith | Golden Pickaxe | 2 Emeralds |
| Toolsmith | Golden Axe | 2 Emeralds |
| Toolsmith | Golden Shovel | 1 Emerald |
| Toolsmith | Golden Hoe | 2 Emeralds |
| Toolsmith | Diamond Pickaxe | 16 Emeralds |
| Toolsmith | Diamond Axe | 16 Emeralds |
| Toolsmith | Diamond Shovel | 6 Emeralds |
| Toolsmith | Diamond Hoe | 11 Emeralds |
| Weaponsmith | Copper Sword | 1 Emerald |
| Weaponsmith | Copper Axe | 1 Emerald |
| Weaponsmith | Iron Sword | 1 Emerald |
| Weaponsmith | Iron Axe | 1 Emerald |
| Weaponsmith | Golden Sword | 2 Emeralds |
| Weaponsmith | Golden Axe | 2 Emeralds |
| Weaponsmith | Diamond Sword | 11 Emeralds |
| Weaponsmith | Diamond Axe | 16 Emeralds |
<!-- /generated:equipment -->

**Equipment runs from Copper to Diamond.** Each smith sells Copper, Iron, Gold, and Diamond versions of its gear at derived prices. Diamond gear makes Emeralds a route past caving, so its prices should be watched in playtesting. Netherite is not sold.

### Librarian

Librarians keep enchanted Books as an alternate route into enchanting.

- Every Librarian has the complete deterministic Book catalog from the start.
- Librarians sell the lowest tier of every enchantment except curses.
- Books combine through vanilla Anvil rules, so reaching a high tier requires exponentially more tier-I Books.
- **A Book costs what one tier costs in Super Awesome Enchanting:** the Emerald value of its catalyst plus the 25 percent premium, rounded up. Prices read from the Enchanting pack's catalyst table, so the two packs cannot drift apart. Catalysts no Villager trades have hand-set values in the generator. A Book I matches a catalyst tier, while combining Books up to a high tier stays the dearer route.
- Librarians never sell the Mending Book, in any configuration. See below.

<!-- generated:books -->
| Book | Catalyst per tier | Price |
| --- | --- | ---: |
| Bane of Arthropods I | 1 Spider Eye | 1 Emerald |
| Blast Protection I | 1 Obsidian | 1 Emerald |
| Breach I | 1 Amethyst Block | 1 Emerald |
| Channeling I | 1 Lightning Rod | 1 Emerald |
| Efficiency I | 1 Redstone Block | 1 Emerald |
| Fire Aspect I | 1 Blaze Rod | 1 Emerald |
| Fire Protection I | 1 Magma Cream | 1 Emerald |
| Flame I | 1 Blaze Rod | 1 Emerald |
| Impaling I | 1 Prismarine Shard | 1 Emerald |
| Knockback I | 1 Piston | 1 Emerald |
| Luck of the Sea I | 1 Pufferfish | 1 Emerald |
| Lure I | 1 Tropical Fish | 1 Emerald |
| Multishot I | 1 Dispenser | 1 Emerald |
| Piercing I | 1 Amethyst Block | 1 Emerald |
| Power I | 1 Amethyst Block | 1 Emerald |
| Projectile Protection I | 1 Shield | 1 Emerald |
| Punch I | 1 Piston | 1 Emerald |
| Quick Charge I | 1 Redstone Block | 1 Emerald |
| Sharpness I | 1 Amethyst Block | 1 Emerald |
| Smite I | 1 Glowstone | 1 Emerald |
| Soul Speed I | 1 Soul Sand | 1 Emerald |
| Thorns I | 1 Pointed Dripstone | 1 Emerald |
| Frost Walker I | 1 Blue Ice | 2 Emeralds |
| Lunge I | 1 Breeze Rod | 2 Emeralds |
| Sweeping Edge I | 1 Breeze Rod | 2 Emeralds |
| Wind Burst I | 1 Breeze Rod | 2 Emeralds |
| Aqua Affinity I | 1 Sponge | 3 Emeralds |
| Depth Strider I | 1 Nautilus Shell | 3 Emeralds |
| Feather Falling I | 1 Slime Block | 3 Emeralds |
| Respiration I | 1 Turtle Scute | 3 Emeralds |
| Riptide I | 1 Nautilus Shell | 3 Emeralds |
| Silk Touch I | 1 Slime Block | 3 Emeralds |
| Swift Sneak I | 1 Sculk Sensor | 3 Emeralds |
| Unbreaking I | 1 Iron Block | 3 Emeralds |
| Protection I | 1 Diamond | 5 Emeralds |
| Density I | 1 Gold Block | 6 Emeralds |
| Looting I | 1 Gold Block | 6 Emeralds |
| Loyalty I | 1 Ender Pearl | 10 Emeralds |
| Infinity I | 64 Spectral Arrow | 12 Emeralds |
| Fortune I | 1 Diamond Block | 45 Emeralds |
<!-- /generated:books -->

## Wandering Trader

The Wandering Trader keeps vanilla's catalog and prices, reduced to lowest terms, with three changes:

- Every remaining trade is offered at once, in the same fixed order as Villager catalogs, with unlimited uses.
- Anything a Villager already buys or sells is removed. The generator works this out from the Villager catalogs, so the two stay in step. That drops Logs, Dyes, Sand, Red Sand, Glowstone, Gunpowder, Slime Balls, and the enchanted Iron Pickaxe.
- Its buying trades are removed. Water and Milk Buckets refill for free, and the other buying trades pay more than their ingredients cost or undercut the Farmer, so each was an Emerald loop.

The Long Invisibility Potion stays. It is the only Potion for sale anywhere, and the trader's rarity keeps it from replacing brewing.

<!-- generated:wandering_trader -->
| Price | Player gets |
| ---: | ---: |
| 1 Emerald | 1 Beetroot Seeds |
| 1 Emerald | 1 Melon Seeds |
| 1 Emerald | 1 Name Tag |
| 1 Emerald | 1 Pumpkin Seeds |
| 1 Emerald | 1 Wheat Seeds |
| 3 Emeralds | 1 Tropical Fish Bucket |
| 3 Emeralds | 1 Pufferfish Bucket |
| 5 Emeralds | 1 Potion |
| 5 Emeralds | 1 Nautilus Shell |
| 1 Emerald | 5 Lily Pad |
| 1 Emerald | 3 Brown Mushroom |
| 1 Emerald | 3 Pale Hanging Moss |
| 1 Emerald | 3 Red Mushroom |
| 1 Emerald | 3 Shelf Mushroom |
| 1 Emerald | 3 Vine |
| 1 Emerald | 2 Moss Block |
| 1 Emerald | 2 Pale Moss Block |
| 1 Emerald | 2 Pointed Dripstone |
| 1 Emerald | 2 Rooted Dirt |
| 1 Emerald | 2 Small Dripleaf |
| 1 Emerald | 2 Sulfur Spike |
| 1 Emerald | 1 Allium |
| 1 Emerald | 1 Azure Bluet |
| 1 Emerald | 1 Blue Orchid |
| 1 Emerald | 1 Cornflower |
| 1 Emerald | 1 Dandelion |
| 1 Emerald | 1 Tall Dry Grass |
| 1 Emerald | 1 Fern |
| 1 Emerald | 1 Lily of the Valley |
| 1 Emerald | 1 Open Eyeblossom |
| 1 Emerald | 1 Orange Tulip |
| 1 Emerald | 1 Oxeye Daisy |
| 1 Emerald | 1 Packed Ice |
| 1 Emerald | 1 Pink Tulip |
| 1 Emerald | 1 Podzol |
| 1 Emerald | 1 Poppy |
| 1 Emerald | 1 Pumpkin |
| 1 Emerald | 1 Red Tulip |
| 1 Emerald | 1 Sugar Cane |
| 1 Emerald | 1 White Tulip |
| 1 Emerald | 1 Wildflowers |
| 2 Emeralds | 1 Golden Dandelion |
| 2 Emeralds | 1 Sea Pickle |
| 3 Emeralds | 1 Brain Coral Block |
| 3 Emeralds | 1 Bubble Coral Block |
| 3 Emeralds | 1 Cactus |
| 3 Emeralds | 1 Fire Coral Block |
| 3 Emeralds | 1 Firefly Bush |
| 3 Emeralds | 1 Horn Coral Block |
| 3 Emeralds | 1 Kelp |
| 3 Emeralds | 1 Tube Coral Block |
| 5 Emeralds | 1 Acacia Sapling |
| 5 Emeralds | 1 Birch Sapling |
| 5 Emeralds | 1 Cherry Sapling |
| 5 Emeralds | 1 Dark Oak Sapling |
| 5 Emeralds | 1 Jungle Sapling |
| 5 Emeralds | 1 Mangrove Propagule |
| 5 Emeralds | 1 Oak Sapling |
| 5 Emeralds | 1 Pale Oak Sapling |
| 5 Emeralds | 1 Poplar Sapling |
| 5 Emeralds | 1 Spruce Sapling |
| 6 Emeralds | 1 Blue Ice |
<!-- /generated:wandering_trader -->

## Relationship to other packs

Super Awesome Villagers works without any other pack in this repository. Its deterministic trade economy does not require Super Awesome Enchanting.

**The Mending Book is never sold.** Super Awesome Enchanting does not delete Mending; it overrides `minecraft:enchantment/mending.json` so that the enchantment ID means Unbreakable. A Book carrying `minecraft:mending` is therefore an Unbreakable Book whenever Enchanting is installed — the most valuable enchantment in the collection, gated there behind a Netherite Ingot catalyst. Trade sets are static JSON with no runtime test for another pack's presence, so the Book cannot be included conditionally. It is omitted outright.

Standalone players are not cut off from Mending: it remains in fishing loot, chest loot, and the vanilla Enchanting Table. There is simply no shop for it.

When both packs are installed, equipment vendors still sell unenchanted gear and Librarians provide low-tier Books as the expensive alternative to catalysts.

## Open design work

- Verify that the vanilla trading interface remains usable with roughly fifty offers at once. The Cleric now has 53. No engine cap on recipe count is documented and the screen scrolls, but the practical limit is unrecorded. This is tested before any Book pricing work.
- Confirm end to end that a single profession behaves as intended: catalog available at level 1, no exhaustion, no demand or reputation movement, no Hero of the Village discount.
- Playtest the Proposed rates, particularly the Farmer and Butcher, which were rescaled without play data.
- Watch whether farming remains a viable Emerald route now that mining pays substantially better.
- Recheck the Bone and crop rates together if either moves.
- Confirm in play that a Farmer's harvest marks its drops, and that the trade screen rejects marked crops. The server test only checks the loot table.
