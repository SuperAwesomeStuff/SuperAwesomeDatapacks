
execute unless entity @s[type=player] run return run tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua"},{"text":"Run /function sae:uninstall as an in-game administrator, not from the server console.","color":"red"}]
function sae:uninstall/registry_start
kill @e[type=item,predicate=fancyui:ui/safety/is_fixed]
tellraw @s [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Workstations were restored. Remove the datapack before restarting.","color":"yellow"}]
