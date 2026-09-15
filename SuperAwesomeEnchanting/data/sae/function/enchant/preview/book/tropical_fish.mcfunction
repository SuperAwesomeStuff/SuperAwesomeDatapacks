execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
execute unless score #catalyst_count sae.tmp matches 1.. run return 0
function sae:enchant/preview/book_candidate/lure
execute unless data entity @s data.sae.pending run return 0
scoreboard players set #candidates sae.tmp 1
data modify entity @s data.sae.label set value "Book upgrade"
data modify entity @s data.sae.curse set value false
