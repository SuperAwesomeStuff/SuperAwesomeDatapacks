#
#   Update item
#
#   Purpose: To modify the executing entity data 'data.watch[{Slot:__}].item'
#
#   Input: { Slot: int, target: string }
#


#$say data modify entity @s data.watch[{Slot:$(Slot)b}].item set from storage fancyui:data $(target)
$data modify entity @s data.watch[{Slot:$(Slot)b}].item set from storage fancyui:data $(target)
