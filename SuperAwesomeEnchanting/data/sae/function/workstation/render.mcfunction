
data remove entity @s data.sae.render_pending
execute unless items block ~ ~ ~ container.0 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.1 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.2 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.3 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.4 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.5 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.6 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.7 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.8 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.9 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.12 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.13 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.14 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.15 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.16 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.17 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.18 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.19 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.20 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.21 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.22 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.23 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.24 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.25 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute unless items block ~ ~ ~ container.26 *[minecraft:custom_data~{fancyui:{fixed:true}}] run data modify entity @s data.sae.render_pending set value true
execute if data entity @s data.sae.render_pending run return 0
tag @a remove sae.actor
tag @p[distance=..8,sort=nearest,limit=1] add sae.actor
function sae:workstation/options/render
tag @a remove sae.actor
