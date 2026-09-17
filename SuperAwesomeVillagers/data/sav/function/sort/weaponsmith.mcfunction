data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_sword"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_sword"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_sword"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_sword"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_axe"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
