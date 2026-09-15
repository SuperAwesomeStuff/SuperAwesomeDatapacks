#
#   Get Item
#
#   Purpose: To get the item in this marker's slot
#
#   Input: { Slot: int, destination: string }
#


#$say data modify storage fancyui:data $(destination) set from entity @n[type=marker,tag=fancyui.button.container] data.slots[{Slot:$(Slot)b}]
$data modify storage fancyui:data $(destination) set from entity @n[type=marker,tag=fancyui.button.container] data.slots[{Slot:$(Slot)b}]
