tag @s add sav.stocked
execute if data entity @s Offers.Recipes[0] run return run function sav:sort/wandering_trader
data modify storage sav:stock recipes set value []
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:beetroot_seeds","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:melon_seeds","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:name_tag","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pumpkin_seeds","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:wheat_seeds","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:tropical_fish_bucket","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:pufferfish_bucket","count":1},"maxUses":100000,"xp":0}
item replace entity @s weapon.mainhand with minecraft:potion
item modify entity @s weapon.mainhand sav:wandering_trader/sell_potion
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:nautilus_shell","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:lily_pad","count":5},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:brown_mushroom","count":3},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pale_hanging_moss","count":3},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:red_mushroom","count":3},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:shelf_mushroom","count":3},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:vine","count":3},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:moss_block","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pale_moss_block","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pointed_dripstone","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:rooted_dirt","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:small_dripleaf","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:sulfur_spike","count":2},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:allium","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:azure_bluet","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:blue_orchid","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:cornflower","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:dandelion","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:tall_dry_grass","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:fern","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:lily_of_the_valley","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:open_eyeblossom","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:orange_tulip","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:oxeye_daisy","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:packed_ice","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pink_tulip","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:podzol","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:poppy","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:pumpkin","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:red_tulip","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:sugar_cane","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:white_tulip","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:wildflowers","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":2},"sell":{"id":"minecraft:golden_dandelion","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":2},"sell":{"id":"minecraft:sea_pickle","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:brain_coral_block","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:bubble_coral_block","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:cactus","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:fire_coral_block","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:firefly_bush","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:horn_coral_block","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:kelp","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":3},"sell":{"id":"minecraft:tube_coral_block","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:acacia_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:birch_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:cherry_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:dark_oak_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:jungle_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:mangrove_propagule","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:oak_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:pale_oak_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:poplar_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":5},"sell":{"id":"minecraft:spruce_sapling","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":6},"sell":{"id":"minecraft:blue_ice","count":1},"maxUses":100000,"xp":0}
item replace entity @s weapon.mainhand with minecraft:air
data modify entity @s Offers.Recipes set from storage sav:stock recipes
