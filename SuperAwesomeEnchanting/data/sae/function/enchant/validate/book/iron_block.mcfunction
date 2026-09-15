execute unless items block ~ ~ ~ container.10 minecraft:book unless items block ~ ~ ~ container.10 minecraft:enchanted_book run return 0
scoreboard players set #target_count sae.tmp 0
execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count
execute unless score #target_count sae.tmp matches 1 run return 0
scoreboard players set #cost sae.tmp 0
function sae:enchant/validate/book_candidate/unbreaking
execute unless data entity @s data.sae.pending run return 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/iron_block
execute if score #catalyst_count sae.tmp < #required sae.tmp run return 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0
scoreboard players set #valid sae.tmp 1
data modify entity @s data.sae.catalyst set value "iron_block"
data modify entity @s data.sae.curse set value false
