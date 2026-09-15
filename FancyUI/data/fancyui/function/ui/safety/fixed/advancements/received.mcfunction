#
#   Received
#
#   Purpose: To run the logic when received a fixed item
#
#   Input: None
#


# Detected a fixed item in the player's inventory
function fancyui:ui/safety/fixed/inventory/on_detect

advancement revoke @s only fancyui:ui/safety/fixed/received
