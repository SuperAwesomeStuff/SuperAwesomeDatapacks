
execute unless data storage sae:registry entries[0] run return run function sae:workstation/unregister_finish
data modify storage sae:registry candidate set from storage sae:registry entries[0]
data remove storage sae:registry entries[0]
execute store result score #candidate_id sae.tmp run data get storage sae:registry candidate.id
execute unless score #candidate_id sae.tmp = #remove_id sae.tmp run data modify storage sae:registry kept append from storage sae:registry candidate
data remove storage sae:registry candidate
function sae:workstation/unregister_scan
