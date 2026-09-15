
scoreboard players set #dependency_notice sae.tmp 1
execute unless score version fancyui.master matches 1.. run tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Missing or incompatible FancyUI datapack. Install the included private compatibility fork.","color":"red"}]
