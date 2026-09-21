
tag @a remove sae.recipient
scoreboard players operation #recipient0 sae.tmp = @s sae.uuid0
scoreboard players operation #recipient1 sae.tmp = @s sae.uuid1
scoreboard players operation #recipient2 sae.tmp = @s sae.uuid2
scoreboard players operation #recipient3 sae.tmp = @s sae.uuid3
execute as @a store result score @s sae.uuid0 run data get entity @s UUID[0]
execute as @a store result score @s sae.uuid1 run data get entity @s UUID[1]
execute as @a store result score @s sae.uuid2 run data get entity @s UUID[2]
execute as @a store result score @s sae.uuid3 run data get entity @s UUID[3]
execute as @a if score @s sae.uuid0 = #recipient0 sae.tmp if score @s sae.uuid1 = #recipient1 sae.tmp if score @s sae.uuid2 = #recipient2 sae.tmp if score @s sae.uuid3 = #recipient3 sae.tmp run tag @s add sae.recipient
