#
#   Save Exact Item
#
#   Purpose: To save the armor stand's mainhand item's exact designated position's current item in the 'fancyui.fixed.target' marker's container to its owner, or a temporary item
#
#   Input: None
#


# say safety/fixed/save_overwriting_item

# Save whether there is an instigator
execute unless items entity @n[tag=fancyui.cursor.instigator] player.cursor * run tag @s add fancyui.fixed.set_overwrite_to_cursor

function fancyui:ui/safety/fixed/saving/slot/find

execute if entity @s[tag=fancyui.fixed.summon_slot_item] at @n[tag=fancyui.fixed.armor_stand] run function fancyui:ui/safety/fixed/saving/summon_item
tag @s remove fancyui.fixed.set_overwrite_to_cursor
