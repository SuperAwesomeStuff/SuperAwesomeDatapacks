#
#   Watch Tick
#
#   Purpose: To update all marker container's watch slots
#
#   Input: None
#


execute if score config.performance fancyui.master matches 1 as @a at @s as @e[type=marker,tag=fancyui.container.watch,distance=..10] run tag @s add fancyui.watch.tick.target
execute unless score config.performance fancyui.master matches 1 as @e[type=marker,tag=fancyui.container.watch] run tag @s add fancyui.watch.tick.target

execute as @e[type=marker,tag=fancyui.watch.tick.target] at @s run function fancyui:ui/watch/update_rec
tag @e[type=marker,tag=fancyui.watch.tick.target] remove fancyui.watch.tick.target
