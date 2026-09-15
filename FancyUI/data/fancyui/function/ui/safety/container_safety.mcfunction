#
#   Container Safety
#
#   Purpose: To perform all item safety features on this container
#
#   Input: None
#


# Hopper safety
execute align xyz positioned ~0.5 ~0.5 ~0.5 as @e[type=hopper_minecart,distance=..2] run data modify entity @s Enabled set value false
execute if block ~ ~-1 ~ hopper run data modify block ~ ~-1 ~ TransferCooldown set value 2

# Item removal detection
execute as @e[type=item,distance=..10,predicate=fancyui:ui/safety/is_fixed] at @s run function fancyui:ui/safety/fixed/dropped/on_detect
