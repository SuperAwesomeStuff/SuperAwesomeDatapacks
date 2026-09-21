
function sae:transfer/tag_recipient
scoreboard players set #delivered sae.tmp 0
execute if entity @a[tag=sae.recipient,limit=1] unless items entity @a[tag=sae.recipient,limit=1] player.cursor * run function sae:transfer/deliver_cursor
execute if score #delivered sae.tmp matches 0 run function sae:transfer/deliver_drop
item replace block ~ ~ ~ container.11 with air
scoreboard players set modified_slot fancyui.master 11
function fancyui:manual_removal
data remove entity @s data.sae.pending_delivery
tag @a remove sae.recipient
function sae:workstation/render
