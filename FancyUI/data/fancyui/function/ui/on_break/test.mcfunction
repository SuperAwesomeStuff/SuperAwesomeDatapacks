#
#   Test On Break
#
#   Purpose: To run a function if the block is broken
#
#   Input: None
#


# say on_break/test

function fancyui:meta/reset_macro
data modify storage fancyui:data macro.block set from entity @s data.container
function fancyui:ui/on_break/macro/test_block with storage fancyui:data macro

execute unless score test_block.matches fancyui.master matches 1 run function fancyui:ui/on_break/activate
