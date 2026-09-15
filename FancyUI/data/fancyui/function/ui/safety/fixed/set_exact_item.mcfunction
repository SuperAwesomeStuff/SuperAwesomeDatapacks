#
#   Set Exact Item
#
#   Purpose: To save this armor stand's mainhand item to its exact designated position in the 'fancyui.fixed.target' marker's container
#
#   Input: None
#


# say safety/fixed/set_exact_item

#tellraw @p [{"text":"a: "},{"nbt":"equipment","entity":"@s"}]

execute as @n[tag=fancyui.fixed.armor_stand] at @s run function fancyui:ui/safety/fixed/saving/save_overwriting_item

execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:0b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.0 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:1b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.1 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:2b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.2 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:3b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.3 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:4b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.4 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:5b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.5 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:6b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.6 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:7b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.7 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:8b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.8 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:9b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.9 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:10b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.10 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:11b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.11 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:12b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.12 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:13b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.13 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:14b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.14 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:15b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.15 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:16b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.16 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:17b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.17 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:18b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.18 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:19b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.19 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:20b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.20 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:21b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.21 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:22b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.22 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:23b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.23 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:24b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.24 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:25b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.25 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:26b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.26 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:27b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.27 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:28b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.28 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:29b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.29 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:30b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.30 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:31b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.31 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:32b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.32 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:33b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.33 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:34b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.34 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:35b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.35 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:36b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.36 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:37b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.37 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:38b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.38 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:39b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.39 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:40b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.40 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:41b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.41 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:42b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.42 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:43b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.43 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:44b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.44 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:45b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.45 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:46b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.46 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:47b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.47 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:48b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.48 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:49b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.49 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:50b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.50 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:51b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.51 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:52b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.52 from entity @s weapon.mainhand
execute if items entity @s weapon.mainhand *[custom_data~{fancyui:{Slot:53b}}] at @n[type=marker,tag=fancyui.fixed.target] run return run item replace block ~ ~ ~ container.53 from entity @s weapon.mainhand
