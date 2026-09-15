
scoreboard players operation #missing sae.tmp = #required sae.tmp
scoreboard players operation #missing sae.tmp -= #catalyst_count sae.tmp
execute store result storage sae:runtime macro.missing int 1 run scoreboard players get #missing sae.tmp
function sae:workstation/options/add_missing_lore_macro with storage sae:runtime macro
