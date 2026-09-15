#
#   Test
#
#   Purpose: To test if the slot has been replaced
#
#   Input: None
#


# say watch/replacement/test

# Set a comparison storage
data modify storage fancyui:data comparison set from storage fancyui:data watch_slot.item

# Get the slot item
data modify storage fancyui:data macro.destination set value "slot_item"
data modify storage fancyui:data macro.Slot set from storage fancyui:data watch_slot.Slot
function fancyui:ui/watch/macro/get_item with storage fancyui:data macro

# execute if data storage fancyui:data macro{Slot:15b} run tellraw @a {"nbt":"slot_item","storage":"fancyui:data"}

# Store success whether if the item has been replaced
scoreboard players reset replacement.test.success fancyui.master
execute store success score replacement.test.success fancyui.master run data modify storage fancyui:data comparison set from storage fancyui:data slot_item

# It was, so the item changed
execute if score replacement.test.success fancyui.master matches 1 run function fancyui:ui/watch/replacement/replacement
