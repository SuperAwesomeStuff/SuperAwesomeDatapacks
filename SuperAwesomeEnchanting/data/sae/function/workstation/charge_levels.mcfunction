
execute if entity @a[tag=fancyui.button.clicker,gamemode=creative] run return 0
execute store result storage sae:runtime macro.cost int 1 run scoreboard players get #cost sae.tmp
function sae:workstation/charge_levels_macro with storage sae:runtime macro
