
scoreboard players set #actor_ok sae.tmp 0
execute store result score #actor0 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[0]
execute store result score #actor1 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[1]
execute store result score #actor2 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[2]
execute store result score #actor3 sae.tmp run data get entity @p[distance=..8,sort=nearest,limit=1] UUID[3]
execute if score #actor0 sae.tmp = @s sae.uuid0 if score #actor1 sae.tmp = @s sae.uuid1 if score #actor2 sae.tmp = @s sae.uuid2 if score #actor3 sae.tmp = @s sae.uuid3 run scoreboard players set #actor_ok sae.tmp 1
execute if score #actor_ok sae.tmp matches 1 run function sae:workstation/session/snapshot
execute if score #actor_ok sae.tmp matches 0 run function sae:workstation/session/conflict
