
data modify storage sae:runtime macro.enchantment set from entity @s data.sae.enchantment
data modify storage sae:runtime macro.next set from entity @s data.sae.next
function sae:enchant/apply_equipment_macro with storage sae:runtime macro
execute if data entity @s {data:{sae:{enchantment:"minecraft:mending"}}} run data modify block ~ ~ ~ Items[{Slot:10b}].components."minecraft:damage" set value 0
