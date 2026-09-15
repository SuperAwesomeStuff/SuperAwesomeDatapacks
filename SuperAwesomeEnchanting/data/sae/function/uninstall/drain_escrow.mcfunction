
execute unless data storage sae:escrow entries[0] run return 0
data modify storage sae:escrow returning set from storage sae:escrow entries[0]
data remove storage sae:escrow entries[0]
function sae:uninstall/spawn_escrow_items
data remove storage sae:escrow returning
function sae:uninstall/drain_escrow
