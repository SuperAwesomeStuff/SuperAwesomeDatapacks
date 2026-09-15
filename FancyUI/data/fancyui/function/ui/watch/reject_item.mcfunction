#
#   Reject Item
#
#   Purpose: To run item rejection logic for the slot in storage 'fancyui:data watch_slot'
#
#   Input: None
#


# say watch/reject_item

data modify entity @s data.watch[0].has_item set value false

function fancyui:meta/reset_macro
data modify storage fancyui:data macro set from storage fancyui:data watch_slot
function fancyui:ui/watch/macro/spawn_item with storage fancyui:data macro
