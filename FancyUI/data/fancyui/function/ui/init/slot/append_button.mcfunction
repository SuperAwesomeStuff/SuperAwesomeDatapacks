#
#   Append Button
#
#   Purpose: To append to this container's Items using the slot from storage 'fancyui:data slot.Slot'
#
#   Input: None
#


# say init/slot/append_button

# Save the provided data
data modify storage fancyui:data old_slot set from storage fancyui:data slot

# Set some static data
data merge storage fancyui:data {slot:\
    {\
        count: 1b,\
        id:"minecraft:stone_button",\
        components: {\
            "minecraft:max_stack_size": 1,\
            "minecraft:custom_data": {\
                fancyui: {\
                    origin: [14,79,-6],\
                    Slot: 19,\
                    fixed: true,\
                    button: true\
                }\
            }\
        }\
    }\
}

# Save the rest of the data
data modify storage fancyui:data slot.components."minecraft:custom_data".fancyui.Slot set from storage fancyui:data slot.Slot
function fancyui:ui/init/slot/save_pos

# Merge in provided data
data modify storage fancyui:data slot merge from storage fancyui:data old_slot

# Add to the container
data modify block ~ ~ ~ Items append from storage fancyui:data slot
