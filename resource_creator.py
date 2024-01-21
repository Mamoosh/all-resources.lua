import os

print("resource_manifest_version '77731fab-63ca-442c-a67b-abc70f28dfa5'")
print("\n\nfiles {\n")
def print_ssubfolders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            stream  = (os.path.join(root, name)).replace(path, '') + '\\'
            stream = stream.replace("\\" , "/")
            print("'" + stream + 'vehicles.meta' + "',")
            print("'" + stream + 'carvariations.meta' + "',")
            print("'" + stream + 'carcols.meta' + "',")
            print("'" + stream + 'handling.meta' + "',")
            print("'" + stream + 'dlctext.meta' + "',")
            print("'" + stream + 'contentunlocks.meta' + "',")
            print("'" + stream + 'vehiclelayouts.meta' + "',")
            print("'" + stream + 'shop_vehicle.meta' + "',")
            print("\n")

print("}\n")

def print_subfolders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            stream  = (os.path.join(root, name)).replace(path, '') + '\\'
            stream = stream.replace("\\" , "/")
            print("data_file 'HANDLING_FILE' '" + stream + "handling.meta'")
            print("data_file 'VEHICLE_METADATA_FILE' '" + stream + "vehicles.meta'")
            print("data_file 'CARCOLS_FILE' '" + stream + "carcols.meta'")
            print("data_file 'VEHICLE_VARIATION_FILE' '" + stream + "carvariations.meta'")
            print("data_file 'DLCTEXT_FILE' '" + stream + "dlctext.meta'")
            print("data_file 'CONTENT_UNLOCKING_META_FILE' '" + stream + "contentunlocks.meta'")
            print("data_file 'VEHICLE_LAYOUTS_FILE' '" + stream + "vehiclelayouts.meta'")
            print("data_file 'VEHICLE_SHOP_DLC_FILE' '" + stream + "shop_vehicle.meta'")
            print("\n")



path = 'D:\\fivem\\CFXDefault_1BFEF6.base\\resources\\[ unbrand]\\cars\\'
print_ssubfolders(path)
print_subfolders(path)

