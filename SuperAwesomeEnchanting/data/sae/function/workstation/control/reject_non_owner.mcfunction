
function sae:workstation/session/tag_owner
tellraw @a[tag=fancyui.button.clicker] [{"text":"This Workstation belongs to ","color":"red"},{"selector":"@a[tag=sae.owner]","color":"yellow"},{"text":".","color":"red"}]
tag @a remove sae.owner
