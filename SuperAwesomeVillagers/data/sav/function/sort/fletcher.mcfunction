data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:arrow"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:bow"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:crossbow"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:acacia_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:birch_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:cherry_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:crimson_stem"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:dark_oak_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:jungle_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:mangrove_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:oak_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:pale_oak_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:poplar_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:spruce_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"sell":{"id":"minecraft:warped_stem"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
