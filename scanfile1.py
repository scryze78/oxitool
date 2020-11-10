import os
import time

start_time = time.time()
PATH="C:\\"
a=0
def recherche(path):
    try:
        dirList= os.listdir(path)
        for fname in dirList:
            #    print(fname)
            chemin=path+"\\"+fname
            if os.path.isfile(chemin):
                print(fname, os.path.getsize(chemin))
            #        envoyer(fname, os.path.getsize(chemin))
            elif os.path.isdir(chemin):
                recherche(chemin)
    except PermissionError:
        pass


recherche(PATH)
print("--- %s seconds ---" % (time.time() - start_time))
#b= os.path.getsize("/path/isa_005.mp3")

#ext = os.path.splitext(file_name)[1]
