
summon item ~ ~1 ~ {Item:{id:"minecraft:stone",count:1},Tags:["sae.transfer_result"]}
data modify entity @n[type=item,tag=sae.transfer_result,distance=..3] Item set from block ~ ~ ~ Items[{Slot:11b}]
execute if entity @a[tag=sae.owner,limit=1] run data modify entity @n[type=item,tag=sae.transfer_result,distance=..3] Owner set from entity @a[tag=sae.owner,limit=1] UUID
tag @n[type=item,tag=sae.transfer_result,distance=..3] remove sae.transfer_result
scoreboard players set #delivered sae.tmp 1
