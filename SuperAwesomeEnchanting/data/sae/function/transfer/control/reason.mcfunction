execute if data entity @s data.sae{transfer_reason:"Insert exactly one source item"} run function sae:transfer/control/reason_0
execute if data entity @s data.sae{transfer_reason:"Insert exactly one destination item"} run function sae:transfer/control/reason_1
execute if data entity @s data.sae{transfer_reason:"Books cannot be transfer sources"} run function sae:transfer/control/reason_2
execute if data entity @s data.sae{transfer_reason:"Source has no enchantments"} run function sae:transfer/control/reason_3
execute if data entity @s data.sae{transfer_reason:"Destination is already enchanted"} run function sae:transfer/control/reason_4
execute if data entity @s data.sae{transfer_reason:"Source and destination categories do not match"} run function sae:transfer/control/reason_5
execute if data entity @s data.sae{transfer_reason:"Destination cannot accept every enchantment"} run function sae:transfer/control/reason_6
execute if data entity @s data.sae{transfer_reason:"Insufficient levels"} run function sae:transfer/control/reason_7
