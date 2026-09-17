data modify storage sav:stock profession set value ""
data modify storage sav:stock profession set from entity @s VillagerData.profession
execute if data storage sav:stock {profession:"minecraft:fisherman"} run return run function sav:stock/fisherman
execute if data storage sav:stock {profession:"minecraft:librarian"} run return run function sav:stock/librarian
execute if data storage sav:stock {profession:"minecraft:farmer"} run return run function sav:stock/farmer
execute if data storage sav:stock {profession:"minecraft:butcher"} run return run function sav:stock/butcher
execute if data storage sav:stock {profession:"minecraft:fletcher"} run return run function sav:stock/fletcher
execute if data storage sav:stock {profession:"minecraft:mason"} run return run function sav:stock/mason
execute if data storage sav:stock {profession:"minecraft:shepherd"} run return run function sav:stock/shepherd
execute if data storage sav:stock {profession:"minecraft:leatherworker"} run return run function sav:stock/leatherworker
execute if data storage sav:stock {profession:"minecraft:cleric"} run return run function sav:stock/cleric
execute if data storage sav:stock {profession:"minecraft:cartographer"} run return run function sav:stock/cartographer
execute if data storage sav:stock {profession:"minecraft:armorer"} run return run function sav:stock/armorer
execute if data storage sav:stock {profession:"minecraft:toolsmith"} run return run function sav:stock/toolsmith
execute if data storage sav:stock {profession:"minecraft:weaponsmith"} run return run function sav:stock/weaponsmith
