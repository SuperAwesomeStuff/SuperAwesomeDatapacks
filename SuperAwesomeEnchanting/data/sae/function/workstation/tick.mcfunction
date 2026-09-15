
execute if block ~ ~-1 ~ minecraft:hopper run data modify block ~ ~-1 ~ TransferCooldown set value 20
execute if block ~ ~1 ~ minecraft:hopper run data modify block ~ ~1 ~ TransferCooldown set value 20
execute if block ~1 ~ ~ minecraft:hopper run data modify block ~1 ~ ~ TransferCooldown set value 20
execute if block ~-1 ~ ~ minecraft:hopper run data modify block ~-1 ~ ~ TransferCooldown set value 20
execute if block ~ ~ ~1 minecraft:hopper run data modify block ~ ~ ~1 TransferCooldown set value 20
execute if block ~ ~ ~-1 minecraft:hopper run data modify block ~ ~ ~-1 TransferCooldown set value 20
tag @e[type=hopper_minecart,distance=..2] add sae.hopper_blocked
execute as @e[type=hopper_minecart,distance=..2] run data modify entity @s Enabled set value false
execute if entity @s[tag=sae.session] run function sae:workstation/session/check_owner
