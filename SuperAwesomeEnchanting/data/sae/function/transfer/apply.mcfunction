
function sae:transfer/capture_recipient
execute if items block ~ ~ ~ container.11 minecraft:book run function sae:transfer/apply_book
execute unless items block ~ ~ ~ container.11 minecraft:book run function sae:transfer/apply_equipment
scoreboard players set modified_slot fancyui.master 11
function fancyui:manual_placement
item replace block ~ ~ ~ container.10 with air
scoreboard players set modified_slot fancyui.master 10
function fancyui:manual_removal
function sae:workstation/charge_levels
scoreboard players set @a[tag=fancyui.button.clicker] sae.cooldown 6
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 1 1
data modify entity @s data.sae.pending_delivery set value true
schedule function sae:transfer/deliver 1t append
