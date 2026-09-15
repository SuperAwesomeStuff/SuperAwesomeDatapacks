
execute if block ~ ~ ~ minecraft:enchanting_table align xyz run function sae:workstation/place/create
execute if score #found sae.tmp matches 1 run return 1
scoreboard players add #ray sae.tmp 1
execute if score #ray sae.tmp matches ..24 positioned ^ ^ ^0.25 run function sae:workstation/place/raycast
