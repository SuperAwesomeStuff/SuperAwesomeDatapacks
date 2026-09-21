data modify storage sae:runtime option set value {id:"minecraft:glowstone",name:{text:"Smite",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Glowstone",color:"gray",italic:false}],data:{action:"enchant_option",book:1b,catalyst:"glowstone"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #any sae.tmp 0
scoreboard players set #cost sae.tmp 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments"."minecraft:smite"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 5.. run scoreboard players set #next sae.tmp 5
execute unless score #current sae.tmp matches 5.. run scoreboard players set #any sae.tmp 1
execute unless score #current sae.tmp matches 5.. if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Smite I",color:"gray",italic:false}
execute if score #next sae.tmp matches 2 run data modify storage sae:runtime option.lore append value {text:"Smite II",color:"gray",italic:false}
execute if score #next sae.tmp matches 3 run data modify storage sae:runtime option.lore append value {text:"Smite III",color:"gray",italic:false}
execute if score #next sae.tmp matches 4 run data modify storage sae:runtime option.lore append value {text:"Smite IV",color:"gray",italic:false}
execute if score #next sae.tmp matches 5 run data modify storage sae:runtime option.lore append value {text:"Smite V",color:"gray",italic:false}
function sae:workstation/options/add_cost_lore
execute unless score #any sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Every result is at maximum tier",color:"red",italic:false}
execute unless score #any sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/glowstone
execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore
execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.actor] store result score #levels sae.tmp run experience query @s levels
scoreboard players set #level_ok sae.tmp 0
execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1
execute if entity @a[tag=sae.actor,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1
execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Insufficient levels",color:"red",italic:false}
execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
function sae:workstation/options/style_availability
function sae:workstation/options/place
