import os

folderPath = "C://Users//Jesse/Downloads/TestDownload" # change youruser with your username or update the directory to a custom one.
folders = ["Images", "Videos", "Documents","Zips", "Executables"] # Add or change folder names as you wish

# checks if folders exists, if not creates them
for folder in folders:
    if not os.path.isdir(folderPath + "/" + folder):
        os.makedirs(folderPath + "/" + folder)



# dir_list = os.listdir(downloadPath)


# for file in dir_list:
#     if ".png" or ".jpg" in file:
#         print(True)

