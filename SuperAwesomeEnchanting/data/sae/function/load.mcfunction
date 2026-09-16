
scoreboard objectives add sae.tmp dummy
scoreboard objectives add sae.clock dummy
scoreboard objectives add sae.uuid0 dummy
scoreboard objectives add sae.uuid1 dummy
scoreboard objectives add sae.uuid2 dummy
scoreboard objectives add sae.uuid3 dummy
scoreboard objectives add sae.deaths deathCount
scoreboard objectives add sae.cooldown dummy
scoreboard objectives add sae.timer dummy
scoreboard objectives add sae.vanilla trigger
scoreboard players set #clock sae.clock 0
scoreboard players set #dependency_notice sae.tmp 0
execute unless data storage sae:registry next_id run data modify storage sae:registry next_id set value 0
data modify storage sae:catalog version set value "26.3"
tellraw @a [{"text":"[Super Awesome Enchanting] ","color":"dark_aqua","bold":true},{"text":"Loaded for Java 26.3","color":"aqua"}]
