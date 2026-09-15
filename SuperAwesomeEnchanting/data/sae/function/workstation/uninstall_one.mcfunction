
function sae:workstation/drop_slot/10
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function sae:workstation/drop_slot/11
setblock ~ ~ ~ minecraft:enchanting_table
kill @e[type=block_display,tag=sae.workstation.display,distance=..1]
kill @s
