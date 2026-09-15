#
#   Spawn Item
#
#   Purpose: To turn the item in this container at the specified slot into an item entity
#
#   Input: { Slot: int }
#


summon item ~ ~.5 ~ {Tags:["fancyui.spawned_item"],Age:0,Item:{id:"minecraft:dirt",count:1}}

# Set the spawned item to the container item
#$say data modify entity @n[type=item,tag=fancyui.spawned_item] Item set from block ~ ~ ~ Items[{Slot:$(Slot)b}]
$data modify entity @n[type=item,tag=fancyui.spawned_item] Item set from block ~ ~ ~ Items[{Slot:$(Slot)b}]

# Clear the slot
#$say data remove block ~ ~ ~ Items[{Slot:$(Slot)b}]
$data remove block ~ ~ ~ Items[{Slot:$(Slot)b}]

tag @n[type=item,tag=fancyui.spawned_item] remove fancyui.spawned_item
