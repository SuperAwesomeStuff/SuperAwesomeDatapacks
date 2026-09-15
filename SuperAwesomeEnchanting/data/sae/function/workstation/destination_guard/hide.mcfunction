
execute unless items block ~ ~ ~ container.11 *[minecraft:custom_data~{sae:{destination_guard:true}}] run return 0
item replace block ~ ~ ~ container.11 with air
scoreboard players set modified_slot fancyui.master 11
function fancyui:manual_removal
