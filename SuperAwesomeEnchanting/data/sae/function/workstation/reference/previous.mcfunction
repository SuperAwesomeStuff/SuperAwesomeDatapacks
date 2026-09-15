
execute store result score #page sae.tmp run data get entity @s data.sae.page
scoreboard players remove #page sae.tmp 1
execute if score #page sae.tmp matches ..-1 run scoreboard players set #page sae.tmp 0
execute store result entity @s data.sae.page int 1 run scoreboard players get #page sae.tmp
