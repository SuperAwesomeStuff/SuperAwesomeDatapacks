
$execute store success score #was_forceloaded sae.tmp in $(dimension) positioned $(x) $(y) $(z) run forceload query ~ ~
$execute in $(dimension) positioned $(x) $(y) $(z) run forceload add ~ ~
$execute in $(dimension) positioned $(x) $(y) $(z) as @e[type=marker,tag=sae.workstation,distance=..1,limit=1] at @s run function sae:workstation/uninstall_one
$execute in $(dimension) positioned $(x) $(y) $(z) unless entity @e[type=marker,tag=sae.workstation,distance=..1,limit=1] run setblock ~ ~ ~ minecraft:enchanting_table
$execute if score #was_forceloaded sae.tmp matches 0 in $(dimension) positioned $(x) $(y) $(z) run forceload remove ~ ~
