
execute if items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/apply_book
execute unless items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/apply_equipment
item replace block ~ ~ ~ container.10 with air
function sae:workstation/consume_transfer_catalyst
function sae:workstation/charge_levels
tellraw @a[tag=fancyui.button.clicker] {"text":"All enchantments transferred; the source item was consumed.","color":"green"}
