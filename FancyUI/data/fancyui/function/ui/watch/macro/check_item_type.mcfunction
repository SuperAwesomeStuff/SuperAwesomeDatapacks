#
#   Check Item Type
#
#   Purpose: To tag this entity with 'fancyui.watch.correct_item' if the specified container item matches the provided one
#
#   Input: { criteria: string, Slot: int }
#


#$say execute if items block ~ ~ ~ container.$(Slot) $(criteria) run tag @s add fancyui.watch.correct_item
$execute if items block ~ ~ ~ container.$(Slot) $(criteria) run tag @s add fancyui.watch.correct_item
