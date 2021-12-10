import os

fenrir = "/mnt/d/Tasks/Vistas Situadas - Imagens/20211207FenrirFS_bk"
tmp = "/mnt/c/Users/Pit/Desktop/Nova pasta"
images = "/mnt/d/Tasks/Image classification/images"
pictures = "/mnt/c/Users/Pit/Pictures"


def print_list(folder):
    l = []
    for item in os.listdir(folder):
        l.append(item)
    l = " OR ".join(l)
    print(folder, ": ", l)


# for f in os.listdir(fenrir):
#     print_list(fenrir+"/"+f)


def compare_folder(folderA, folderB):
    folderA_lists = [x.split(".jpg")[0] for x in os.listdir(folderA)]
    folderA_list = [x.replace("_geo", "") for x in folderA_lists]
    print(len(folderA_list))

    folderB_list = [x.split(".jpg")[0] for x in os.listdir(folderB)]

    print(len(folderB_list))
    #i = list(set(folderB_list)-set(folderA_list))

    i = list(set(folderA_list)-set(folderB_list))
    print(len(i))
    i = " ou ".join(i)
    print(i)


compare_folder(fenrir+"/"+"selected", tmp)
#compare_folder(pictures, images)
