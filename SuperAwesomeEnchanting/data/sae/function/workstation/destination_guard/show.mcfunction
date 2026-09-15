
execute if items block ~ ~ ~ container.11 *[minecraft:custom_data~{sae:{destination_guard:true}}] run return 0
execute if data block ~ ~ ~ Items[{Slot:11b}] run return 0
item replace block ~ ~ ~ container.11 from block ~ ~ ~ container.0
data modify block ~ ~ ~ Items[{Slot:11b}].components."minecraft:custom_data".fancyui.Slot set value 11b
data modify block ~ ~ ~ Items[{Slot:11b}].components."minecraft:custom_data".sae set value {destination_guard:true}
scoreboard players set modified_slot fancyui.master 11
function fancyui:manual_placement
