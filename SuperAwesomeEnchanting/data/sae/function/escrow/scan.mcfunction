
execute unless data storage sae:escrow entries[0] run return run function sae:escrow/finish_scan
data modify storage sae:escrow returning set from storage sae:escrow entries[0]
data remove storage sae:escrow entries[0]
execute store result score #owner0 sae.tmp run data get storage sae:escrow returning.owner[0]
execute store result score #owner1 sae.tmp run data get storage sae:escrow returning.owner[1]
execute store result score #owner2 sae.tmp run data get storage sae:escrow returning.owner[2]
execute store result score #owner3 sae.tmp run data get storage sae:escrow returning.owner[3]
scoreboard players set #escrow_match sae.tmp 0
execute if score #owner0 sae.tmp = @s sae.uuid0 if score #owner1 sae.tmp = @s sae.uuid1 if score #owner2 sae.tmp = @s sae.uuid2 if score #owner3 sae.tmp = @s sae.uuid3 run scoreboard players set #escrow_match sae.tmp 1
execute if score #escrow_match sae.tmp matches 1 run function sae:escrow/return_entry
execute unless score #escrow_match sae.tmp matches 1 run data modify storage sae:escrow kept append from storage sae:escrow returning
data remove storage sae:escrow returning
function sae:escrow/scan
