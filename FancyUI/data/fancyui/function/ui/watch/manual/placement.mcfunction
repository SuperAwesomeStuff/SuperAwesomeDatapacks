#
#   Placement
#
#   Purpose: To modify any required data due to a manual placement
#
#   Input: None
#


# say watch/manual/placement

# Set the appropriate marker slot data
function fancyui:meta/reset_macro
execute store result storage fancyui:data macro.Slot int 1 run scoreboard players get modified_slot fancyui.master
data modify storage fancyui:data macro.has_item set value "true"
function fancyui:ui/watch/manual/macro/update_has_item with storage fancyui:data macro

# Get the slot item
data modify storage fancyui:data macro.destination set value "placement_item"
function fancyui:ui/watch/macro/get_item with storage fancyui:data macro

# Set the watch value with it
data modify storage fancyui:data target set from storage fancyui:data placement_item
data modify storage fancyui:data macro.target set value "target"
function fancyui:ui/watch/manual/macro/update_item with storage fancyui:data macro
