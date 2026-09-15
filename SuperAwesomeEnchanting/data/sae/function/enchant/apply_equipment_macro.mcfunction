
execute unless data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments" set value {}
$data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."$(enchantment)" set value $(next)
