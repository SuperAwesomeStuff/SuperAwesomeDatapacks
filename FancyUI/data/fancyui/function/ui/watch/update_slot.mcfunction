#
#   Update Slot
#
#   Purpose: To update the slot in storage 'fancyui:data watch_slot'
#
#   Input: None
#


# say watch/update_slot

# Reset then retrieve the item in that current slot
data remove storage fancyui:data item
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.Slot set from storage fancyui:data watch_slot.Slot
data modify storage fancyui:data macro.destination set value "item"
function fancyui:ui/watch/macro/get_item with storage fancyui:data macro

# If no item but had an item, run removal callback logic
execute unless data storage fancyui:data item if data storage fancyui:data watch_slot{has_item:true} run return run function fancyui:ui/watch/removal

# If there is an item an didn't have one, run placement logic
execute if data storage fancyui:data item if data storage fancyui:data watch_slot{has_item:false} run return run function fancyui:ui/watch/placement

# If the item has been replaced
execute if data storage fancyui:data item run function fancyui:ui/watch/replacement/test
