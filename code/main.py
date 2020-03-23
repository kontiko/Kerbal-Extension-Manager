import sys
import os
import shutil
import json
def add(data):
    modname=data[0]
    filepaths=data[1:]
    try:
        if os.path.dirname(__file__)=="":
            with open('config.json') as json_data_file:
                config = json.load(json_data_file)
        else:
            with open(os.path.dirname(__file__)+'/config.json') as json_data_file:
                config = json.load(json_data_file)
        
        
    except:
        print("can't open Config file")
        return
    if os.path.exists(config["ksppath"]+"kem/"+modname+"/"):
        print("Mod with these name already exists")
        return
    os.makedirs(config["ksppath"]+"kem/"+modname+"/", exist_ok = True)
    for filepath in filepaths:
        print(filepath)
        shutil.copyfile(filepath,config["ksppath"]+"kem/"+modname+"/"+filepath.split("/")[-1])

def help():
    print("help")

if sys.argv[1]=="help":
    help()
elif sys.argv[1]=="add":
    add(sys.argv[2:])
else:
    print("Unknown command. try <kme help>")
