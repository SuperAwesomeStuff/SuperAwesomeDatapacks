
execute unless data storage sae:escrow returning.items[0] run return 0
summon item ~ ~1 ~ {Item:{id:"minecraft:stone",count:1},Tags:["sae.escrow_return"],PickupDelay:0s}
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Item set from storage sae:escrow returning.items[0]
data modify entity @n[type=item,tag=sae.escrow_return,distance=..3] Owner set from entity @s UUID
tag @n[type=item,tag=sae.escrow_return,distance=..3] remove sae.escrow_return
data remove storage sae:escrow returning.items[0]
function sae:escrow/spawn_items
