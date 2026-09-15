
# Ensure the master scoreboard exists
scoreboard objectives add fancyui.master dummy

# Apply migration if required
execute unless score version fancyui.master matches 1.. run function fancyui:meta/migrations/latest_version
