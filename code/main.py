import sys
import os
import shutil
import json
config = {}
def update_config():
    global config
    try:
        if os.path.dirname(__file__)=="":
            with open('config.json') as json_data_file:
                config = json.load(json_data_file)
        else:
            with open(os.path.dirname(__file__)+'/config.json') as json_data_file:
                config = json.load(json_data_file)
        return False
        
    except:
        print("can't open Config file")
        return True
def add(data):
    if update_config():
        return
    modname=data[0]
    filepaths=data[1:]
    if os.path.exists(config["ksppath"]+"kem/"+modname+"/"):
        print("Mod with these name already exists")
        return
    os.makedirs(config["ksppath"]+"kem/"+modname+"/", exist_ok = True)
    for filepath in filepaths:
        print(filepath)
        shutil.copyfile(filepath,config["ksppath"]+"kem/"+modname+"/"+filepath.split("/")[-1])
def remove(modname):
    if update_config():
        return
    if os.path.exists(config["ksppath"]+"kem/"+modname+"/"):
        shutil.rmtree(config["ksppath"]+"kem/"+modname+"/")
    else:
        print(Mod is not Available)
def list():
    if update_config():
        return
    for mod in [x[0] for x in os.walk(config["ksppath"]+"kem/")][1:]:
        print(mod.split("/")[-1])
def help():
    print("help")

if sys.argv[1]=="help":
    help()
elif sys.argv[1]=="add":
    add(sys.argv[2:])
elif sys.argv[1]=="remove":
    if len(sys.argv)==3:
        remove(sys.argv[2])
    else:
        print ("Wrong argument number. Remove has <Name of Mod> as argument")
elif sys.argv[1]=="list":
    list()
else:
    print("Unknown command. try <kme help>")
