#
#   Test Block
#
#   Purpose: To set the scoreboard 'test_block.matches fancyui.master' to 1 if the current block matches the provided one
#
#   Input: { block: string }
#


scoreboard players set test_block.matches fancyui.master 0
#$say execute if block ~ ~ ~ $(block) run scoreboard players set test_block.matches fancyui.master 1
$execute if block ~ ~ ~ $(block) run scoreboard players set test_block.matches fancyui.master 1
