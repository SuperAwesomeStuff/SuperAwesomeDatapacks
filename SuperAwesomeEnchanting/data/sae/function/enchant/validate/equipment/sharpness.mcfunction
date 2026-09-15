execute unless items block ~ ~ ~ container.10 #minecraft:enchantable/sharp_weapon run return 0
scoreboard players set #target_count sae.tmp 0
execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count
execute unless score #target_count sae.tmp matches 1 run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:smite" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:impaling" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:density" run return 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:breach" run return 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sharpness"
execute if score #current sae.tmp matches 5.. run return 0
scoreboard players operation #cost sae.tmp = #current sae.tmp
scoreboard players add #cost sae.tmp 1
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/amethyst_block
execute if score #catalyst_count sae.tmp < #required sae.tmp run return 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0
scoreboard players set #valid sae.tmp 1
data modify entity @s data.sae.enchantment set value "minecraft:sharpness"
data modify entity @s data.sae.catalyst set value "amethyst_block"
data modify entity @s data.sae.next set value 5
execute store result entity @s data.sae.next int 1 run scoreboard players get #cost sae.tmp
data modify entity @s data.sae.curse set value false
