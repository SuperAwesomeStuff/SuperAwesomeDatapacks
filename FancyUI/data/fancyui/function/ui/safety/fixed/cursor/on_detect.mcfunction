#
#   On Detect
#
#   Purpose: To test when a player picks up a fixed item in their cursor
#
#   Input: None
#


# say safety/fixed/cursor/on_detect

tag @s add fancyui.cursor.instigator

execute if items entity @s player.cursor *[custom_data~{fancyui:{button:true}}] run function fancyui:ui/button/on_click

function fancyui:ui/safety/fixed/cursor/replace_fixed

item replace entity @s player.cursor with minecraft:air

tag @s remove fancyui.cursor.instigator
