
execute unless data entity @s data.sae.book_target run return 0
execute if data entity @s {data:{sae:{page:1}}} run return run function sae:workstation/set_page_zero
data modify entity @s data.sae.page set value 1
data remove entity @s data.sae.armed
scoreboard players set @s sae.timer 0
