import os

downloadPath = "C://Users//<youruser>/Downloads" # change youruser with your username or update the directory to a custom one.

dir_list = os.listdir(downloadPath)

for file in dir_list:
    if ".png" or ".jpg" in file:
        print(True)

