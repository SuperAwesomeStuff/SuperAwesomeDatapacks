data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:spyglass"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:compass"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:jungle_pyramid_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:swamp_hut_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:desert_village_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:plains_village_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:savanna_village_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:snowy_village_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:taiga_village_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:buried_trial_chambers_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:ocean_monument_map"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:woodland_mansion_map"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
