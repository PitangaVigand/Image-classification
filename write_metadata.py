import os
import re

from iptcinfo3 import IPTCInfo
from PIL.ExifTags import TAGS
from tqdm import tqdm


fenrir = "/mnt/d/Tasks/Vistas Situadas - Imagens/20211207FenrirFS_bk"
images = "/mnt/d/Tasks/Image classification/images"
pictures = "/mnt/c/Users/Pit/Pictures"


def tags_by_folder(folder):
    tags = {}
    for folder_tag in tqdm(os.listdir(folder)):
        for img in os.listdir(folder+"/" + folder_tag):
            #name = (re.search(r"\.0_(.*).jpg", img)).group(1)
            name = img
            if name.endswith("_geo"):
                name = name.split("_geo")[0]
            try:
                if name not in tags:
                    tags[name] = [folder_tag]
                else:
                    tags[name].extend([folder_tag])
            except Exception as e:
                print(e)
    return tags


def add_folder_tag(folder, tag_dict):
    """ Add tag by given dictionary with relatioship between item and tags"""
    without_tag = []
    for img in tqdm(os.listdir(folder)):
        if img.endswith(".jpg"):
            name = img
            # if name.endswith("_geo"):
            #     name = name.split("_geo.jpg")[0]
            #name = (img.replace(img.split("_")[0]+"_", "")).replace(".jpg", "")
            if name in tag_dict:
                path = folder+"/"+img
                info = IPTCInfo(path)
                for key in tag_dict[name]:
                    if key.encode('UTF-8') not in info['keywords']:
                        info['keywords'].append(key)

                info.save()
                info.save_as(path)
            else:
                if not name.endswith("_geo"):
                    without_tag.append(img)
    return without_tag


keys = tags_by_folder(fenrir)
without_tag = add_folder_tag(images, keys)
print(without_tag)
