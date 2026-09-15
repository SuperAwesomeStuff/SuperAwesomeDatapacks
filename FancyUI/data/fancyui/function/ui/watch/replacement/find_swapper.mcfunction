#
#   Find Swapper
#
#   Purpose: To target the player that swapped the item
#
#   Input: None
#


#say watch/replace/find_swapper

execute as @a if items entity @s player.cursor * at @s run function fancyui:ui/watch/replacement/mark_if_swapper
