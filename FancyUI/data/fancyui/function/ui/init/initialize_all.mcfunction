#
#   Initialize Tick
#
#   Purpose: To setup all container markers that have not been initialized
#
#   Input: None
#


# Find uninitalized markers and initialize them
execute as @e[type=marker,tag=fancyui.container,tag=!fancyui.container.init] at @s run function fancyui:ui/init/initialize
