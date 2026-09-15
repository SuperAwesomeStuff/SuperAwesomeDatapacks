
execute store result score #page sae.tmp run data get entity @s data.sae.page
scoreboard players add #page sae.tmp 1
execute unless data entity @s {data:{sae:{category:"Melee"}}} unless data entity @s {data:{sae:{category:"Ranged"}}} run scoreboard players set #page sae.tmp 0
execute if score #page sae.tmp matches 2.. run scoreboard players set #page sae.tmp 0
execute store result entity @s data.sae.page int 1 run scoreboard players get #page sae.tmp
