#
#   Summon Item
#
#   Purpose: To summon the armor stand's offhand item as a item in the world
#
#   Input: None
#


# say safety/fixed/saving/summon_item

execute at @n[type=armor_stand,tag=fancyui.fixed.armor_stand] run summon item ~ ~ ~ {Item:{id:"minecraft:dirt",count:1b},Tags:["fancyui.saving.item"]}

#tellraw @p {"nbt":"equipment","entity":"@s"}

item replace entity @n[type=item,tag=fancyui.saving.item] contents from entity @s weapon.offhand

tag @n[type=item,tag=fancyui.saving.item] remove fancyui.saving.item
