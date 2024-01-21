import os

print("resource_manifest_version '77731fab-63ca-442c-a67b-abc70f28dfa5'")
print("\n\nfiles {\n")
def print_subfolders(path):
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


path = 'D:\\fivem\\CFXDefault_1BFEF6.base\\resources\\[ unbrand]\\cars\\'
print_subfolders(path)

