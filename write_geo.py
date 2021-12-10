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
images = "/mnt/d/Tasks/Image classification/images"
current_features = (geojson.load(
    open("/mnt/d/situated-views-etl/data/output/import_viewcones.geojson"))).features
pictures = "/mnt/c/Users/Pit/Pictures"
metadata = metadata.loc[metadata["Source"] == "Instituto Moreira Salles"]
df_geo = metadata.loc[metadata["Latitude"].notna()]
ids_geo = (df_geo["Source ID"]).to_list()
ids_tags = {x: ["geo"] for x in ids_geo}

features = [x.properties["Source ID"]
            for x in current_features if x.properties["Source"] == "Instituto Moreira Salles"]
print(len(features))


def add_tag(folder, items_list, tag_list):
    """ Add tag by given list with relatioship between item and tags"""
    geo = []
    for img in tqdm(os.listdir(folder)):
        for item in items_list:
            if img.endswith(item.upper()+".jpg") or img.endswith(item + ".jpg"):
                path_from = folder+"/"+img
                path_to = path_from.split(".jpg")[0]+"_geo.jpg"
                os.rename(path_from, path_to)
                # path = folder+"/"+img
                # info = IPTCInfo(path)
                # for tag in tag_list:
                #     if tag.encode('UTF-8') not in info['keywords']:
                #         info['keywords'].append(tag)

                # info.save()
                # info.save_as(path)
                # geo.append(item)
            # else:
            #     out.append(id)

    return geo


g = add_tag(images, ids_geo, ["geo"])
print(len(g))
# print(" OR ".join(list(set(ids_geo) - set(g))))
# #not_ = add_tag(pictures, ids_tags)
# # print(not_)
# # update_tag(pictures,tags)
