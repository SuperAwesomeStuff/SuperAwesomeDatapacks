
function sae:workstation/control/check_owner
execute unless score #actor_ok sae.tmp matches 1 run return 0
execute if entity @a[tag=fancyui.button.clicker,scores={sae.cooldown=1..}] run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
tag @a remove sae.owner
tag @a[tag=fancyui.button.clicker] add sae.owner
function sae:transfer/preview
tag @a remove sae.owner
execute unless score #valid sae.tmp matches 1 run return run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
function sae:transfer/apply
