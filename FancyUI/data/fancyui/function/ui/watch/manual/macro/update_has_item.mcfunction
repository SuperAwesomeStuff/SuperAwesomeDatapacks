#
#   Update has_item
#
#   Purpose: To modify the executing entity data 'data.watch[{Slot:__}].has_item'
#
#   Input: { Slot: int, has_item: bool }
#


#$say data modify entity @s data.watch[{Slot:$(Slot)b}].has_item set value $(has_item)
$data modify entity @s data.watch[{Slot:$(Slot)b}].has_item set value $(has_item)
