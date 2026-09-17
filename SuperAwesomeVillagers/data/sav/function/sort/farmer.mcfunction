data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:carrot"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:potato"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:nether_wart"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:chorus_fruit"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:beetroot"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:apple"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:pumpkin_pie"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:torchflower"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:pitcher_plant"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
