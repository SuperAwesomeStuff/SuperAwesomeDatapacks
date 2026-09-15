
execute unless data storage sae:escrow returning.items[0] run return 0
summon item ~ ~1 ~ {Tags:["sae.uninstall_return"]}
data modify entity @n[type=item,tag=sae.uninstall_return,distance=..3] Item set from storage sae:escrow returning.items[0]
tag @n[type=item,tag=sae.uninstall_return,distance=..3] remove sae.uninstall_return
data remove storage sae:escrow returning.items[0]
function sae:uninstall/spawn_escrow_items
