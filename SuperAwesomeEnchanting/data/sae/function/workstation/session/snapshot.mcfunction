
data remove entity @s data.sae.snapshot
execute if data block ~ ~ ~ Items[{Slot:10b}] run data modify entity @s data.sae.snapshot.target set from block ~ ~ ~ Items[{Slot:10b}]
execute if data block ~ ~ ~ Items[{Slot:12b}] run data modify entity @s data.sae.snapshot.catalyst set from block ~ ~ ~ Items[{Slot:12b}]
execute if data block ~ ~ ~ Items[{Slot:14b}] run data modify entity @s data.sae.snapshot.destination set from block ~ ~ ~ Items[{Slot:14b}]
