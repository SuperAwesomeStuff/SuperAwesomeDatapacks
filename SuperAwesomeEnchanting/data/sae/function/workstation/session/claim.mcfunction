
tag @s add sae.session
execute store result score @s sae.uuid0 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[0]
execute store result score @s sae.uuid1 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[1]
execute store result score @s sae.uuid2 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[2]
execute store result score @s sae.uuid3 run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[3]
function sae:workstation/session/snapshot
