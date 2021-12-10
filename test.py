import os
import re

from iptcinfo3 import IPTCInfo
from PIL.ExifTags import TAGS
from tqdm import tqdm


path = "/mnt/c/Users/Pit/Pictures/aebf-4_31.0_007CX184-07.jpg"
info = IPTCInfo(path)
for key in info['keywords']:
    i = key
    if i.encode('UTF-8') in info['keywords']:
        print(key)
b'dgbfndghn' != 'dgbfndghn'