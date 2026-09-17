tag @s add sav.stocked
execute if data entity @s Offers.Recipes[0] run return run function sav:sort/cartographer
data modify storage sav:stock recipes set value []
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":1},"sell":{"id":"minecraft:spyglass","count":1},"maxUses":100000,"xp":0}
data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":2},"sell":{"id":"minecraft:compass","count":1},"maxUses":100000,"xp":0}
item replace entity @s weapon.mainhand with minecraft:jungle_pyramid_map
item modify entity @s weapon.mainhand sav:cartographer/sell_jungle_pyramid_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:swamp_hut_map
item modify entity @s weapon.mainhand sav:cartographer/sell_swamp_hut_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:desert_village_map
item modify entity @s weapon.mainhand sav:cartographer/sell_desert_village_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:plains_village_map
item modify entity @s weapon.mainhand sav:cartographer/sell_plains_village_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:savanna_village_map
item modify entity @s weapon.mainhand sav:cartographer/sell_savanna_village_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:snowy_village_map
item modify entity @s weapon.mainhand sav:cartographer/sell_snowy_village_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:taiga_village_map
item modify entity @s weapon.mainhand sav:cartographer/sell_taiga_village_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:buried_trial_chambers_map
item modify entity @s weapon.mainhand sav:cartographer/sell_buried_trial_chambers_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:ocean_monument_map
item modify entity @s weapon.mainhand sav:cartographer/sell_ocean_monument_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:woodland_mansion_map
item modify entity @s weapon.mainhand sav:cartographer/sell_woodland_mansion_map
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes append value {"buy":{"id":"minecraft:emerald","count":16},"sell":{},"maxUses":100000,"xp":0}
execute if items entity @s weapon.mainhand * run data modify storage sav:stock recipes[-1].sell set from entity @s equipment.mainhand
item replace entity @s weapon.mainhand with minecraft:air
data modify entity @s Offers.Recipes set from storage sav:stock recipes
