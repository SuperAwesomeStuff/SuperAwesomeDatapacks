
scoreboard players set successful_call fancyui.master 0
function sae:workstation/unregister
kill @e[type=item,distance=..2,predicate=fancyui:ui/safety/is_fixed]
kill @e[type=item,distance=..2,nbt={Item:{id:"minecraft:chest"}}]
summon item ~ ~ ~ {Item:{id:"minecraft:enchanting_table",count:1}}
kill @e[type=block_display,tag=sae.workstation.display,distance=..1]
kill @s
