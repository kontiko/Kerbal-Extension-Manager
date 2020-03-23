import sys
import os
import shutil
def add(filepaths):
    try:
        configfile=open(os.path.dirname(__file__)+"/configs.json")
    except:
        print("can't open Config file")
        return
    f=open(filepath,"r")
    print(f.readlines())

def help():
    print("help")

if sys.argv[1]=="help":
    help()
elif sys.argv[1]=="add":
    read(sys.argv[2:])
else:
    print("Unknown command. try <kme help>")
