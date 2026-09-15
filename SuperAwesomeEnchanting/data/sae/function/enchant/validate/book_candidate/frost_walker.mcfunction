scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments"."minecraft:frost_walker"
execute if score #current sae.tmp matches 2.. run return 0
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute store result entity @s data.sae.pending."minecraft:frost_walker" int 1 run scoreboard players get #next sae.tmp
execute if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp
