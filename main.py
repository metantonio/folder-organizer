import os
import shutil



#specific directory to work without beeing there
sourcepath='D:\Descargas'
#parent directory
os.chdir(sourcepath)
#print(os.getcwd())
##check number of files in  directory
#files = os.listdir()
sourcefiles = os.listdir(sourcepath)
name=""

##list of extension
extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv", ".avi", ".flv", ".mov"],
    "musics": [".mp3", ".wav", ".aac"],
    "zip": [".zip", ".tgz", ".rar", ".tar", ".7z"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls", ".xml", ".xlsm"],
    "setup": [".msi", ".exe", ".EXE"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"],
    "sketchup": [".skp", ".skb"],
    "apk": [".apk", ".APK"],
    "html":[".html", ".HTML"],
    "others":["."],
    "batchs":[".bat"]


}


#sort to specific folder depend on extenstions
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            # print(ext)
            if file.endswith(ext):
                return key

#creating folder
def folders():
    folderList = list(extentions.keys())
    if os.path.isdir("others"):
        print("already exist folder others!")
    else:
        os.mkdir("others")
    for folder in folderList:
        path = os.path.join(sourcepath, folder)
        if os.path.isdir(folder):
            print("exist already: ",folder)
        else:
            os.mkdir(folder)
    return print("Folders Created")

#iterat through each file
folders()
folderList = list(extentions.keys())
for file in sourcefiles:
    for i in folderList:
        if i == file:
            name=file
            print("folder name: ",name)
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "./" + dist)
        except:
            print(file + " is already exist")
    else:
        print("File or Directory moved: ",file)
        try:
            if file is not name:
                shutil.move(file, "./others")
        except:
            print(file + " is already exist in directory")
