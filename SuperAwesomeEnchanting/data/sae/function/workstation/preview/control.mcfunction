
data modify storage sae:runtime control set from block ~ ~ ~ Items[{Slot:16b}]
execute if score #valid sae.tmp matches 1 run function sae:workstation/preview/control_valid
execute unless score #valid sae.tmp matches 1 run function sae:workstation/preview/control_invalid
data modify block ~ ~ ~ Items[{Slot:16b}] set from storage sae:runtime control
data remove storage sae:runtime control
