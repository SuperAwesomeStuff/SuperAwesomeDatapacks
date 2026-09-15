
scoreboard players set #cost sae.tmp 5
scoreboard players set #levels sae.tmp 0
execute as @a[tag=sae.owner] store result score #levels sae.tmp run experience query @s levels
data modify entity @s data.sae.transfer_reason set value "Insufficient levels"
execute unless entity @a[tag=sae.owner,gamemode=creative] if score #levels sae.tmp < #cost sae.tmp run return 0
data modify entity @s data.sae.transfer_reason set value "Ready"
scoreboard players set #valid sae.tmp 1
