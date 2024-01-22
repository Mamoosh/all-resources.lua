import os

path = 'C:\\fivem\\CFXDefault_1BFEF6.base\\resources\\[ unbrand]\\cars\\'
lua_file_path = 'C:\\__resource.lua'


def print_ssubfolders(path):
    output = ""
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            stream = (os.path.join(root, name)).replace(path, '') + '\\'
            stream = stream.replace("\\", "/")
            output += "'" + stream + 'vehicles.meta' + "',\n"
            output += "'" + stream + 'carvariations.meta' + "',\n"
            output += "'" + stream + 'carcols.meta' + "',\n"
            output += "'" + stream + 'handling.meta' + "',\n"
            output += "'" + stream + 'dlctext.meta' + "',\n"
            output += "'" + stream + 'contentunlocks.meta' + "',\n"
            output += "'" + stream + 'vehiclelayouts.meta' + "',\n"
            output += "'" + stream + 'shop_vehicle.meta' + "',\n\n"

    with open(lua_file_path, 'w') as lua_file:
        lua_file.write("resource_manifest_version '77731fab-63ca-442c-a67b-abc70f28dfa5'\n\nfiles {\n")
        lua_file.write(output)
        lua_file.write("}\n")


def print_subfolders(path):
    output = ""
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            stream = (os.path.join(root, name)).replace(path, '') + '\\'
            stream = stream.replace("\\", "/")
            output += "data_file 'HANDLING_FILE' '" + stream + "handling.meta'\n"
            output += "data_file 'VEHICLE_METADATA_FILE' '" + stream + "vehicles.meta'\n"
            output += "data_file 'CARCOLS_FILE' '" + stream + "carcols.meta'\n"
            output += "data_file 'VEHICLE_VARIATION_FILE' '" + stream + "carvariations.meta'\n"
            output += "data_file 'DLCTEXT_FILE' '" + stream + "dlctext.meta'\n"
            output += "data_file 'CONTENT_UNLOCKING_META_FILE' '" + stream + "contentunlocks.meta'\n"
            output += "data_file 'VEHICLE_LAYOUTS_FILE' '" + stream + "vehiclelayouts.meta'\n"
            output += "data_file 'VEHICLE_SHOP_DLC_FILE' '" + stream + "shop_vehicle.meta'\n\n"

    with open(lua_file_path, 'a') as lua_file:
        lua_file.write(output)


print_ssubfolders(path)
print_subfolders(path)
