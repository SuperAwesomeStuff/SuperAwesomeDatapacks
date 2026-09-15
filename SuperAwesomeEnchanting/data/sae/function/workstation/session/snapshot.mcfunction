
data remove entity @s data.sae.snapshot
execute if data block ~ ~ ~ Items[{Slot:10b}] run data modify entity @s data.sae.snapshot.target set from block ~ ~ ~ Items[{Slot:10b}]
execute if data entity @s {data:{sae:{mode:"transfer"}}} if data block ~ ~ ~ Items[{Slot:11b}] run data modify entity @s data.sae.snapshot.destination set from block ~ ~ ~ Items[{Slot:11b}]
