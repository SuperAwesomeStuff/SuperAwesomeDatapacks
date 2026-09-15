
function sae:workstation/options/clear
data remove entity @s data.sae.book_target
execute if data entity @s {data:{sae:{mode:"transfer"}}} run return run function sae:transfer/render
function sae:workstation/options/render_enchant_controls
scoreboard players set #target_count sae.tmp 0
execute store result score #target_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count
execute if score #target_count sae.tmp matches 0 run return run function sae:workstation/options/instruction_empty
execute unless score #target_count sae.tmp matches 1 run return run function sae:workstation/options/instruction_stack
execute if items block ~ ~ ~ container.10 minecraft:book run data modify entity @s data.sae.book_target set value true
execute if items block ~ ~ ~ container.10 minecraft:enchanted_book run data modify entity @s data.sae.book_target set value true
execute if data entity @s data.sae.book_target run function sae:workstation/options/render_book_page_control
execute if data entity @s {data:{sae:{book_target:true,page:1}}} run return run function sae:workstation/options/book_page_1
execute if data entity @s data.sae.book_target run return run function sae:workstation/options/book_page_0
function sae:workstation/options/equipment
