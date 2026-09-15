
execute store result score @s sae.uuid0 run data get entity @s UUID[0]
execute store result score @s sae.uuid1 run data get entity @s UUID[1]
execute store result score @s sae.uuid2 run data get entity @s UUID[2]
execute store result score @s sae.uuid3 run data get entity @s UUID[3]
data remove storage sae:escrow kept
function sae:escrow/scan
