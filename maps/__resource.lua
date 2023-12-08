resource_manifest_version '77731fab-63ca-442c-a67b-abc70f28dfa5'

files {
	'vehicles.meta',
	'carvariations.meta',
	'carcols.meta',
	'handling.meta',
	'dlctext.meta'
	'contentunlocks.meta',
    'vehiclelayouts.meta',
	'shop_vehicle.meta'
}

data_file 'HANDLING_FILE' 'handling.meta'
data_file 'VEHICLE_METADATA_FILE' 'vehicles.meta'
data_file 'CARCOLS_FILE' 'carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'carvariations.meta'
data_file 'DLCTEXT_FILE' 'dlctext.meta'
data_file 'CONTENT_UNLOCKING_META_FILE' 'data/contentunlocks.meta'
data_file 'VEHICLE_LAYOUTS_FILE' 'data/vehiclelayouts.meta'
data_file 'VEHICLE_SHOP_DLC_FILE' 'data/shop_vehicle.meta'

client_script 'vehicle_names.lua'
