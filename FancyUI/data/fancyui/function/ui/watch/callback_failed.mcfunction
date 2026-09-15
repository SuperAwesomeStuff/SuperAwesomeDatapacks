#
#   Callback Failed
#
#   Purpose: To display that a callback failed and its value
#
#   Input: None
#


# say watch/callback_failed

tellraw @a[distance=..20] [{"text":""},{"text":"Callback failed for function [","bold":true,"color":"red"},{"nbt":"macro.function","storage":"fancyui:data","bold":true,"italic":true,"color":"gold"},{"text":"]","bold":true,"color":"red"}]
