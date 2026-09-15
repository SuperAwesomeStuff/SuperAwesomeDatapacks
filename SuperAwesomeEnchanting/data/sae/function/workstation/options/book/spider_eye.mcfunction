data modify storage sae:runtime option set value {id:"minecraft:spider_eye",name:{text:"Bane Of Arthropods",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Spider Eye",color:"gray",italic:false}],data:{action:"enchant_option",book:1b,catalyst:"spider_eye"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #any sae.tmp 0
scoreboard players set #cost sae.tmp 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments"."minecraft:bane_of_arthropods"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 5.. run scoreboard players set #next sae.tmp 5
execute unless score #current sae.tmp matches 5.. run scoreboard players set #any sae.tmp 1
execute unless score #current sae.tmp matches 5.. if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Bane Of Arthropods I",color:"gray",italic:false}
execute if score #next sae.tmp matches 2 run data modify storage sae:runtime option.lore append value {text:"Bane Of Arthropods II",color:"gray",italic:false}
execute if score #next sae.tmp matches 3 run data modify storage sae:runtime option.lore append value {text:"Bane Of Arthropods III",color:"gray",italic:false}
execute if score #next sae.tmp matches 4 run data modify storage sae:runtime option.lore append value {text:"Bane Of Arthropods IV",color:"gray",italic:false}
execute if score #next sae.tmp matches 5 run data modify storage sae:runtime option.lore append value {text:"Bane Of Arthropods V",color:"gray",italic:false}
function sae:workstation/options/add_cost_lore
execute unless score #any sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Every result is at maximum tier",color:"red",italic:false}
execute unless score #any sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/spider_eye
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
