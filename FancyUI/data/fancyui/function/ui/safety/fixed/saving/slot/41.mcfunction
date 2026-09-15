
execute if items block ~ ~ ~ container.41 * run tag @s add fancyui.fixed.has_overwrite_item

execute if entity @s[tag=fancyui.fixed.has_overwrite_item,                  tag=fancyui.fixed.set_overwrite_to_cursor] run item replace entity @n[tag=fancyui.cursor.instigator] player.cursor from block ~ ~ ~ container.41
execute if entity @s[tag=fancyui.fixed.has_overwrite_item] unless entity @s[tag=fancyui.fixed.set_overwrite_to_cursor] run tag @s add fancyui.fixed.summon_slot_item

execute if entity @s[tag=fancyui.fixed.summon_slot_item] run item replace entity @s weapon.offhand from block ~ ~ ~ container.41

item replace block ~ ~ ~ container.41 from entity @s weapon.mainhand
