
data modify storage sae:escrow pending set value {owner:[I;0,0,0,0],items:[]}
execute store result storage sae:escrow pending.owner[0] int 1 run scoreboard players get @s sae.uuid0
execute store result storage sae:escrow pending.owner[1] int 1 run scoreboard players get @s sae.uuid1
execute store result storage sae:escrow pending.owner[2] int 1 run scoreboard players get @s sae.uuid2
execute store result storage sae:escrow pending.owner[3] int 1 run scoreboard players get @s sae.uuid3
execute if data entity @s data.sae.snapshot.target run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.target
execute if data entity @s data.sae.snapshot.catalyst run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.catalyst
execute if data entity @s data.sae.snapshot.destination run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.destination
execute if data storage sae:escrow pending.items[0] run data modify storage sae:escrow entries append from storage sae:escrow pending
item replace block ~ ~ ~ container.10 with air
item replace block ~ ~ ~ container.12 with air
item replace block ~ ~ ~ container.14 with air
data remove storage sae:escrow pending
function sae:workstation/session/release
