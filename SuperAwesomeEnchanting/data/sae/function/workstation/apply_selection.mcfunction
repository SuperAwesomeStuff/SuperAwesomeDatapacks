
execute if data entity @s data.sae.pending run function sae:enchant/apply_book
execute unless data entity @s data.sae.pending run function sae:enchant/apply_equipment
scoreboard players set modified_slot fancyui.master 10
function fancyui:manual_placement
function sae:workstation/consume_selected_catalyst
function sae:workstation/charge_levels
scoreboard players set @a[tag=fancyui.button.clicker] sae.cooldown 6
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 1 1
function sae:workstation/session/snapshot
