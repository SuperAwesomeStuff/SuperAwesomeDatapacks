execute if predicate sav:raid_level_1 run give @s minecraft:emerald 4
execute if predicate sav:raid_level_2 run give @s minecraft:emerald 8
execute if predicate sav:raid_level_3 run give @s minecraft:emerald 12
execute if predicate sav:raid_level_4 run give @s minecraft:emerald 16
execute if predicate sav:raid_level_5 run give @s minecraft:emerald 20
effect clear @s minecraft:hero_of_the_village
advancement revoke @s only sav:raid_reward
