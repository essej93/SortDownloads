import os

downloadPath = "C://Users//Jesse/Downloads/TestDownload"

dir_list = os.listdir(downloadPath)

for file in dir_list:
    if ".png" or ".jpg" in file:
        print(True)

