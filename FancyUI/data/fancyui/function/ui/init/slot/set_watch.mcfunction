#
#   Set Watch
#
#   Purpose: To set a reminder on the marker to watch this slot
#
#   Input: None
#


# say init/slot/set_watch

# Ensure there is a loop stop point
execute unless data entity @s data.watch[0] run data modify entity @s data.watch set value [{stop:true}]

tag @s add fancyui.container.watch

data modify entity @s data.watch append value {Slot:0b,has_item:false}

data modify entity @s data.watch[-1].Slot set from storage fancyui:data slot.Slot

# Save the watch-specific values if set
execute if data storage fancyui:data slot.criteria run data modify entity @s data.watch[-1].criteria set from storage fancyui:data slot.criteria
execute if data storage fancyui:data slot.callback run data modify entity @s data.watch[-1].callback set from storage fancyui:data slot.callback
execute if data storage fancyui:data slot.removal_callback run data modify entity @s data.watch[-1].removal_callback set from storage fancyui:data slot.removal_callback
