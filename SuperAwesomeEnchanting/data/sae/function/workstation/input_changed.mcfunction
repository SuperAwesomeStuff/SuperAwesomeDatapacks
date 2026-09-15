
scoreboard players set successful_call fancyui.master 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
execute unless entity @s[tag=sae.session] if data storage fancyui:data callback_data{slot:10} if data block ~ ~ ~ Items[{Slot:10b}] run function sae:workstation/session/claim
execute unless entity @s[tag=sae.session] if data entity @s {data:{sae:{mode:"transfer"}}} if data storage fancyui:data callback_data{slot:11} if data block ~ ~ ~ Items[{Slot:11b}] run function sae:workstation/session/claim
execute if entity @s[tag=sae.session] run function sae:workstation/session/verify_actor
execute if data entity @s {data:{sae:{mode:"enchant"}}} unless data block ~ ~ ~ Items[{Slot:10b}] run function sae:workstation/session/release
execute if data entity @s {data:{sae:{mode:"transfer"}}} unless data block ~ ~ ~ Items[{Slot:10b}] unless data block ~ ~ ~ Items[{Slot:11b}] run function sae:workstation/session/release
data modify entity @s data.sae.page set value 0
function sae:workstation/render
