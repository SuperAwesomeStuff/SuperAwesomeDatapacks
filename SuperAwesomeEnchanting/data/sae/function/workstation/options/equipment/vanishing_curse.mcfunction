data modify storage sae:runtime option set value {id:"minecraft:glass",name:{text:"Vanishing",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Glass",color:"gray",italic:false}],data:{action:"enchant_option",option:"vanishing_curse"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:vanishing_curse"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 1.. run scoreboard players set #next sae.tmp 1
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.name set value {text:"Vanishing I",color:"aqua",italic:false}
scoreboard players operation #cost sae.tmp = #next sae.tmp
function sae:workstation/options/add_cost_lore
execute if score #current sae.tmp matches 1.. run data modify storage sae:runtime option.lore append value {text:"Maximum tier reached",color:"red",italic:false}
execute if score #current sae.tmp matches 1.. run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/glass
execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore
execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
scoreboard players set #level_ok sae.tmp 0
execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1
execute if entity @a[tag=sae.owner,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1
execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Insufficient levels",color:"red",italic:false}
execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
data modify storage sae:runtime option.lore append value {text:"Grindstones cannot remove this",color:"dark_red",italic:false}
execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"First click arms this curse",color:"yellow",italic:false}
execute if score #available sae.tmp matches 1 if data entity @s data.sae.armed{kind:"curse",choice:"minecraft:vanishing_curse"} if score @s sae.timer matches 1.. run data modify storage sae:runtime option.lore[-1] set value {text:"Click again to apply curse",color:"red",italic:false}
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value "dark_gray"
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Unavailable",color:"red",italic:false}
function sae:workstation/options/place
