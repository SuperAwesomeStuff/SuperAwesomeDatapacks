data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:item_model" set from block ~ ~ ~ Items[{Slot:11b}].id
execute if items block ~ ~ ~ container.11 minecraft:book run data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:item_model" set value "minecraft:enchanted_book"
execute if data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:item_model" run data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:item_model" set from block ~ ~ ~ Items[{Slot:11b}].components."minecraft:item_model"
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:custom_name" set value {text:"Transfer result",color:"aqua",italic:false}
execute if data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:custom_name" run data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:custom_name" set from block ~ ~ ~ Items[{Slot:11b}].components."minecraft:custom_name"
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:lore" set value []
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantments" set from block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"
execute if data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments" run data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantments" merge from block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantments"
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantment_glint_override" set value true
execute if data block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantment_glint_override" run data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:enchantment_glint_override" set from block ~ ~ ~ Items[{Slot:11b}].components."minecraft:enchantment_glint_override"
execute if items block ~ ~ ~ container.11 minecraft:book run function sae:transfer/render_preview_book
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:custom_data".sae set value {action:"transfer_take"}
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:lore" append value {text:"Source will be destroyed",color:"red",italic:false}
data modify block ~ ~ ~ Items[{Slot:13b}].components."minecraft:lore" append value {text:"Cost: 5 levels",color:"gray",italic:false}
