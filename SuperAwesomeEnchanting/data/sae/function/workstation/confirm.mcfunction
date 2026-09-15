
execute unless entity @s[tag=sae.session] run return run tellraw @a[tag=fancyui.button.clicker] {"text":"Insert a target item first.","color":"red"}
function sae:workstation/session/check_clicker
execute unless score #actor_ok sae.tmp matches 1 run return run tellraw @a[tag=fancyui.button.clicker] {"text":"This Workstation belongs to another player.","color":"red"}
function sae:workstation/preview
execute unless data entity @s data.sae{valid:1} run return run tellraw @a[tag=fancyui.button.clicker] {"text":"The inputs no longer describe a valid operation.","color":"red"}
execute as @a[tag=fancyui.button.clicker] store result score #levels sae.tmp run experience query @s levels
execute unless entity @a[tag=fancyui.button.clicker,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return run tellraw @a[tag=fancyui.button.clicker] {"text":"You do not have enough levels.","color":"red"}
execute if data entity @s {data:{sae:{mode:"transfer"}}} run function sae:transfer/apply
execute unless data entity @s {data:{sae:{mode:"transfer"}}} run function sae:enchant/apply
function sae:workstation/session/snapshot
function sae:workstation/render
