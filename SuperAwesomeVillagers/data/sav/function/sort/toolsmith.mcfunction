data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:shears"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:flint_and_steel"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:bucket"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_pickaxe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_shovel"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:copper_hoe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_pickaxe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_shovel"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:iron_hoe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_pickaxe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_shovel"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:golden_hoe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_pickaxe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_axe"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_shovel"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:diamond_hoe"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
