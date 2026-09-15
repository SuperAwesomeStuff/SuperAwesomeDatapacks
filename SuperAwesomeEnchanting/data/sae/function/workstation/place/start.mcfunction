
advancement revoke @s only sae:place_workstation
scoreboard players set #ray sae.tmp 0
scoreboard players set #found sae.tmp 0
execute anchored eyes positioned ^ ^ ^0.25 run function sae:workstation/place/raycast
