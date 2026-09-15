
execute as @e[type=marker,tag=fancyui.container] at @s if data entity @s data.sae.pending_delivery run function sae:transfer/deliver_one
