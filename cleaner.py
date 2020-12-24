import os
def createIfNotExist(folders):
    if not os.path.exists(folders):
        os.makedirs(folders)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{files}")

files= os.listdir()
files.remove("cleaner.py")
print(files)
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Apps')
createIfNotExist('Others')

docExt=[".txt",".pdf",".doc",".docx"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docExt]
print(docs)

imgExt =[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExt]
print(images)

appExt =[".dmg"]
apps=[file for file in files if os.path.splitext(file)[1].lower() in appExt]
print(apps)
others=[]
for file in files:
    ext= os.path.splitext(file)[1].lower()
    if(ext not in appExt) and (ext not in docExt) and (ext not in imgExt) and os.path.isfile(file):
        others.append(file)
move("Images",images)
move("Apps",apps)
move("Docs",docs)
move("Others",others)

