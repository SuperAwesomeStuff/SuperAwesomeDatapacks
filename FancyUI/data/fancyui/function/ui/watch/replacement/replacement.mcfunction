#
#   Replacement
#
#   Purpose: To run the item replacement logic
#
#   Input: None
#


# say watch/replace/replacement

# Item: storage fancyui:data item
# Watch Slot: storage fancyui:data watch_slot

function fancyui:ui/watch/replacement/find_swapper

# Save the new item into the watch slot
data modify storage fancyui:data macro.target set value "item"
function fancyui:ui/watch/manual/macro/update_item with storage fancyui:data macro
data modify storage fancyui:data watch_slot.item set from storage fancyui:data item

scoreboard players set swapped fancyui.master 1

# say @p[tag=fancyui.watch.swapper]

function fancyui:ui/watch/removal
function fancyui:ui/watch/placement

scoreboard players reset swapped fancyui.master
tag @a[tag=fancyui.watch.swapper] remove fancyui.watch.swapper
