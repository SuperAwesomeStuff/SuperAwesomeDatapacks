data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:beef"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:mutton"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:rabbit_hide"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:cooked_beef"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:cooked_mutton"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:rabbit"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:cooked_rabbit"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
