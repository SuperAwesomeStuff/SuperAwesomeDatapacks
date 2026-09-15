
scoreboard players set #actor_ok sae.tmp 1
execute if entity @s[tag=sae.session] run function sae:workstation/session/check_clicker
execute unless score #actor_ok sae.tmp matches 1 run playsound minecraft:block.note_block.bass master @a[tag=fancyui.button.clicker] ~ ~ ~ 0.6 0.7
execute unless score #actor_ok sae.tmp matches 1 run function sae:workstation/control/reject_non_owner
