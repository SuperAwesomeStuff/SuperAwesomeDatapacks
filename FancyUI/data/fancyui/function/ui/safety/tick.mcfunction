#
#   Safety Tick
#
#   Purpose: To update all item safety features
#
#   Input: None
#


execute as @a if items entity @s player.cursor *[custom_data~{fancyui:{fixed:true}}] at @s run function fancyui:ui/safety/fixed/cursor/on_detect

execute as @e[type=marker,tag=fancyui.container] at @s run function fancyui:ui/safety/container_safety
