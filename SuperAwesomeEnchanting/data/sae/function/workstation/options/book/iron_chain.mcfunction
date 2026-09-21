data modify storage sae:runtime option set value {id:"minecraft:iron_chain",name:{text:"Binding",color:"aqua",italic:false},lore:[{text:"Catalyst: 1 × Iron Chain",color:"gray",italic:false}],data:{action:"enchant_option",book:1b,catalyst:"iron_chain"}}
scoreboard players set #available sae.tmp 1
scoreboard players set #any sae.tmp 0
scoreboard players set #cost sae.tmp 0
scoreboard players set #current sae.tmp 0
execute store result score #current sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].components."minecraft:stored_enchantments"."minecraft:binding_curse"
scoreboard players operation #next sae.tmp = #current sae.tmp
scoreboard players add #next sae.tmp 1
execute if score #current sae.tmp matches 1.. run scoreboard players set #next sae.tmp 1
execute unless score #current sae.tmp matches 1.. run scoreboard players set #any sae.tmp 1
execute unless score #current sae.tmp matches 1.. if score #next sae.tmp > #cost sae.tmp run scoreboard players operation #cost sae.tmp = #next sae.tmp
execute if score #next sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Binding I",color:"gray",italic:false}
function sae:workstation/options/add_cost_lore
execute unless score #any sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Every result is at maximum tier",color:"red",italic:false}
execute unless score #any sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
scoreboard players set #required sae.tmp 1
function sae:workstation/inventory/count/iron_chain
execute if score #catalyst_count sae.tmp < #required sae.tmp run function sae:workstation/options/add_missing_lore
execute if score #catalyst_count sae.tmp < #required sae.tmp run scoreboard players set #available sae.tmp 0
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.actor] store result score #levels sae.tmp run experience query @s levels
scoreboard players set #level_ok sae.tmp 0
execute if score #levels sae.tmp >= #cost sae.tmp run scoreboard players set #level_ok sae.tmp 1
execute if entity @a[tag=sae.actor,gamemode=creative] run scoreboard players set #level_ok sae.tmp 1
execute unless score #level_ok sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Insufficient levels",color:"red",italic:false}
execute unless score #level_ok sae.tmp matches 1 run scoreboard players set #available sae.tmp 0
data modify storage sae:runtime option.lore append value {text:"Grindstones cannot remove this",color:"dark_red",italic:false}
execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"First click arms this curse",color:"yellow",italic:false}
execute if score #available sae.tmp matches 1 if data entity @s data.sae.armed{kind:"curse",choice:"iron_chain"} if score @s sae.timer matches 1.. run data modify storage sae:runtime option.lore[-1] set value {text:"Click again to apply curse",color:"red",italic:false}
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value "dark_gray"
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Unavailable",color:"red",italic:false}
function sae:workstation/options/place
