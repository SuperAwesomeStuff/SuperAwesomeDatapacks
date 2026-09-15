#
#   Save Position
#
#   Purpose: To set the storage 'fancyui:data slot.components."minecraft:custom_data".fancyui.origin' to this entity's pos scoreboard value
#
#   Input: None
#


# say init/slot/append_item

execute store result storage fancyui:data slot.components."minecraft:custom_data".fancyui.origin[0] int 1 run scoreboard players get @s fancyui.pos.x
execute store result storage fancyui:data slot.components."minecraft:custom_data".fancyui.origin[1] int 1 run scoreboard players get @s fancyui.pos.y
execute store result storage fancyui:data slot.components."minecraft:custom_data".fancyui.origin[2] int 1 run scoreboard players get @s fancyui.pos.z
