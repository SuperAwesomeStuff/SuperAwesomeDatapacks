execute if data entity @s data.sae.armed{choice:"minecraft:binding_curse"} if data entity @s data.sae{enchantment:"minecraft:binding_curse"} run scoreboard players set #armed_match sae.tmp 1
execute if data entity @s data.sae.armed{choice:"iron_chain"} if data entity @s data.sae{catalyst:"iron_chain"} run scoreboard players set #armed_match sae.tmp 1
execute if data entity @s data.sae.armed{choice:"minecraft:vanishing_curse"} if data entity @s data.sae{enchantment:"minecraft:vanishing_curse"} run scoreboard players set #armed_match sae.tmp 1
execute if data entity @s data.sae.armed{choice:"glass"} if data entity @s data.sae{catalyst:"glass"} run scoreboard players set #armed_match sae.tmp 1
