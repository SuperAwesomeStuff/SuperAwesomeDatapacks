
scoreboard players set successful_call fancyui.master 0
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_enchant"} run data modify entity @s data.sae.mode set value "enchant"
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"mode_transfer"} run data modify entity @s data.sae.mode set value "transfer"
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_armor"} run data merge entity @s {data:{sae:{category:"Armor",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_melee"} run data merge entity @s {data:{sae:{category:"Melee",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_ranged"} run data merge entity @s {data:{sae:{category:"Ranged",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_tools"} run data merge entity @s {data:{sae:{category:"Tools",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_movement"} run data merge entity @s {data:{sae:{category:"Movement and water",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"tab_curses"} run data merge entity @s {data:{sae:{category:"Curses",page:0}}}
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"previous"} run function sae:workstation/reference/previous
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"next"} run function sae:workstation/reference/next
execute if data storage fancyui:data button.components."minecraft:custom_data".sae{action:"confirm"} run function sae:workstation/confirm
function sae:workstation/render
