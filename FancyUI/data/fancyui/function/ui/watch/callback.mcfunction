#
#   Callback
#
#   Purpose: To run the item callback logic from the slot in storage 'fancyui:data watch_slot'
#
#   Input: None
#


# say watch/callback

# Clean old callback data
data remove storage fancyui:data callback_data

# Save new data if exists
data modify storage fancyui:data callback_data set from storage fancyui:data watch_slot.callback.data

# Set the callback macro and call it
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.function set from storage fancyui:data watch_slot.callback.function
function fancyui:ui/watch/macro/call_function with storage fancyui:data macro

execute unless score successful_call fancyui.master matches -2147483648..2147483647 run function fancyui:ui/watch/callback_failed
