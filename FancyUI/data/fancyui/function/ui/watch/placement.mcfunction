#
#   Placement
#
#   Purpose: To run the item placement logic from the slot in storage 'fancyui:data watch_slot'
#
#   Input: None
#


# say watch/placement

function fancyui:meta/reset_macro
data modify storage fancyui:data macro set from storage fancyui:data watch_slot
function fancyui:ui/watch/macro/check_item_type with storage fancyui:data macro

execute unless entity @s[tag=fancyui.watch.correct_item] run return run function fancyui:ui/watch/reject_item
tag @s remove fancyui.watch.correct_item

# Save that an item is there now
data modify entity @s data.watch[0].has_item set value true
data modify entity @s data.watch[0].item set from storage fancyui:data item

#tellraw @p {"nbt":"data.watch[0]","entity":"@s"}
#tellraw @p {"nbt":"watch_slot","storage":"fancyui:data"}

# Run the callback logic if there is one
execute if data storage fancyui:data watch_slot.callback run function fancyui:ui/watch/callback
