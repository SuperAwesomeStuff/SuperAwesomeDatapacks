
execute store result score #registry_id sae.tmp run data get storage sae:registry next_id
scoreboard players add #registry_id sae.tmp 1
execute store result storage sae:registry next_id int 1 run scoreboard players get #registry_id sae.tmp
scoreboard players operation @s sae.tmp = #registry_id sae.tmp
data modify storage sae:registry pending set value {id:0,x:0,y:0,z:0,dimension:"minecraft:overworld"}
execute store result storage sae:registry pending.id int 1 run scoreboard players get #registry_id sae.tmp
execute store result storage sae:registry pending.x int 1 run data get entity @s Pos[0]
execute store result storage sae:registry pending.y int 1 run data get entity @s Pos[1]
execute store result storage sae:registry pending.z int 1 run data get entity @s Pos[2]
execute if dimension minecraft:the_nether run data modify storage sae:registry pending.dimension set value "minecraft:the_nether"
execute if dimension minecraft:the_end run data modify storage sae:registry pending.dimension set value "minecraft:the_end"
data modify storage sae:registry entries append from storage sae:registry pending
data remove storage sae:registry pending
