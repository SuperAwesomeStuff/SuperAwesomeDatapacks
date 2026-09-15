data modify storage sae:runtime option set value {id:"minecraft:amethyst_block",name:{text:"Breach",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Amethyst Block",color:"gray",italic:false}],data:{action:"enchant_option",option:"breach"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:breach"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 4.. run scoreboard players set #next sae.tmp 4
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.name set value {text:"Breach I",color:"aqua",italic:false}
execute if score #next sae.tmp matches 2 run data modify storage sae:runtime option.name set value {text:"Breach II",color:"aqua",italic:false}
execute if score #next sae.tmp matches 3 run data modify storage sae:runtime option.name set value {text:"Breach III",color:"aqua",italic:false}
execute if score #next sae.tmp matches 4 run data modify storage sae:runtime option.name set value {text:"Breach IV",color:"aqua",italic:false}
scoreboard players operation #cost sae.tmp = #next sae.tmp
function sae:workstation/options/add_cost_lore
execute if score #current sae.tmp matches 4.. run data modify storage sae:runtime option.lore append value {text:"Maximum tier reached",color:"red",italic:false}
execute if score #current sae.tmp matches 4.. run scoreboard players set #available sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sharpness" run data modify storage sae:runtime option.lore append value {text:"Conflicts with Sharpness",color:"red",italic:false}
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sharpness" run scoreboard players set #available sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:smite" run data modify storage sae:runtime option.lore append value {text:"Conflicts with Smite",color:"red",italic:false}
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:smite" run scoreboard players set #available sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" run data modify storage sae:runtime option.lore append value {text:"Conflicts with Bane Of Arthropods",color:"red",italic:false}
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" run scoreboard players set #available sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:impaling" run data modify storage sae:runtime option.lore append value {text:"Conflicts with Impaling",color:"red",italic:false}
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:impaling" run scoreboard players set #available sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:density" run data modify storage sae:runtime option.lore append value {text:"Conflicts with Density",color:"red",italic:false}
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:density" run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/amethyst_block
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
