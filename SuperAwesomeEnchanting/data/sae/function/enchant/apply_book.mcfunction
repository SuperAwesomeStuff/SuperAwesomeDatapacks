
data modify block ~ ~ ~ Items[{Slot:10b}].id set value "minecraft:enchanted_book"
execute unless data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" set value {}
data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments" merge from entity @s data.sae.pending
execute if data entity @s data.sae.pending."minecraft:mending" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:damage" set value 0
