#
#   Callback
#
#   Purpose: To run the item callback logic from the slot in storage 'fancyui:data button.callback'
#
#   Input: None
#

# say button/callback

# Clean old callback data
data remove storage fancyui:data callback_data

# Save new data if exists
data modify storage fancyui:data callback_data set from storage fancyui:data slot_item.callback.data

# Set the callback macro and call it
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.function set from storage fancyui:data slot_item.callback.function
function fancyui:ui/button/macro/call_function with storage fancyui:data macro

execute unless score successful_call fancyui.master matches -2147483648..2147483647 run function fancyui:ui/button/callback_failed
