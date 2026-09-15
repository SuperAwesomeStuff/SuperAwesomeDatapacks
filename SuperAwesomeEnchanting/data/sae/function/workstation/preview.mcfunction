
scoreboard players set #valid sae.tmp 0
scoreboard players set #candidates sae.tmp 0
scoreboard players set #cost sae.tmp 0
data remove entity @s data.sae.pending
data remove entity @s data.sae.enchantment
data remove entity @s data.sae.next
data remove entity @s data.sae.valid
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function sae:transfer/preview
execute unless data entity @s {data:{sae:{mode:"transfer"}}} if items block ~ ~ ~ container.10 minecraft:book run function sae:enchant/preview/book
execute unless data entity @s {data:{sae:{mode:"transfer"}}} if items block ~ ~ ~ container.10 minecraft:enchanted_book run function sae:enchant/preview/book
execute unless data entity @s {data:{sae:{mode:"transfer"}}} unless items block ~ ~ ~ container.10 minecraft:book unless items block ~ ~ ~ container.10 minecraft:enchanted_book run function sae:enchant/preview/equipment
execute if score #candidates sae.tmp matches 1 run scoreboard players set #valid sae.tmp 1
execute if score #candidates sae.tmp matches 2.. run scoreboard players set #valid sae.tmp 0
execute store result entity @s data.sae.valid int 1 run scoreboard players get #valid sae.tmp
execute store result entity @s data.sae.cost int 1 run scoreboard players get #cost sae.tmp
function sae:workstation/preview/control
