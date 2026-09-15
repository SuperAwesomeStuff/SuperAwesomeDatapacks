#
#   Replace fixed
#
#   Purpose: To extract the fixed inventory item and start the replacement process
#
#   Input: None
#


# say safety/fixed/inventory/replace_fixed

summon minecraft:armor_stand ~ ~ ~ {equipment:{},Tags:["fancyui.fixed.armor_stand"]}

data modify entity @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] equipment.mainhand set from entity @s Inventory[{components:{"minecraft:custom_data":{fancyui:{fixed:true}}}}]

execute as @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] run function fancyui:ui/safety/fixed/set_as_fixed

data remove entity @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand] equipment
kill @n[type=minecraft:armor_stand,tag=fancyui.fixed.armor_stand]
