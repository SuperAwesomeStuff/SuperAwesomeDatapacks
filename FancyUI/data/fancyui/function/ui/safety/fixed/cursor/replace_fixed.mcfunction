#
#   Replace fixed
#
#   Purpose: To extract the cursor item and start the replacement process
#
#   Input: None
#


# say safety/fixed/cursor/replace_fixed

summon minecraft:armor_stand ~ ~ ~ {equipment:{},Tags:["fancyui.fixed.armor_stand"]}

item replace entity @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] weapon.mainhand from entity @s player.cursor
item replace entity @s player.cursor with minecraft:air

execute as @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] run function fancyui:ui/safety/fixed/set_as_fixed

data remove entity @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] equipment.mainhand
kill @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand]
