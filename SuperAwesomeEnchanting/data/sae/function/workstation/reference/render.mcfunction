execute if data entity @s {data:{sae:{category:"Armor",page:0}}} run function sae:workstation/reference/armor_0
execute if data entity @s {data:{sae:{category:"Melee",page:0}}} run function sae:workstation/reference/melee_0
execute if data entity @s {data:{sae:{category:"Melee",page:1}}} run function sae:workstation/reference/melee_1
execute if data entity @s {data:{sae:{category:"Ranged",page:0}}} run function sae:workstation/reference/ranged_0
execute if data entity @s {data:{sae:{category:"Ranged",page:1}}} run function sae:workstation/reference/ranged_1
execute if data entity @s {data:{sae:{category:"Tools",page:0}}} run function sae:workstation/reference/tools_0
execute if data entity @s {data:{sae:{category:"Movement and water",page:0}}} run function sae:workstation/reference/movement_and_water_0
execute if data entity @s {data:{sae:{category:"Curses",page:0}}} run function sae:workstation/reference/curses_0
execute unless data entity @s data.sae.category run data modify entity @s data.sae.category set value "Armor"
execute unless data entity @s data.sae.page run data modify entity @s data.sae.page set value 0
function sae:workstation/reference/filter
