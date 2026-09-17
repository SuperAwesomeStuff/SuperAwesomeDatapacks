data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:shield"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_helmet"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_chestplate"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_leggings"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_boots"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_helmet"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_chestplate"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_leggings"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_boots"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_helmet"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_chestplate"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_leggings"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_boots"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_helmet"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_chestplate"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_leggings"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_boots"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
