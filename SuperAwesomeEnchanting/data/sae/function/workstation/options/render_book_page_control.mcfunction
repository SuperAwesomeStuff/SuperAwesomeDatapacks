
data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:item_model" set value "minecraft:arrow"
data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_data".sae set value {action:"page_toggle"}
execute if data entity @s {data:{sae:{page:0}}} run data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_name" set value {text:"Next — Page 1/2",color:"white",italic:false}
execute if data entity @s {data:{sae:{page:1}}} run data modify block ~ ~ ~ Items[{Slot:19b}].components."minecraft:custom_name" set value {text:"Previous — Page 2/2",color:"white",italic:false}
