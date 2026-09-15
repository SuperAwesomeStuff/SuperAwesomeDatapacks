#
#   Activate
#
#   Purpose: To run the callback function when the block is broken
#
#   Input: None
#


# say on_break/activate

# Run the callback function
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.function set from entity @s data.on_break
function fancyui:ui/watch/macro/call_function with storage fancyui:data macro

# Test if callback failed
execute unless score successful_call fancyui.master matches -2147483648..2147483647 run function fancyui:ui/watch/callback_failed
