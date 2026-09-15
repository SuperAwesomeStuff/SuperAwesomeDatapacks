#
#   Append Background
#
#   Purpose: To append to this container's Items using the slot from storage 'fancyui:data slot.Slot'
#
#   Input: None
#


# say init/slot/append_background


data modify storage fancyui:data old_components set from storage fancyui:data slot.components

# Set static data
data merge storage fancyui:data {slot:\
    {\
        count: 1b,\
        id:"minecraft:gray_stained_glass_pane",\
        components: {\
            "minecraft:tooltip_display": {hide_tooltip:true},\
            "minecraft:max_stack_size": 1,\
            "minecraft:custom_name": {text:" ",italic:false},\
            "minecraft:custom_data": {\
                fancyui: {\
                    origin:[14,79,-6],\
                    Slot:19,\
                    fixed:true\
                }\
            }\
        }\
    }\
}

# Merge in old component data
data modify storage fancyui:data slot.components merge from storage fancyui:data old_components

data modify storage fancyui:data slot.components."minecraft:custom_data".fancyui.test set from storage fancyui:data old_components

# Save the rest of the data
data modify storage fancyui:data slot.components."minecraft:custom_data".fancyui.Slot set from storage fancyui:data slot.Slot
function fancyui:ui/init/slot/save_pos

data modify block ~ ~ ~ Items append from storage fancyui:data slot

data remove storage fancyui:data old_components
