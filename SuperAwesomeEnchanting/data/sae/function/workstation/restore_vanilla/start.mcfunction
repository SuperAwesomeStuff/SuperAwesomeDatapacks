
scoreboard players set #found sae.tmp 0
execute as @n[type=marker,tag=sae.workstation,distance=..6] at @s run function sae:workstation/restore_vanilla/apply
execute if score #found sae.tmp matches 0 run tellraw @s [{"text":"No workstation found. ","color":"red"},{"text":"Stand within six blocks of a Super Awesome Enchanting table and try again.","color":"gray"}]
