
tag @a remove sae.owner
execute unless entity @s[tag=sae.session] run return 0
scoreboard players operation #owner0 sae.tmp = @s sae.uuid0
scoreboard players operation #owner1 sae.tmp = @s sae.uuid1
scoreboard players operation #owner2 sae.tmp = @s sae.uuid2
scoreboard players operation #owner3 sae.tmp = @s sae.uuid3
execute as @a if score @s sae.uuid0 = #owner0 sae.tmp if score @s sae.uuid1 = #owner1 sae.tmp if score @s sae.uuid2 = #owner2 sae.tmp if score @s sae.uuid3 = #owner3 sae.tmp run tag @s add sae.owner
