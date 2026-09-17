schedule function sav:stock/audit 1s replace
execute as @e[type=minecraft:villager,tag=sav.stocked] unless data entity @s Offers.Recipes[0] run tag @s remove sav.stocked
