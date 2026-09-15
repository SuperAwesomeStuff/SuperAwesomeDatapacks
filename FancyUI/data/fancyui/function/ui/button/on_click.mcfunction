#
#   On Click
#
#   Purpose: To run the necessary logic for when a player clicked a button
#
#   Input: None
#


# say button/on_click

tag @s add fancyui.button.clicker

summon armor_stand ~ ~ ~ {equipment:{},Tags:["fancyui.button.armor_stand"],Invisible:1b}

item replace entity @n[tag=fancyui.button.armor_stand] weapon.mainhand from entity @s player.cursor

# Save the button data
data modify storage fancyui:data button set from entity @n[tag=fancyui.button.armor_stand] equipment.mainhand

# Find the container's marker
execute store result score @n[tag=fancyui.button.armor_stand] fancyui.pos.x run data get storage fancyui:data button.components."minecraft:custom_data".fancyui.origin[0]
execute store result score @n[tag=fancyui.button.armor_stand] fancyui.pos.y run data get storage fancyui:data button.components."minecraft:custom_data".fancyui.origin[1]
execute store result score @n[tag=fancyui.button.armor_stand] fancyui.pos.z run data get storage fancyui:data button.components."minecraft:custom_data".fancyui.origin[2]
execute as @e[type=marker,tag=fancyui.container] if score @s fancyui.pos.x = @n[tag=fancyui.button.armor_stand] fancyui.pos.x if score @s fancyui.pos.y = @n[tag=fancyui.button.armor_stand] fancyui.pos.y if score @s fancyui.pos.z = @n[tag=fancyui.button.armor_stand] fancyui.pos.z run tag @s add fancyui.button.container

# Clean up the armor stand
data remove entity @n[tag=fancyui.button.armor_stand] equipment.mainhand
kill @n[tag=fancyui.button.armor_stand]

# Get the marker slot item
function fancyui:meta/reset_macro
data modify storage fancyui:data macro.destination set value "slot_item"
data modify storage fancyui:data macro.Slot set from storage fancyui:data button.components."minecraft:custom_data".fancyui.Slot
function fancyui:ui/button/macro/get_item with storage fancyui:data macro

execute if data storage fancyui:data slot_item.callback as @n[tag=fancyui.button.container] at @s run function fancyui:ui/button/callback

# Clean up
tag @n[tag=fancyui.button.container] remove fancyui.button.container
tag @s remove fancyui.button.clicker
