
scoreboard players set successful_call fancyui.master 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
data modify entity @s data.sae.page set value 0
function sae:workstation/render
