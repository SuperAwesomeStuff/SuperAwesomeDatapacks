#
#   Get Item
#
#   Purpose: To get the item in this container's slot
#
#   Input: { Slot: int, destination: string }
#


# $say data modify storage fancyui:data $(destination) set from block ~ ~ ~ Items[{Slot:$(Slot)b}]
$data modify storage fancyui:data $(destination) set from block ~ ~ ~ Items[{Slot:$(Slot)b}]
