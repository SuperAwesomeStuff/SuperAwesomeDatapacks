#
#   Slot Type Setup
#
#   Purpose: To set setup the slot in storage fancyui:data slot
#
#   Input: None
#


execute if data storage fancyui:data slot{type:"background"} run function fancyui:ui/init/slot/append_background
execute if data storage fancyui:data slot{type:"item"} run function fancyui:ui/init/slot/append_item
execute if data storage fancyui:data slot{type:"watch"} run function fancyui:ui/init/slot/set_watch
execute if data storage fancyui:data slot{type:"button"} run function fancyui:ui/init/slot/append_button
