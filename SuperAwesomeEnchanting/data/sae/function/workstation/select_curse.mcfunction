
scoreboard players set #armed_match sae.tmp 0
function sae:workstation/select_curse_match
execute if score #armed_match sae.tmp matches 1 if score @s sae.timer matches 1.. run return run function sae:workstation/apply_selection
data modify entity @s data.sae.armed set value {kind:"curse",choice:""}
data modify entity @s data.sae.armed.choice set from entity @s data.sae.catalyst
execute if data entity @s data.sae.enchantment run data modify entity @s data.sae.armed.choice set from entity @s data.sae.enchantment
scoreboard players set @s sae.timer 60
playsound minecraft:block.enchantment_table.use master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.7 0.7
