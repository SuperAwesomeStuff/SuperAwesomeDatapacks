
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute if data entity @s {data:{sae:{mode:"transfer"}}} if data block ~ ~ ~ Items[{Slot:11b}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute if data entity @s {data:{sae:{mode:"transfer"}}} run return run function sae:workstation/set_mode_enchant
function sae:workstation/destination_guard/hide
data modify entity @s data.sae.mode set value "transfer"
data modify entity @s data.sae.page set value 0
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
