
execute if entity @a[tag=fancyui.button.clicker,scores={sae.cooldown=1..}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
tag @a remove sae.actor
tag @a[tag=fancyui.button.clicker] add sae.actor
scoreboard players set #valid sae.tmp 0
data remove entity @s data.sae.pending
data remove entity @s data.sae.enchantment
data remove entity @s data.sae.catalyst
data remove entity @s data.sae.curse
function sae:enchant/validate_selection
tag @a remove sae.actor
execute unless score #valid sae.tmp matches 1 run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute if data entity @s data.sae{curse:true} run return run function sae:workstation/select_curse
function sae:workstation/apply_selection
