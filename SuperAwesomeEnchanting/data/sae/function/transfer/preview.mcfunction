execute store result score #source_count sae.tmp run data get block ~ ~ ~ Items[{Slot:10b}].count
execute store result score #destination_count sae.tmp run data get block ~ ~ ~ Items[{Slot:14b}].count
execute store result score #catalyst_count sae.tmp run data get block ~ ~ ~ Items[{Slot:12b}].count
execute unless score #source_count sae.tmp matches 1 run return 0
execute unless score #destination_count sae.tmp matches 1 run return 0
execute unless score #catalyst_count sae.tmp matches 1.. run return 0
execute unless items block ~ ~ ~ container.12 minecraft:amethyst_block run return 0
execute if items block ~ ~ ~ container.10 minecraft:book run return 0
execute if items block ~ ~ ~ container.10 minecraft:enchanted_book run return 0
scoreboard players set #source_enchants sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:aqua_affinity" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:blast_protection" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:breach" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:channeling" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:binding_curse" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:vanishing_curse" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:density" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:depth_strider" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:efficiency" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:feather_falling" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fire_aspect" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fire_protection" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:flame" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fortune" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:frost_walker" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:impaling" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:infinity" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:knockback" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:looting" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:loyalty" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:luck_of_the_sea" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:lunge" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:lure" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:mending" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:multishot" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:piercing" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:power" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:projectile_protection" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:protection" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:punch" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:quick_charge" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:respiration" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:riptide" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sharpness" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:silk_touch" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:smite" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:soul_speed" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sweeping_edge" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:swift_sneak" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:thorns" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:unbreaking" run scoreboard players add #source_enchants sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:wind_burst" run scoreboard players add #source_enchants sae.tmp 1
execute unless score #source_enchants sae.tmp matches 1.. run return 0
scoreboard players set #destination_ok sae.tmp 1
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:aqua_affinity" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:aqua_affinity" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:blast_protection" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:blast_protection" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:breach" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:breach" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:channeling" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:channeling" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:binding_curse" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:binding_curse" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:vanishing_curse" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:vanishing_curse" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:density" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:density" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:depth_strider" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:depth_strider" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:efficiency" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:efficiency" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:feather_falling" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:feather_falling" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fire_aspect" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fire_aspect" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fire_protection" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fire_protection" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:flame" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:flame" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fortune" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:fortune" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:frost_walker" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:frost_walker" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:impaling" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:impaling" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:infinity" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:infinity" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:knockback" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:knockback" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:looting" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:looting" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:loyalty" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:loyalty" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:luck_of_the_sea" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:luck_of_the_sea" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:lunge" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:lunge" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:lure" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:lure" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:mending" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:multishot" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:multishot" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:piercing" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:piercing" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:power" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:power" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:projectile_protection" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:projectile_protection" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:protection" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:protection" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:punch" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:punch" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:quick_charge" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:quick_charge" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:respiration" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:respiration" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:riptide" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:riptide" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:sharpness" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:sharpness" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:silk_touch" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:silk_touch" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:smite" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:smite" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:soul_speed" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:soul_speed" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:sweeping_edge" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:sweeping_edge" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:swift_sneak" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:swift_sneak" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:thorns" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:thorns" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:unbreaking" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:unbreaking" run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:wind_burst" unless items block ~ ~ ~ container.14 #sae:netherite_equipment run scoreboard players set #destination_ok sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:14b}].components."minecraft:enchantments"."minecraft:wind_burst" run scoreboard players set #destination_ok sae.tmp 0
execute unless score #destination_ok sae.tmp matches 1 run return 0
scoreboard players set #category_match sae.tmp 0
execute if items block ~ ~ ~ container.14 minecraft:book run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/helmet if items block ~ ~ ~ container.14 #sae:transfer/helmet run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/chestplate if items block ~ ~ ~ container.14 #sae:transfer/chestplate run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/leggings if items block ~ ~ ~ container.14 #sae:transfer/leggings run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/boots if items block ~ ~ ~ container.14 #sae:transfer/boots run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/sword if items block ~ ~ ~ container.14 #sae:transfer/sword run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/axe if items block ~ ~ ~ container.14 #sae:transfer/axe run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/pickaxe if items block ~ ~ ~ container.14 #sae:transfer/pickaxe run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/shovel if items block ~ ~ ~ container.14 #sae:transfer/shovel run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/hoe if items block ~ ~ ~ container.14 #sae:transfer/hoe run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/spear if items block ~ ~ ~ container.14 #sae:transfer/spear run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/bow if items block ~ ~ ~ container.14 #sae:transfer/bow run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/crossbow if items block ~ ~ ~ container.14 #sae:transfer/crossbow run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/mace if items block ~ ~ ~ container.14 #sae:transfer/mace run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/trident if items block ~ ~ ~ container.14 #sae:transfer/trident run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/shield if items block ~ ~ ~ container.14 #sae:transfer/shield run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/elytra if items block ~ ~ ~ container.14 #sae:transfer/elytra run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/fishing_rod if items block ~ ~ ~ container.14 #sae:transfer/fishing_rod run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/shears if items block ~ ~ ~ container.14 #sae:transfer/shears run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/brush if items block ~ ~ ~ container.14 #sae:transfer/brush run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/flint_and_steel if items block ~ ~ ~ container.14 #sae:transfer/flint_and_steel run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/carrot_on_a_stick if items block ~ ~ ~ container.14 #sae:transfer/carrot_on_a_stick run scoreboard players set #category_match sae.tmp 1
execute if items block ~ ~ ~ container.10 #sae:transfer/warped_fungus_on_a_stick if items block ~ ~ ~ container.14 #sae:transfer/warped_fungus_on_a_stick run scoreboard players set #category_match sae.tmp 1
execute unless score #category_match sae.tmp matches 1 run return 0
scoreboard players set #compatible sae.tmp 1
execute if items block ~ ~ ~ container.14 minecraft:book run function sae:transfer/preview_valid
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:aqua_affinity" unless items block ~ ~ ~ container.14 #minecraft:enchantable/head_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:bane_of_arthropods" unless items block ~ ~ ~ container.14 #minecraft:enchantable/weapon run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:blast_protection" unless items block ~ ~ ~ container.14 #minecraft:enchantable/armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:breach" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mace run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:channeling" unless items block ~ ~ ~ container.14 #minecraft:enchantable/trident run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:binding_curse" unless items block ~ ~ ~ container.14 #minecraft:enchantable/equippable run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:vanishing_curse" unless items block ~ ~ ~ container.14 #minecraft:enchantable/vanishing run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:density" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mace run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:depth_strider" unless items block ~ ~ ~ container.14 #minecraft:enchantable/foot_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:efficiency" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mining run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:feather_falling" unless items block ~ ~ ~ container.14 #minecraft:enchantable/foot_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fire_aspect" unless items block ~ ~ ~ container.14 #minecraft:enchantable/fire_aspect run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fire_protection" unless items block ~ ~ ~ container.14 #minecraft:enchantable/armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:flame" unless items block ~ ~ ~ container.14 #minecraft:enchantable/bow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:fortune" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mining_loot run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:frost_walker" unless items block ~ ~ ~ container.14 #minecraft:enchantable/foot_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:impaling" unless items block ~ ~ ~ container.14 #minecraft:enchantable/trident run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:infinity" unless items block ~ ~ ~ container.14 #minecraft:enchantable/bow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:knockback" unless items block ~ ~ ~ container.14 #minecraft:enchantable/melee_weapon run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:looting" unless items block ~ ~ ~ container.14 #minecraft:enchantable/melee_weapon run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:loyalty" unless items block ~ ~ ~ container.14 #minecraft:enchantable/trident run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:luck_of_the_sea" unless items block ~ ~ ~ container.14 #minecraft:enchantable/fishing run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:lunge" unless items block ~ ~ ~ container.14 #minecraft:enchantable/lunge run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:lure" unless items block ~ ~ ~ container.14 #minecraft:enchantable/fishing run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:mending" unless items block ~ ~ ~ container.14 #minecraft:enchantable/durability run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:multishot" unless items block ~ ~ ~ container.14 #minecraft:enchantable/crossbow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:piercing" unless items block ~ ~ ~ container.14 #minecraft:enchantable/crossbow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:power" unless items block ~ ~ ~ container.14 #minecraft:enchantable/bow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:projectile_protection" unless items block ~ ~ ~ container.14 #minecraft:enchantable/armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:protection" unless items block ~ ~ ~ container.14 #minecraft:enchantable/armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:punch" unless items block ~ ~ ~ container.14 #minecraft:enchantable/bow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:quick_charge" unless items block ~ ~ ~ container.14 #minecraft:enchantable/crossbow run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:respiration" unless items block ~ ~ ~ container.14 #minecraft:enchantable/head_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:riptide" unless items block ~ ~ ~ container.14 #minecraft:enchantable/trident run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sharpness" unless items block ~ ~ ~ container.14 #minecraft:enchantable/sharp_weapon run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:silk_touch" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mining_loot run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:smite" unless items block ~ ~ ~ container.14 #minecraft:enchantable/weapon run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:soul_speed" unless items block ~ ~ ~ container.14 #minecraft:enchantable/foot_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:sweeping_edge" unless items block ~ ~ ~ container.14 #minecraft:enchantable/sweeping run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:swift_sneak" unless items block ~ ~ ~ container.14 #minecraft:enchantable/leg_armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:thorns" unless items block ~ ~ ~ container.14 #minecraft:enchantable/armor run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:unbreaking" unless items block ~ ~ ~ container.14 #minecraft:enchantable/durability run scoreboard players set #compatible sae.tmp 0
execute if data block ~ ~ ~ Items[{Slot:10b}].components."minecraft:enchantments"."minecraft:wind_burst" unless items block ~ ~ ~ container.14 #minecraft:enchantable/mace run scoreboard players set #compatible sae.tmp 0
execute if score #compatible sae.tmp matches 1 run function sae:transfer/preview_valid
