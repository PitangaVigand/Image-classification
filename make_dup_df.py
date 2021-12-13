import os
from iptcinfo3 import IPTCInfo
import pandas as pd
import re
from tqdm import tqdm

images = "/mnt/d/Tasks/Image classification/images"
file = "/mnt/d/Tasks/Image classification/images/aaaa-0_0.0_001AAN005121.jpg"
# if b'geo' in IPTCInfo(file)['keywords']:
#     print("ok")
# else:
#     print("no")
# # print(IPTCInfo(file)['keywords'])


def find_dups_bymeta(folder):
    folder_list = [x.replace(".jpg", "")
                   for x in os.listdir(folder) if x.endswith(".jpg")]
    dup = []
    dups = {}
    for img in tqdm(folder_list):
        #img = img.replace(".jpg", "")
        # print(img)
        info = IPTCInfo(folder+"/"+img+".jpg")
        if b"dup" in info['keywords']:
            dup.append(img)
    for item in tqdm(dup):
        info = IPTCInfo(folder+"/"+item+".jpg")
        if b'master' in info["keywords"]:
            code = item.split("-")[0]
            matching = [s for s in dup if code in s]
            dups[item] = " | ".join(matching)
    return dups


df = pd.DataFrame.from_dict(find_dups_bymeta(
    images), orient="index")
dups = find_dups_bymeta(images)
df.to_csv("/mnt/d/Tasks/Image classification/duplicates.csv")
# print(dups)
