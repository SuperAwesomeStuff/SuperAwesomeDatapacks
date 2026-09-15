
scoreboard players set successful_call fancyui.master 0
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_toggle"} run function sae:workstation/mode_toggle
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"page_toggle"} run function sae:workstation/page_toggle
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"enchant_option"} run function sae:workstation/select_option
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"transfer_take"} run function sae:workstation/transfer_take
function sae:workstation/render
