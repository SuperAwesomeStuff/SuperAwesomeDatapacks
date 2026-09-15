data modify block ~ ~ ~ Items[{Slot:20b}].components."minecraft:item_model" set value "minecraft:gray_stained_glass_pane"
data modify block ~ ~ ~ Items[{Slot:20b}].components."minecraft:custom_name" set value {text:" ",italic:false}
data remove block ~ ~ ~ Items[{Slot:20b}].components."minecraft:lore"
data modify block ~ ~ ~ Items[{Slot:20b}].components."minecraft:custom_data".sae set value {action:"empty"}
