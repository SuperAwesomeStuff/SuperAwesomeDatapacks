
scoreboard players add #clock sae.clock 1
execute unless score #dependency_notice sae.tmp matches 1 run function sae:dependency/check
execute if score #clock sae.clock matches 20.. run function sae:maintenance/tick
execute if score #clock sae.clock matches 20.. run scoreboard players set #clock sae.clock 0
execute as @e[type=marker,tag=sae.workstation] at @s run function sae:workstation/tick
execute as @e[type=hopper_minecart,tag=sae.hopper_blocked] at @s unless entity @e[type=marker,tag=sae.workstation,distance=..2] run data modify entity @s Enabled set value true
execute as @e[type=hopper_minecart,tag=sae.hopper_blocked] at @s unless entity @e[type=marker,tag=sae.workstation,distance=..2] run tag @s remove sae.hopper_blocked
scoreboard players remove @a[scores={sae.cooldown=1..}] sae.cooldown 1
scoreboard players enable @a sae.vanilla
execute as @a[scores={sae.vanilla=1..}] at @s run function sae:workstation/restore_vanilla/start
scoreboard players set @a[scores={sae.vanilla=1..}] sae.vanilla 0
