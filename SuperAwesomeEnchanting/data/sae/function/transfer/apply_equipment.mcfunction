
execute unless data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments" set value {}
data modify block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments" merge from block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"
execute if data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments"."minecraft:mending" run data modify block ~ ~ ~ Items[{Slot:11b}].components."minecraft:damage" set value 0
