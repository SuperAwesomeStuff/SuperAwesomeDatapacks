# Super Awesome Enchanting

Super Awesome Enchanting replaces Minecraft's random Enchanting Table results with a deterministic, resource-based system. Players choose an enchantment, supply its catalyst, and know the result and cost before committing.

**Status:** Playtest-ready for Minecraft Java 26.3. Static validation, dedicated-server tests, and an initial client test pass. Balance and multiplayer behavior still need longer playtesting.

**Target:** Minecraft Java Edition 26.3.

## Goals

- Let players choose enchantments instead of rerolling random offers.
- Allow enchanting as soon as an Enchanting Table becomes available, without a level-30 setup.
- Give gathered resources lasting uses while keeping Minecraft's progression recognizable.
- Reward exploration without making finite structure loot the only source of an enchantment.
- Work on a small multiplayer server even after nearby structures have been looted.

## Catalyst enchanting

Place a piece of equipment or a Book in the Enchanting Table with the catalyst associated with an enchantment. Each operation raises the applicable enchantment by one tier and consumes the catalyst quantity listed in the table below. The XP cost equals the resulting tier: tier I costs one level, tier II costs two levels, and so on.

The target slot accepts exactly one item. Creative players do not pay the XP cost, but the operation still consumes the listed catalyst quantity. Catalyst enchanting never creates or raises an enchantment above its vanilla maximum tier.

There is no level-30 requirement. Lapis and Bookshelves are not part of the new process. The Enchanting Table keeps its vanilla recipe, so Diamonds and Obsidian still determine when enchanting begins.

Existing enchantments do not prevent further catalyst upgrades. Vanilla item restrictions and enchantment incompatibilities still apply. An invalid or conflicting operation returns every supplied item and consumes no XP.

Books accept every catalyst. When one catalyst represents several enchantments, a Book gains or raises every associated enchantment that has not reached its maximum. The operation costs the highest resulting tier among the enchantments that changed. It fails only when none of the associated enchantments can advance.

For equipment, the catalyst catalog must resolve to at most one applicable enchantment for each item. Catalog validation fails if an equipment and catalyst combination becomes ambiguous. Books are the deliberate multi-enchantment exception.

Applying an enchanted Book to equipment follows vanilla compatibility rules. Compatible enchantments transfer, incompatible ones are discarded, and the Book is consumed. Books can still be combined with the usual Anvil rules.

## Catalyst table

The total column shows the material cost of starting without the enchantment and reaching its vanilla maximum tier. These values are part of the current design and will be tested for balance during implementation.

