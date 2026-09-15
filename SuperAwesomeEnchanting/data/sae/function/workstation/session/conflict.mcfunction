
execute if data storage fancyui:data callback_data{slot:10} run function sae:workstation/drop_slot/10
execute if data storage fancyui:data callback_data{slot:12} run function sae:workstation/drop_slot/12
execute if data storage fancyui:data callback_data{slot:14} run function sae:workstation/drop_slot/14
function sae:escrow/store
tellraw @a[distance=..8] [{"text":"[Enchanting] ","color":"dark_aqua"},{"text":"The operation was cancelled because another player changed the Workstation.","color":"red"}]
