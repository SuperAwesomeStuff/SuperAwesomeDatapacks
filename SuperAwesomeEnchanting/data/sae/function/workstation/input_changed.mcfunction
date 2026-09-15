
scoreboard players set successful_call fancyui.master 0
execute unless entity @s[tag=sae.session] if data storage fancyui:data callback_data{slot:10} if data block ~ ~ ~ Items[{Slot:10b}] run function sae:workstation/session/claim
execute if entity @s[tag=sae.session] run function sae:workstation/session/verify_actor
execute unless data block ~ ~ ~ Items[{Slot:10b}] unless data block ~ ~ ~ Items[{Slot:12b}] unless data block ~ ~ ~ Items[{Slot:14b}] run function sae:workstation/session/release
function sae:workstation/render
