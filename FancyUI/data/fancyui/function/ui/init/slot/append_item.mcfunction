#
#   Append Item
#
#   Purpose: To append to this container's Items using the slot from storage 'fancyui:data slot.Slot'
#
#   Input: None
#


# say init/slot/append_item

# Save pos if specified
execute if data storage fancyui:data slot{save_pos: true} run function fancyui:ui/init/slot/save_pos

data modify block ~ ~ ~ Items append from storage fancyui:data slot
