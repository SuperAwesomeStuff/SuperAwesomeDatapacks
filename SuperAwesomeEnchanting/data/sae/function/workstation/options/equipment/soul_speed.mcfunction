data modify storage sae:runtime option set value {id:"minecraft:soul_sand",name:{text:"Soul Speed",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Soul Sand",color:"gray",italic:false}],data:{action:"enchant_option",option:"soul_speed"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:soul_speed"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 3.. run scoreboard players set #next sae.tmp 3
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.name set value {text:"Soul Speed I",color:"aqua",italic:false}
execute if score #next sae.tmp matches 2 run data modify storage sae:runtime option.name set value {text:"Soul Speed II",color:"aqua",italic:false}
execute if score #next sae.tmp matches 3 run data modify storage sae:runtime option.name set value {text:"Soul Speed III",color:"aqua",italic:false}
scoreboard players operation #cost sae.tmp = #next sae.tmp
function sae:workstation/options/add_cost_lore
execute if score #current sae.tmp matches 3.. run data modify storage sae:runtime option.lore append value {text:"Maximum tier reached",color:"red",italic:false}
execute if score #current sae.tmp matches 3.. run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/soul_sand
execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore
execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
scoreboard players set #level_ok sae.tmp 0
execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1
execute if entity @a[tag=sae.owner,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1
execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Insufficient levels",color:"red",italic:false}
execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
function sae:workstation/options/style_availability
function sae:workstation/options/place
