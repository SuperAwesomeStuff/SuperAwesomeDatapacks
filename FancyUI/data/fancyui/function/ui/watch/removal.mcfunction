#
#   Removal
#
#   Purpose: To run the item removal logic from the slot in storage 'fancyui:data watch_slot'
#
#   Input: None
#


# say watch/removal

# Clean old callback data
data remove storage fancyui:data callback_data

# Save that the item is no longer there
data modify entity @s data.watch[0].has_item set value false
data remove entity @s data.watch[0].item

execute unless data storage fancyui:data watch_slot.removal_callback run return 0

# Save new data if exists
data modify storage fancyui:data callback_data set from storage fancyui:data watch_slot.removal_callback.data

# Set the callback macro and call it
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.function set from storage fancyui:data watch_slot.removal_callback.function
function fancyui:ui/watch/macro/call_function with storage fancyui:data macro

execute unless score successful_call fancyui.master matches -2147483648..2147483647 run function fancyui:ui/watch/callback_failed
