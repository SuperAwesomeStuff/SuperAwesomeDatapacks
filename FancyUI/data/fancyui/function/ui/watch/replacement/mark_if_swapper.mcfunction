#
#   Mark If Swapper
#
#   Purpose: To tag this player as the swapper if they have the matching item
#
#   Input: None
#


# say watch/replace/mark_if_swapper

summon minecraft:armor_stand ~ ~ ~ {equipment:{},Tags:["fancyui.swap.armor_stand"]}


# Try to replace the cursor item and if it fails, I am the swapper
item replace entity @n[tag=fancyui.swap.armor_stand] weapon.mainhand from entity @s player.cursor
data modify storage fancyui:data old_item set from entity @n[tag=fancyui.swap.armor_stand] equipment.mainhand
execute store result score swap.test.success fancyui.master run data modify storage fancyui:data old_item set from storage fancyui:data item

execute if score swap.test.success fancyui.master matches 1 run tag @s add fancyui.watch.swapper

# Clean up
scoreboard players reset swap.test.success fancyui.master
data remove entity @n[tag=fancyui.swap.armor_stand] equipment
kill @n[tag=fancyui.swap.armor_stand]
