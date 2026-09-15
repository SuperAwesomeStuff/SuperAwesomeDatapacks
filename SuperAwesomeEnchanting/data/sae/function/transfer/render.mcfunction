
function sae:workstation/destination_guard/hide
data modify block ~ ~ ~ Items[{Slot:0b}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{Slot:0b}].components."minecraft:custom_name" set value {text:" ",italic:false}
data remove block ~ ~ ~ Items[{Slot:0b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:1b}].components."minecraft:item_model" set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{Slot:1b}].components."minecraft:custom_name" set value {text:"Source",color:"white",italic:false}
data remove block ~ ~ ~ Items[{Slot:1b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:2b}].components."minecraft:item_model" set value "minecraft:chest"
data modify block ~ ~ ~ Items[{Slot:2b}].components."minecraft:custom_name" set value {text:"Transfer item",color:"white",italic:false}
data remove block ~ ~ ~ Items[{Slot:2b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:4b}].components."minecraft:item_model" set value "minecraft:enchanted_book"
data modify block ~ ~ ~ Items[{Slot:4b}].components."minecraft:custom_name" set value {text:"Result",color:"white",italic:false}
data remove block ~ ~ ~ Items[{Slot:4b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:9b}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{Slot:9b}].components."minecraft:custom_name" set value {text:" ",italic:false}
data remove block ~ ~ ~ Items[{Slot:9b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:12b}].components."minecraft:item_model" set value "minecraft:arrow"
data modify block ~ ~ ~ Items[{Slot:12b}].components."minecraft:custom_name" set value {text:"Creates",color:"gray",italic:false}
data remove block ~ ~ ~ Items[{Slot:12b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:item_model" set value "minecraft:enchanting_table"
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:custom_name" set value {text:"Switch to Enchant",color:"white",italic:false}
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:lore" set value [{text:"Return to item-first enchanting",color:"gray",italic:false}]
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:custom_data".sae set value {action:"mode_toggle"}
execute if data block ~ ~ ~ Items[{Slot:11b}] run data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:item_model" set value "minecraft:barrier"
execute if data block ~ ~ ~ Items[{Slot:11b}] run data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:lore" set value [{text:"Remove the destination before switching",color:"red",italic:false}]
function sae:workstation/options/clear_page_control
function sae:workstation/options/clear_transfer_control
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:custom_name" set value {text:"Awaiting valid inputs",color:"dark_gray",italic:false}
data remove block ~ ~ ~ Items[{Slot:13b}].components."minecraft:lore"
data remove block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantments"
data remove block ~ ~ ~ Items[{Slot:13b}].components."minecraft:stored_enchantments"
data remove block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantment_glint_override"
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:custom_data".sae set value {action:"empty"}
function sae:transfer/preview
execute if score #valid sae.tmp matches 1 if data block ~ ~ ~ Items[{Slot:10b}] if data block ~ ~ ~ Items[{Slot:11b}] run function sae:transfer/render_preview
execute unless score #valid sae.tmp matches 1 run function sae:transfer/control/reason
