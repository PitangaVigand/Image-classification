import os
from posix import listdir
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import re
from tqdm import tqdm
import pandas as pd
import geojson


from iptcinfo3 import IPTCInfo

metadata = pd.read_csv("/mnt/d/situated-views-etl/data/output/metadata.csv")
# current_features = (geojson.load(
#     open("/mnt/d/situated-views-etl/data/output/import_viewcones.geojson"))).features
pictures = "/mnt/c/Users/Pit/Pictures"
metadata = metadata.loc[metadata["Source"] == "Instituto Moreira Salles"]
df_geo = metadata.loc[metadata["Latitude"].notna()]
ids_geo = (df_geo["Source ID"]).to_list()
ids_tags = {x: ["geo"] for x in ids_geo}
# print(ids_tags)

# folder_list = [(re.search(r"\.0_(.*).jpg", x)).group(1)
#                for x in os.listdir(pictures) if x.endswith(".jpg")]

# list_folder = [x.split("_geo")[0] if x.endswith("_geo") else x
#                for x in folder_list]


def add_tag(folder, list_ids, tag):
    geo = []
    out = []
    # folder_list = [x.split(".jpg")[0] if not x.endswith(
    #     "_geo.jpg") else x.split("_geo.jpg")[0] for x in os.listdir(folder)]

    for img in os.listdir(folder):
        for id in list_ids:
            if img.endswith(id.upper()+".jpg") or img.endswith(id + ".jpg"):
                geo.append(id)
            # else:
            #     out.append(id)

    return geo
# print(ids_folder)
    # for identifier in list_ids:

    #     if name.endswith("_geo"):
    #         name = name.split("_geo.jpg")[0]


print(len(ids_geo))
g = add_tag(pictures, ids_geo, "geo")
print(len(g))
print(" OR ".join(list(set(ids_geo) - set(g))))
#not_ = add_tag(pictures, ids_tags)
# print(not_)
# update_tag(pictures,tags)
