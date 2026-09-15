#
#   Tick
#
#   Purpose: To check if any ui containers have been broken
#
#   Input: None
#


execute if score config.performance fancyui.master matches 1 as @a at @s as @e[type=marker,tag=fancyui.container,distance=..10] run tag @s add fancyui.on_break.tick.target
execute unless score config.performance fancyui.master matches 1 as @e[type=marker,tag=fancyui.container] run tag @s add fancyui.on_break.tick.target

execute as @e[type=marker,tag=fancyui.on_break.tick.target] at @s run function fancyui:ui/on_break/test
tag @e[type=marker,tag=fancyui.on_break.tick.target] remove fancyui.on_break.tick.target
