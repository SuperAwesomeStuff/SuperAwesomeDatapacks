data modify storage sav:stock offers set from entity @s Offers.Recipes
data modify storage sav:stock sorted set value []
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:cod"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:salmon"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:raw_copper"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:lapis_lazuli"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:quartz"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:pufferfish"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:tropical_fish"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:raw_iron"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:raw_gold"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:diamond"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:echo_shard"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:netherite_scrap"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:heart_of_the_sea"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:enchanted_golden_apple"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:nether_star"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:birch_log"}}]
data modify storage sav:stock sorted append from storage sav:stock offers[{"buy":{"id":"minecraft:dragon_egg"}}]
execute store result score #offers sav.stock run data get storage sav:stock offers
execute store result score #sorted sav.stock run data get storage sav:stock sorted
execute unless score #offers sav.stock = #sorted sav.stock run return 0
data modify entity @s Offers.Recipes set from storage sav:stock sorted
