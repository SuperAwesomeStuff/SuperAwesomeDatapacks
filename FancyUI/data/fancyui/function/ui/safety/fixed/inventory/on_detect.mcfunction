#
#   On Detect
#
#   Purpose: To test when a player picks up a fixed item in their inventory
#
#   Input: None
#


# say safety/fixed/inventory/on_detect

tag @s add fancyui.cursor.instigator

function fancyui:ui/safety/fixed/inventory/replace_fixed

tag @s remove fancyui.cursor.instigator

clear @s *[custom_data~{fancyui:{fixed:true}}]
