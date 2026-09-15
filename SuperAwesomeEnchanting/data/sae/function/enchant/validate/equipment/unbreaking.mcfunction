execute unless items block ~ ~ ~ container.10 #minecraft:enchantable/durability run return 0
scoreboard players set #target_count sae.tmp 0
execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count
execute unless score #target_count sae.tmp matches 1 run return 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:unbreaking"
execute if score #current sae.tmp matches 3.. run return 0
scoreboard players operation #cost sae.tmp = #current sae.tmp
scoreboard players add #cost sae.tmp 1
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/iron_block
execute if score #catalyst_count sae.tmp < #required sae.tmp run return 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0
scoreboard players set #valid sae.tmp 1
data modify entity @s data.sae.enchantment set value "minecraft:unbreaking"
data modify entity @s data.sae.catalyst set value "iron_block"
data modify entity @s data.sae.next set value 3
execute store result entity @s data.sae.next int 1 run scoreboard players get #cost sae.tmp
data modify entity @s data.sae.curse set value false
