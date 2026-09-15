
execute unless data block ~ ~ ~ Items[{Slot:12b}] run return 0
summon item ~ ~1 ~ {Tags:["sae.workstation_return"]}
data modify entity @n[type=item,tag=sae.workstation_return,distance=..3] Item set from block ~ ~ ~ Items[{Slot:12b}]
tag @n[type=item,tag=sae.workstation_return,distance=..3] remove sae.workstation_return
item replace block ~ ~ ~ container.12 with air
