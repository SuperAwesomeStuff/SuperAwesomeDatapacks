
scoreboard players set #online sae.tmp 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a store result score @s sae.uuid0 run data get entity @s UUID[0]
execute as @a store result score @s sae.uuid1 run data get entity @s UUID[1]
execute as @a store result score @s sae.uuid2 run data get entity @s UUID[2]
execute as @a store result score @s sae.uuid3 run data get entity @s UUID[3]
execute as @a if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run scoreboard players set #online sae.tmp 1
execute if score #online sae.tmp matches 0 run function sae:escrow/store
