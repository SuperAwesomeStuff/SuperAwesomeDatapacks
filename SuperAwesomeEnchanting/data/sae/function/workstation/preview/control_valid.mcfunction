
data modify storage sae:runtime macro.cost set from entity @s data.sae.cost
data modify storage sae:runtime macro.label set from entity @s data.sae.label
data modify storage sae:runtime control.id set value "minecraft:lime_dye"
function sae:workstation/preview/control_valid_macro with storage sae:runtime macro
execute if data entity @s data.sae{curse:true} run function sae:workstation/preview/control_curse
