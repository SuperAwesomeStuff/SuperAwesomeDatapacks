#
#   Migration File V1
#
#   Purpose: To update the datapack up to this level, then apply new/updated configs or setup
#
#   Input: None
#


tellraw @a ["",{"text":"[FancyUI Datapack]","bold":true,"color":"dark_blue"}," - Setup"]

# Apply last migration
#execute unless score version fancyui.master matches 1.. run function fancyui:meta/migrate/migration_v0

# Set the version
scoreboard players set version fancyui.master 1


scoreboard objectives add fancyui.pos.x dummy
scoreboard objectives add fancyui.pos.y dummy
scoreboard objectives add fancyui.pos.z dummy

# No performance config
scoreboard players set config.performance fancyui.master 0


return 0
scoreboard objectives add fpconflict.conflict_map dummy
