#
#   Slot 37
#
#   Purpose: To set this container's slot 37 to some data specified
#
#   Input: None
#


data remove storage fancyui:data slot
data modify storage fancyui:data slot set from entity @s data.slots[{Slot:37b}]

function fancyui:ui/init/slot/specific/slot_type_setup
