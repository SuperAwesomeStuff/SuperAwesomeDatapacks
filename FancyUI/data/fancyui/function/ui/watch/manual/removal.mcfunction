#
#   Placement
#
#   Purpose: To modify any required data due to a manual placement
#
#   Input: None
#


# say watch/manual/removal

function fancyui:meta/reset_macro
execute store result storage fancyui:data macro.Slot int 1 run scoreboard players get modified_slot fancyui.master
data modify storage fancyui:data macro.has_item set value "false"

function fancyui:ui/watch/manual/macro/update_has_item with storage fancyui:data macro
function fancyui:ui/watch/manual/macro/remove_item with storage fancyui:data macro
