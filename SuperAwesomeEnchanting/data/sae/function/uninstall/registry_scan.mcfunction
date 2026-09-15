
execute unless data storage sae:registry uninstalling[0] run return run data remove storage sae:registry entries
data modify storage sae:registry pending set from storage sae:registry uninstalling[0]
data remove storage sae:registry uninstalling[0]
function sae:uninstall/restore_macro with storage sae:registry pending
data remove storage sae:registry pending
function sae:uninstall/registry_scan
