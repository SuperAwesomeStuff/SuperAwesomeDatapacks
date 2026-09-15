
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.name.color set value "dark_gray"
execute unless score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Unavailable",color:"red",italic:false}
execute if score #available sae.tmp matches 1 run data modify storage sae:runtime option.lore append value {text:"Click to apply",color:"yellow",italic:false}
