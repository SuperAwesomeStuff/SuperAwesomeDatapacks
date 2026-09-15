#
#   Slot 23
#
#   Purpose: To set this container's slot 23 to some data specified
#
#   Input: None
#


data remove storage fancyui:data slot
data modify storage fancyui:data slot set from entity @s data.slots[{Slot:23b}]

function fancyui:ui/init/slot/specific/slot_type_setup
