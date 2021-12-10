import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import re

images = "/mnt/d/Tasks/Image classification/images"
fenrir = "/mnt/e/Tasks/Vistas Situadas - Imagens/20211207FenrirFS_bk"
pictures = "/mnt/c/Users/Pit/Pictures"


def clean_name(folder):
    for img in os.listdir(folder):
        if img.endswith(".jpg"):
            name = img.replace("_geo", "")
            code = img.split("-")[0]
            name = "_".join(name.split("_")[2:])
            print(folder+"/" + img, folder+"/" + code + "_"+name)
            os.rename(folder+"/" + img, folder+"/" + code + "_"+name)


# clean_name(pictures)


def clean_geo_name(folder):
    for img in os.listdir(folder):
        if img.endswith(".jpg"):
            name = img.replace("_geo", "")
            print(folder+"/" + img, folder+"/" + name)
            os.rename(folder+"/" + img, folder+"/" + name)


clean_geo_name(images)
