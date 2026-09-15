#
#   Update
#
#   Purpose: To update this marker's watch slots
#
#   Input: None
#


# Cycle the watch
data modify entity @s data.watch append from entity @s data.watch[0]
data remove entity @s data.watch[0]

# Stop when hit flag
execute if data entity @s data.watch[0].stop run return 0

data modify storage fancyui:data watch_slot set from entity @s data.watch[0]
function fancyui:ui/watch/update_slot

function fancyui:ui/watch/update_rec
