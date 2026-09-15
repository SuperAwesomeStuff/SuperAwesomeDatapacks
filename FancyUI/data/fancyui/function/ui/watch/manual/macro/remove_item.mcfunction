#
#   Remove Item
#
#   Purpose: To remove the watch slot's item data
#
#   Input: { Slot: int }
#


# $say data remove entity @s data.watch[{Slot:$(Slot)b}].item
$data remove entity @s data.watch[{Slot:$(Slot)b}].item
