# Super Awesome Enchanting

Super Awesome Enchanting replaces Minecraft's random Enchanting Table results with a deterministic, resource-based system. Players choose an enchantment, supply its catalyst, and know the result and cost before committing.

**Status:** In design. There is no playable release yet.

**Target:** Minecraft Java Edition 26.3.

## Goals

- Let players choose enchantments instead of rerolling random offers.
- Allow enchanting as soon as an Enchanting Table becomes available, without a level-30 setup.
- Give gathered resources lasting uses while keeping Minecraft's progression recognizable.
- Reward exploration without making finite structure loot the only source of an enchantment.
- Work on a small multiplayer server even after nearby structures have been looted.

## Catalyst enchanting

Place a piece of equipment or a Book in the Enchanting Table with the catalyst associated with an enchantment. Each operation raises the applicable enchantment by one tier and consumes the catalyst quantity listed in the table below. The XP cost equals the resulting tier: tier I costs one level, tier II costs two levels, and so on.

There is no level-30 requirement. Lapis and Bookshelves are not part of the new process. The Enchanting Table keeps its vanilla recipe, so Diamonds and Obsidian still determine when enchanting begins.

Existing enchantments do not prevent further catalyst upgrades. Vanilla item restrictions and enchantment incompatibilities still apply. An invalid or conflicting operation returns every supplied item and consumes no XP.

Books accept every catalyst. When one catalyst represents several enchantments, a Book gains or raises every associated enchantment that has not reached its maximum. The operation costs the highest resulting tier among the enchantments that changed. It fails only when none of the associated enchantments can advance.

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
| Curse of Binding | I | 1 Chain | 1 Chain | Represents an item being physically bound to its wearer. |
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

The Enchanting Table will use a container-backed interface adapted from [FancyUI](https://github.com/FancyPotatOS/FancyUI). The needed framework code will live inside this pack so players do not need a second data pack. The placed workstation will still look like an Enchanting Table.

The companion resource pack will improve the interface, but the underlying interaction and information must remain usable without it.

The interface has two modes:

- **Enchant:** Insert equipment or a Book and a catalyst. The interface previews the exact enchantments, resulting tiers, catalyst cost, and XP cost before confirmation.
- **Transfer:** Insert a source item, a blank destination item or Book, and one Amethyst Block. The interface previews every enchantment that will move and warns that the source will be destroyed. A transfer costs five levels.

A reference view shows all catalyst recipes from the start. Its tabs are Armor, Melee, Ranged, Tools, Movement and water, and Curses. Inserting an item filters the list to compatible enchantments.

Only one player can use a workstation at a time. Breaking or destroying it returns the Enchanting Table and every player-supplied item, then removes its supporting entities and interface items.

The interface design remains subject to multiplayer and performance testing on Java Edition 26.3.

## Enchantment transfer

Direct transfers work between items in the same narrow equipment category, regardless of material. An Iron Pickaxe can transfer to a Diamond Pickaxe, but a Pickaxe cannot transfer directly to a Sword. Bows and Crossbows are separate categories. Tridents, Shields, Elytra, Maces, Fishing Rods, and other unusual equipment each have their own category.

A Book is the deliberate exception. Any item can transfer its enchantments into a blank Book, which can then apply compatible enchantments to a different equipment category through an Anvil.

The destination must be unenchanted. It keeps its name, lore, durability, trim, and other custom data. Its enchantments come from the source. Every enchantment transfers together, including curses and Unbreakable. The system rejects the operation if the complete enchantment set is not valid on the destination rather than silently discarding part of it.

## Unbreakable

Unbreakable replaces Mending and prevents all durability loss.

- All Netherite equipment gains Unbreakable automatically.
- Any other damageable item can receive it with one Netherite Ingot.
- Gaining Unbreakable removes Unbreaking.
- Unbreakable can move through the normal transfer system.
- A Grindstone can remove it from non-Netherite equipment. Netherite equipment regains it automatically.
- Unbreakable never appears in random loot, fishing, mob drops, bartering, or Villager trades.

The intended implementation redefines `minecraft:mending` internally. Existing Mending items and Books then display and behave as Unbreakable without an inventory migration. The pack removes new Mending acquisition from normal sources, including the Mending trade supplied by Super Awesome Villagers when it runs alone.

## Anvils and Grindstones

Vanilla Anvil operations and Book-combining rules remain. Every enchantment's data-driven `anvil_cost` is reduced to 1, and the pack periodically resets the `minecraft:repair_cost` component on items in player inventories. This prevents the prior-work penalty from accumulating without requiring a custom Anvil.

Minecraft's hardcoded "Too Expensive!" threshold still exists. If intrinsic enchantment costs can reach it during testing, the affected costs will be adjusted.

The Grindstone keeps its vanilla role. It removes non-curse enchantments, returns some XP, and never refunds catalysts.

## Found enchanted Books

Catalysts are the reliable enchanting route. Naturally generated enchanted Books are jackpots.

- Books from structure loot, vaults, fishing, mob drops, Piglin bartering, and similar random sources generate at the selected enchantment's maximum tier.
- Librarian Books retain their normal tier ranges unless Super Awesome Villagers is also installed.
- Player-created and catalyst-created Books retain their constructed tiers.
- The frequency and number of naturally generated Books remain close to vanilla. A successful find becomes better rather than more common.

Structure loot uses small themed enchantment pools. Minor structures should usually have three to five choices, while major structures may have up to eight. Stronghold Libraries may draw from the full non-curse pool.

Signature rewards retain separate loot rolls so themed Books do not dilute them. Swift Sneak from Ancient Cities, Wind Burst from Ominous Vaults, and Soul Speed from Bastions or bartering generate at their maximum tiers. Dangerous magical structures may have a separate low-chance curse roll. A curse never replaces the ordinary Book reward.

## Sponge recipe

Sponge becomes renewable enough that Aqua Affinity does not depend on finite Sponge rooms. The shapeless recipe uses:

- 2 Prismarine Crystals
- 2 Kelp

Ocean Monuments remain the efficient source of bulk Sponge.

## Open design work

- Assign the exact themed enchantment pool for each structure.
- Test the container-backed workstation for safety, responsiveness, and multiplayer behavior on Java Edition 26.3.
- Confirm that lowering every enchantment's `anvil_cost` to 1 keeps all legal combinations below the hardcoded Anvil limit.
- Playtest catalyst costs, transfer costs, and loot rewards.

## Sources and inspiration

- [Minecraft 26.3 Release Candidate 2](https://www.minecraft.net/en-us/article/minecraft-26-3-release-candidate-2)
- [Minecraft FancyUI Datapack](https://github.com/FancyPotatOS/FancyUI)
- [Data-driven enchantment definitions introduced in Snapshot 24w18a](https://feedback.minecraft.net/hc/en-us/articles/27439564545677-Minecraft-Java-Edition-Snapshot-24w18a)
- [Minecraft Anvil overview](https://www.minecraft.net/en-us/article/taking-inventory--anvil)
