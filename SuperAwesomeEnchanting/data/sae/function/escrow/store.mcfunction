
data modify storage sae:escrow pending set value {owner:[I;0,0,0,0],items:[]}
execute store result storage sae:escrow pending.owner[0] int 1 run scoreboard players get @s sae.uuid0
execute store result storage sae:escrow pending.owner[1] int 1 run scoreboard players get @s sae.uuid1
execute store result storage sae:escrow pending.owner[2] int 1 run scoreboard players get @s sae.uuid2
execute store result storage sae:escrow pending.owner[3] int 1 run scoreboard players get @s sae.uuid3
execute if data entity @s data.sae.snapshot.target run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.target
execute if data entity @s data.sae.snapshot.destination run data modify storage sae:escrow pending.items append from entity @s data.sae.snapshot.destination
execute if data storage sae:escrow pending.items[0] run data modify storage sae:escrow entries append from storage sae:escrow pending
item replace block ~ ~ ~ container.10 with air
scoreboard players set modified_slot fancyui.master 10
function fancyui:manual_removal
execute if data entity @s {data:{sae:{mode:"transfer"}}} run item replace block ~ ~ ~ container.11 with air
execute if data entity @s {data:{sae:{mode:"transfer"}}} run scoreboard players set modified_slot fancyui.master 11
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function fancyui:manual_removal
data remove storage sae:escrow pending
function sae:workstation/session/release
