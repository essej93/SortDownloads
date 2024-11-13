import os
import shutil

folderPath = "C://Users//<user>/Downloads/" # change youruser with your username or update the directory to a custom one.
folders = ["Images", "Videos", "Documents","Zips", "Executables", "Audio"] # Add or change folder names as you wish but will need to update the sort and move files section

# checks if folders exists, if not creates them
for folder in folders:
    if not os.path.isdir(folderPath + "/" + folder):
        os.makedirs(folderPath + "/" + folder)

dir_list = os.listdir(folderPath)


# create arrays of strings for file types
# can add your own file types to one of the arrays by adding " 'or <.filetype> in f.lower()"
images = [f for f in dir_list if '.jpg' in f.lower() 
          or '.png' in f.lower()
          or '.gif' in f.lower()]

executables = [f for f in dir_list if '.exe' in f.lower()]

videos = [f for f in dir_list if '.mp4' in f.lower() 
          or '.mov' in f.lower() 
          or '.webm' in f.lower()]

documents = [f for f in dir_list if '.doc' in f.lower()
             or '.txt' in f.lower()
             or '.cv' in f.lower()
             or '.pdf' in f.lower()]

zips = [f for f in dir_list if '.zip' in f.lower()
        or '.rar' in f.lower()
        or '.7z' in f.lower()]

audioFiles = [f for f in dir_list if '.mp3' in f.lower()
              or '.wav' in f.lower()]


# SORT AND MOVE FILES
# for loops to sort files
for image in images:
    old_path = folderPath + "/" + image
    new_path = folderPath + "/Images/" + image
    shutil.move(old_path,new_path)

for video in videos:
    old_path = folderPath + "/" + video
    new_path = folderPath + "/Videos/" + video
    shutil.move(old_path,new_path)

for exe in executables:
    old_path = folderPath + "/" + exe
    new_path = folderPath + "/Executables/" + exe
    shutil.move(old_path,new_path)

for doc in documents:
    old_path = folderPath + "/" + doc
    new_path = folderPath + "/Documents/" + doc
    shutil.move(old_path,new_path)
    
for zip in zips:
    old_path = folderPath + "/" + zip
    new_path = folderPath + "/Zips/" + zip
    shutil.move(old_path,new_path)

for audio in audioFiles:
    old_path = folderPath + "/" + audio
    new_path = folderPath + "/Audio/" + audio
    shutil.move(old_path,new_path)



