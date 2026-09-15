
execute unless entity @s[type=player] run return run tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua"},{"text":"Run /function sae:uninstall as an in-game administrator, not from the server console.","color":"red"}]
execute as @a at @s run function sae:escrow/return
function sae:uninstall/registry_start
function sae:uninstall/drain_escrow
kill @e[type=item,predicate=fancyui:ui/safety/is_fixed]
tellraw @s [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Workstations were restored. Any offline-owner escrow was returned here. Remove the datapack before restarting.","color":"yellow"}]
