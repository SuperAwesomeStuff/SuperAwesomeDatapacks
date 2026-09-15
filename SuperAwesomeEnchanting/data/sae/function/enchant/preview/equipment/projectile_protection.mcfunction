execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
execute unless score #catalyst_count sae.tmp matches 1.. run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:protection" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:blast_protection" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fire_protection" run return 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:projectile_protection"
execute if score #current sae.tmp matches 4.. run return 0
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
scoreboard players add #candidates sae.tmp 1
scoreboard players operation #cost sae.tmp = #next sae.tmp
data modify entity @s data.sae.enchantment set value "minecraft:projectile_protection"
execute store result entity @s data.sae.next int 1 run scoreboard players get #next sae.tmp
data modify entity @s data.sae.label set value "Projectile Protection"
data modify entity @s data.sae.curse set value false