| Enchantment | Max tier | Catalyst per tier | Total to maximum | Reasoning |
| --- | ---: | --- | --- | --- |
| Aqua Affinity | I | 1 Sponge | 1 Sponge | Sponge represents efficient underwater work. Its added recipe prevents finite Monument loot from becoming a requirement. |
| Bane of Arthropods | V | 1 Spider Eye | 5 Spider Eyes | A direct association with Spiders and other arthropods; inexpensive because the enchantment is narrow. |
| Blast Protection | IV | 1 Obsidian | 4 Obsidian | Obsidian is Minecraft's recognizable explosion-resistant block. |
| Breach | IV | 1 Amethyst Block | 4 Amethyst Blocks | Amethyst is a magical weapon material and groups related offensive enchantments on Books. |
| Channeling | I | 1 Lightning Rod | 1 Lightning Rod | A direct association with attracting lightning. |
| Curse of Binding | I | 1 Iron Chain | 1 Iron Chain | Represents an item being physically bound to its wearer. |
| Curse of Vanishing | I | 1 Glass | 1 Glass | Glass is visually present but easy to overlook, fitting disappearance without making a curse expensive. |
| Density | V | 1 Gold Block | 5 Gold Blocks | A heavy compacted metal block communicates additional mass. |
| Depth Strider | III | 1 Nautilus Shell | 3 Nautilus Shells | An aquatic material associated with movement beneath the water. |
| Efficiency | V | 1 Redstone Block | 5 Redstone Blocks | Redstone is associated with automation and faster work. |
| Feather Falling | IV | 1 Slime Block | 4 Slime Blocks | Slime Blocks cushion falls and make the effect easy to remember. |
| Fire Aspect | II | 1 Blaze Rod | 2 Blaze Rods | Blaze Rods are a direct source of Nether fire. |
| Fire Protection | IV | 1 Magma Cream | 4 Magma Cream | Magma Cream is already used to survive fire through Potions. |
| Flame | I | 1 Blaze Rod | 1 Blaze Rod | Shares the fire catalyst with Fire Aspect on a different weapon type. |
| Fortune | III | 1 Diamond Block | 3 Diamond Blocks | A large investment for an enchantment that multiplies valuable mined resources and can eventually repay its cost. |
| Frost Walker | II | 1 Blue Ice | 2 Blue Ice | The catalyst is the solid ice that the enchantment leaves behind. |
| Impaling | V | 1 Prismarine Shard | 5 Prismarine Shards | Ocean Monument material shaped like a small weapon point. |
| Infinity | I | 64 Spectral Arrows | 64 Spectral Arrows | Sacrifices a full stack of special arrows, which Infinity itself cannot replace, for unlimited normal arrows. |
| Knockback | II | 1 Piston | 2 Pistons | Pistons push targets away. |
| Looting | III | 1 Gold Block | 3 Gold Blocks | Gold represents treasure and valuable drops. Its compacted form makes the upgrade meaningful while remaining farmable. |
| Loyalty | III | 1 Ender Pearl | 3 Ender Pearls | Ender Pearls represent an object travelling through space and returning to its user. |
| Luck of the Sea | III | 1 Pufferfish | 3 Pufferfish | A distinctive fishing reward associated with ocean luck. |
| Lunge | III | 1 Breeze Rod | 3 Breeze Rods | Wind propulsion matches the Spear's forward burst. |
| Lure | III | 1 Tropical Fish | 3 Tropical Fish | Fish serve as literal bait for faster fishing. |
| Unbreakable | I | 1 Netherite Ingot | 1 Netherite Ingot | Netherite represents permanent equipment and gives non-Netherite items access to the same defining benefit. |
| Multishot | I | 1 Dispenser | 1 Dispenser | A Dispenser fires projectiles and suggests launching several shots mechanically. |
| Piercing | IV | 1 Amethyst Block | 4 Amethyst Blocks | Shares the magical offensive catalyst family while remaining unambiguous on Crossbows. |
| Power | V | 1 Amethyst Block | 5 Amethyst Blocks | The shared general offensive catalyst for Bows. |
| Projectile Protection | IV | 1 Shield | 4 Shields | A Shield is the clearest item associated with defending against projectiles. |
| Protection | IV | 1 Diamond | 4 Diamonds | Diamonds represent strong general-purpose equipment and make broad protection dearer than narrow defenses. |
| Punch | II | 1 Piston | 2 Pistons | Shares the pushing catalyst with Knockback on a different weapon type. |
| Quick Charge | III | 1 Redstone Block | 3 Redstone Blocks | Redstone represents speeding up a mechanical Crossbow action. |
| Respiration | III | 1 Turtle Scute | 3 Turtle Scutes | Scutes already create the aquatic Turtle Shell helmet. |
| Riptide | III | 1 Nautilus Shell | 3 Nautilus Shells | Shares the aquatic movement catalyst with Depth Strider on a different item type. |
| Sharpness | V | 1 Amethyst Block | 5 Amethyst Blocks | The shared general offensive catalyst for melee weapons. |
| Silk Touch | I | 1 Slime Block | 1 Slime Block | A soft, sticky block suggests lifting fragile blocks intact. |
| Smite | V | 1 Glowstone Block | 5 Glowstone Blocks | Bright Nether light represents destroying undead creatures and avoids a catalyst collision with Density on Maces. |
| Soul Speed | III | 1 Soul Sand | 3 Soul Sand | A direct association with the blocks affected by the enchantment. |
| Sweeping Edge | III | 1 Breeze Rod | 3 Breeze Rods | Wind fits the wide sweep of a Sword attack. |
| Swift Sneak | III | 1 Sculk Sensor | 3 Sculk Sensors | Sculk reacts to movement and sound. Sensors provide a repeatable alternative to Ancient City chest luck. |
| Thorns | III | 1 Pointed Dripstone | 3 Pointed Dripstone | A literal sharp point that damages on contact. |
| Unbreaking | III | 1 Iron Block | 3 Iron Blocks | A substantial supply of durable metal reinforces an item before the permanent Netherite upgrade. |
| Wind Burst | III | 1 Breeze Rod | 3 Breeze Rods | A direct association with Breeze wind attacks and Trial Chambers. |

### Shared catalysts on Books

- An Amethyst Block adds Breach, Piercing, Power, and Sharpness.
- A Blaze Rod adds Fire Aspect and Flame.
- A Breeze Rod adds Lunge, Sweeping Edge, and Wind Burst.
- A Gold Block adds Density and Looting.
- A Nautilus Shell adds Depth Strider and Riptide.
- A Piston adds Knockback and Punch.
- A Redstone Block adds Efficiency and Quick Charge.
- A Slime Block adds Feather Falling and Silk Touch.

Repeating the catalyst raises every associated enchantment that has not reached its maximum. Applying the resulting Book to equipment transfers only the compatible enchantments, but consumes the Book and every unused enchantment on it.

## Enchanting Table interface

The Enchanting Table uses [FancyUI](https://github.com/FancyPotatOS/FancyUI) as a separate datapack dependency. This private repository includes a patched 26.3-compatible copy in the top-level `FancyUI` directory. The placed workstation still looks like an Enchanting Table.

No companion resource pack is planned. The interface uses named vanilla items, concise lore, a custom container title, disabled-state controls, and chat feedback. Color and icon choice are never the only way to understand a control.

The interface has two modes. The selected mode remains active after an operation so players can perform several similar operations in sequence:

- **Enchant:** Insert one piece of equipment or one Book. The right side displays every enchantment supported by that target. Clicking an ordinary Enchanting option applies it immediately, pulling its Catalyst from the clicking player's main inventory or hotbar and charging that player the resulting tier's XP cost.
- **Transfer:** Insert a source and a blank transfer item or Book. A dedicated left-to-right row shows **Source → Transfer item → Result**, previews every transferred enchantment and tier, warns that the source will be destroyed, and shows the five-level cost. Transfer does not require a Catalyst. Taking the Result completes the operation.

Enchant mode places the Target label in the second slot of the top row and its item directly below it. The third column remains an empty spacer before the solid three-by-six Catalyst grid on the right. The bottom-left button always switches modes, while Book pagination sits below the Target column. Every equipment item fits on one page. Books expose one option per distinct Catalyst, including shared Catalysts that raise several enchantments together, and use a single control to switch between two pages. There is no separate category navigation or full Catalyst catalogue.

Enchanting options use their Catalyst as the icon and the resulting enchantment or enchantments as the primary name. Equipment options are sorted alphabetically, with curses always placed after ordinary enchantments. Book options are grouped by Catalyst and use the same curses-last ordering. Each tooltip identifies every resulting tier, the Catalyst cost, and the XP cost. Supported options remain visible when unavailable and state the exact reason, including an incompatible enchantment, maximum tier, missing Catalyst, or insufficient XP. Affordability refreshes while a target remains inserted, and every click revalidates the clicking player's inventory and XP before changing the item.

A successful enchantment leaves the target in place, refreshes its options, and plays an Enchanting Table sound without sending a chat or action-bar message. A short click cooldown prevents an accidental double-click from buying two tiers. Curses instead arm on the first click and require a second click within three seconds; changing inputs, selecting another option, switching modes, or allowing the timer to expire disarms them.

Transfer has a separate left-to-right Source, Transfer item, and Result layout. Each item sits below its label. As in Enchant mode, the bottom-left button switches modes without a separate label. When the inputs are compatible and the viewing player can pay five levels, the Result slot previews the completed item's model, custom name, glint, and full enchantment set. Book results use the enchanted-Book model and stored-enchantment tooltip. Taking the Result charges the clicking player and consumes both inputs. The result moves to that player's cursor; if the cursor becomes occupied during delivery, it drops at the workstation instead. Switching modes preserves the primary item, but a player must remove an inserted Transfer item before returning to Enchant mode. Changing the target or mode resets Book pagination to its first page; completing an enchantment does not.

Before a valid target is inserted, the option area asks for equipment or a Book. Invalid targets receive a specific explanation. A target stack must contain exactly one item. In Enchant mode, the Transfer item slot is covered by a fixed interface element and cannot accept an item; it becomes an input only after switching to Transfer mode.

The Source and Transfer item slots are shared Workstation inputs. Any player may insert or remove an item, switch modes or pages, select an Enchanting option, or take a transfer Result. The player who clicks an operation supplies its Catalyst and XP. There is no ownership lock, snapshot, or escrow. Breaking or destroying the workstation drops the Enchanting Table and every player-supplied item at its location, then removes its supporting entities and interface items. Adjacent Hoppers and Hopper Minecarts remain disabled because they cannot distinguish shared inputs from fixed interface controls.

The interface design remains subject to multiplayer and performance testing on Java Edition 26.3.

## Enchantment transfer

Direct transfers work between items in the same narrow equipment category, regardless of material. Helmet, chestplate, leggings, and boots are four separate categories. Sword, Axe, Pickaxe, Shovel, and Hoe are separate categories. Bows and Crossbows are separate. Spears, Maces, Tridents, Shields, Elytra, Fishing Rods, Shears, Brushes, Flint and Steel, Carrots on Sticks, and Warped Fungi on Sticks each have their own category.

A Book is the deliberate exception. Any item can transfer its enchantments into a blank Book, which can then apply compatible enchantments to a different equipment category through an Anvil. An enchanted Book cannot be a transfer source; applying it remains an Anvil operation.

The destination must be unenchanted, except that Netherite equipment may already have only its automatic Unbreakable enchantment. A custom glint without an enchantment does not make an item enchanted. The destination keeps its name, lore, durability, trim, and other custom data. Its enchantments come from the source, with automatic Unbreakable preserved on Netherite equipment. Every enchantment transfers together, including curses and Unbreakable. The system rejects the operation if the complete resulting enchantment set is not valid on the destination rather than silently discarding part of it. Valid command-created tiers above the vanilla maximum survive transfer, but Catalyst enchanting cannot create or raise them.

## Unbreakable

Unbreakable replaces Mending and prevents all durability loss.

- All Netherite equipment gains Unbreakable automatically.
- Any other damageable item can receive it with one Netherite Ingot.
- An item is fully repaired once when it gains Unbreakable.
- Unbreaking may remain alongside Unbreakable, though its effect is redundant.
- Unbreakable is compatible with Infinity.
- Unbreakable can move through the normal transfer system.
- A Grindstone can remove it from non-Netherite equipment. Netherite equipment regains it automatically.
- Unbreakable never appears in random loot, fishing, mob drops, bartering, or Villager trades.

The intended implementation redefines `minecraft:mending` internally. Existing Mending items and Books then display and behave as Unbreakable without an inventory migration. The pack removes new Mending acquisition from normal sources, including the Mending trade supplied by Super Awesome Villagers when it runs alone.

## Material repairs

A damaged tool can be combined with one of its normal repair materials in a player crafting grid or Crafting Table. The material restores one third of the tool's maximum durability, capped at fully repaired, while preserving enchantments, its name, and its other item data. The recipes follow Minecraft 26.3's `minecraft:repairable` material for Wooden, Stone, Copper, Iron, Golden, Diamond, and Netherite tools, plus the Mace and its Breeze Rod.

## Anvils and Grindstones

Vanilla Anvil operations and Book-combining rules remain. Every enchantment's data-driven `anvil_cost` is reduced to 1, and the pack periodically resets the `minecraft:repair_cost` component on directly held player inventory, hotbar, armor, offhand, and cursor items. It does not recurse into Ender Chests, containers, Bundles, or Shulker Boxes; those items are normalized after they enter a direct player slot. This prevents the prior-work penalty from accumulating without requiring a custom Anvil.

Minecraft's hardcoded "Too Expensive!" threshold still exists. If intrinsic enchantment costs can reach it during testing, the affected costs will be adjusted.

The Grindstone keeps its vanilla role. It removes non-curse enchantments, returns some XP, and never refunds catalysts.

## Found enchanted Books

Catalysts are the reliable enchanting route. Naturally generated enchanted Books are jackpots.

- Books from structure loot, vaults, fishing, Piglin bartering, and similar random sources keep their source's vanilla one-or-several enchantment selection behavior, but every selected enchantment generates at its maximum tier.
- Librarian Books retain their normal tier ranges unless Super Awesome Villagers is also installed.
- Player-created and catalyst-created Books retain their constructed tiers.
- The frequency and number of naturally generated Books remain close to vanilla. A successful find becomes better rather than more common.

Natural Books use these themed pools:

| Source | Themed pool |
| --- | --- |
| Abandoned Mineshaft | Efficiency, Fortune, Silk Touch, Unbreaking, Feather Falling |
| Ancient City | Efficiency, Silk Touch, Protection, Projectile Protection, Feather Falling, Respiration, Unbreaking, Thorns |
| Bastion and Piglin bartering | Soul Speed only, as a signature enchantment |
| Desert Pyramid | Blast Protection, Fire Protection, Thorns, Unbreaking |
| Jungle Temple | Bane of Arthropods, Infinity, Punch, Projectile Protection, Unbreaking |
| Pillager Outpost | Multishot, Piercing, Quick Charge, Projectile Protection, Unbreaking |
| Dungeon | Sharpness, Smite, Bane of Arthropods, Protection, Unbreaking |
| Stronghold Corridor | Protection, Projectile Protection, Sharpness, Efficiency, Fortune, Unbreaking |
| Stronghold Crossing | Protection, Projectile Protection, Sharpness, Efficiency, Fortune, Unbreaking, Feather Falling, Looting |
| Stronghold Library | Every general non-curse enchantment except Unbreakable and the three signature enchantments |
| Big Underwater Ruin | Aqua Affinity, Respiration, Depth Strider, Luck of the Sea, Lure |
| Woodland Mansion | Protection, Projectile Protection, Thorns, Sharpness, Smite, Bane of Arthropods, Looting, Unbreaking |
| Fishing treasure | Luck of the Sea, Lure, Unbreaking, Respiration, Frost Walker |
| Normal Vault combat and tool Book | Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, Feather Falling |
| Normal Vault aquatic Book | Riptide, Loyalty, Channeling, Impaling, Aqua Affinity |
| Ominous Vault combat Book | Knockback, Punch, Smite, Looting, Multishot |
| Ominous Vault Mace Book | Breach, Density |

Signature rewards retain separate loot rolls so themed Books do not dilute them. Swift Sneak from Ancient Cities, Wind Burst from Ominous Vaults, and Soul Speed from Bastions or bartering generate at their maximum tiers. Curse Books are not added to natural loot.

The optional vanilla Trade Rebalance experiment is not supported because it directly adds Mending through loot and Villager offers that bypass this pack's normal acquisition controls.

## Sponge recipe

Sponge becomes renewable enough that Aqua Affinity does not depend on finite Sponge rooms. The shapeless recipe crafts one Sponge from:

- 2 Prismarine Crystals
- 2 Kelp

Ocean Monuments remain the efficient source of bulk Sponge.

## Installation and removal

Newly player-placed Enchanting Tables become workstations automatically. Tables that existed before the pack was installed, or were placed by commands or world generation, must be broken and placed again. The pack does not scan unloaded chunks for legacy tables.

To turn a workstation back into an ordinary decorative Enchanting Table, stand within six blocks of it and run `/trigger sae.vanilla`. The command converts the nearest workstation. Any supplied enchanting or transfer items drop safely at the table, and the workstation is removed from the pack's registry.

Copy both of these directories into the world's `datapacks` directory before the world starts:

- `SuperAwesomeEnchanting`
- `FancyUI`

The upstream checkout contains optional `FancyUIResourcePack` directories, but they are not part of the playtest build. This compatibility pack uses vanilla item models, so no resource pack is required. If FancyUI is missing or incompatible, Super Awesome Enchanting reports the dependency error and refuses to convert newly placed Enchanting Tables.

When upgrading from the earlier build that embedded FancyUI as `sae_ui`, run `/function sae:uninstall` while that old build is still loaded. Stop the server, replace the pack, add the separate FancyUI dependency, then restart. Break and replace each restored Enchanting Table to create the new workstation. This prevents old `sae_ui` marker entities from surviving the upgrade.

Before removing the pack, join as an administrator and run `/function sae:uninstall`. The function force-loads registered workstation chunks long enough to restore ordinary Enchanting Tables, preserves chunks that were already force-loaded, drops supplied items at their Workstations, and removes supporting entities. Remove the data pack files only after the function reports completion. Removing the files without running the function is not guaranteed to be safe.

The generated pack is reproducible:

```powershell
python tools/generate_enchanting_pack.py
python tools/validate_enchanting_pack.py
```

The optional `tools/test_enchanting_server.py` smoke suite uses the ignored disposable server under `.cache/minecraft/26.3/integration-server`. It requires the server EULA to have been accepted explicitly. The script installs both datapacks into its test world. It verifies pack loading, UI text and tooltip data, watched-slot acceptance, equipment enchanting, shared-catalyst Books, transfer into Netherite, material repair durability, Unbreakable maintenance, nearby workstation conversion, themed loot execution, and registry-based uninstall restoration.

## Open design work

- Test the container-backed workstation for safety, responsiveness, and multiplayer behavior on Java Edition 26.3.
- Confirm that lowering every enchantment's `anvil_cost` to 1 keeps all legal combinations below the hardcoded Anvil limit.
- Playtest catalyst costs, transfer costs, and loot rewards.

## Sources and inspiration

- [Minecraft Java Edition 26.3](https://www.minecraft.net/en-us/article/minecraft-java-edition-26-3)
- [Minecraft FancyUI Datapack](https://github.com/FancyPotatOS/FancyUI)
- [Data-driven enchantment definitions introduced in Snapshot 24w18a](https://feedback.minecraft.net/hc/en-us/articles/27439564545677-Minecraft-Java-Edition-Snapshot-24w18a)
- [Minecraft Anvil overview](https://www.minecraft.net/en-us/article/taking-inventory--anvil)
