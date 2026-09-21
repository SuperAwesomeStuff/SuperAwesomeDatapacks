
execute if entity @a[tag=fancyui.button.clicker,scores={sae.cooldown=1..}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
tag @a remove sae.actor
tag @a[tag=fancyui.button.clicker] add sae.actor
function sae:transfer/preview
execute unless score #valid sae.tmp matches 1 run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute if score #valid sae.tmp matches 1 run function sae:transfer/apply
tag @a remove sae.actor
