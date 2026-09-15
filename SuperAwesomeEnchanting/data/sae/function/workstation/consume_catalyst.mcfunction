
execute store result score #count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
scoreboard players set #consume sae.tmp 1
execute if data entity @s {data:{sae:{enchantment:"minecraft:infinity"}}} run scoreboard players set #consume sae.tmp 64
execute if data entity @s data.sae.pending."minecraft:infinity" run scoreboard players set #consume sae.tmp 64
scoreboard players operation #count sae.tmp -= #consume sae.tmp
execute if score #count sae.tmp matches ..0 run item replace block ~ ~ ~ container.12 with air
execute if score #count sae.tmp matches 1.. store result storage sae:runtime macro.count int 1 run scoreboard players get #count sae.tmp
execute if score #count sae.tmp matches 1.. run function sae:workstation/set_catalyst_count with storage sae:runtime macro
