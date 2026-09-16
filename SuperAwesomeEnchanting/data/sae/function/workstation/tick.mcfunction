
execute if block ~ ~-1 ~ minecraft:hopper run data modify block ~ ~-1 ~ TransferCooldown set value 20
execute if block ~ ~1 ~ minecraft:hopper run data modify block ~ ~1 ~ TransferCooldown set value 20
execute if block ~1 ~ ~ minecraft:hopper run data modify block ~1 ~ ~ TransferCooldown set value 20
execute if block ~-1 ~ ~ minecraft:hopper run data modify block ~-1 ~ ~ TransferCooldown set value 20
execute if block ~ ~ ~1 minecraft:hopper run data modify block ~ ~ ~1 TransferCooldown set value 20
execute if block ~ ~ ~-1 minecraft:hopper run data modify block ~ ~ ~-1 TransferCooldown set value 20
tag @e[type=hopper_minecart,distance=..2] add sae.hopper_blocked
execute as @e[type=hopper_minecart,distance=..2] run data modify entity @s Enabled set value false
execute if entity @s[tag=sae.session] run function sae:workstation/session/check_owner
execute if score @s sae.timer matches 1.. run scoreboard players remove @s sae.timer 1
execute if score @s sae.timer matches 0 run data remove entity @s data.sae.armed
execute if data entity @s data.sae.render_pending run function sae:workstation/render
execute if entity @s[tag=sae.session] if score #clock sae.clock matches 0 run function sae:workstation/render
execute if entity @s[tag=sae.session] if score #clock sae.clock matches 10 run function sae:workstation/render
