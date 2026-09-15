
data modify block ~ ~ ~ Items[{Slot:0b}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{Slot:0b}].components."minecraft:custom_name" set value {text:" ",italic:false}
data remove block ~ ~ ~ Items[{Slot:0b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:1b}].components."minecraft:item_model" set value "minecraft:enchanting_table"
data modify block ~ ~ ~ Items[{Slot:1b}].components."minecraft:custom_name" set value {text:"Target",color:"white",italic:false}
function sae:workstation/destination_guard/show
function sae:workstation/options/clear_transfer_chrome
function sae:workstation/options/clear_page_control
function sae:workstation/options/clear_transfer_control
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:item_model" set value "minecraft:amethyst_shard"
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:custom_name" set value {text:"Switch to Transfer",color:"white",italic:false}
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:lore" set value [{text:"Move all enchantments to a compatible item",color:"gray",italic:false}]
data modify block ~ ~ ~ Items[{Slot:18b}].components."minecraft:custom_data".sae set value {action:"mode_toggle"}
