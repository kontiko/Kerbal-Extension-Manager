import sys
import os
import shutil
import json
config = {}
def is_modinstalled(modname):
    if update_config():
        return
    file=open(config["ksppath"]+"kem/installed.txt","r")
    list=[i.replace("\n","") for i in file.readlines()]
    file.close()
    return modname in list
    
    
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
        
        if os.path.isfile(filepath):
            shutil.copyfile(filepath,config["ksppath"]+"kem/"+modname+"/"+filepath.split("/")[-1])
        elif os.path.isdir(filepath):
            shutil.copytree(filepath,config["ksppath"]+"kem/"+modname+"/"+filepath.split("/")[-1])
        else:
            shutil.rmtree(config["ksppath"]+"kem/"+modname+"/")
            print("File/directory '"+filepath+"' not exist end process is aborted")

def remove(modname):
    if update_config():
        return
    if os.path.exists(config["ksppath"]+"kem/"+modname):
        shutil.rmtree(config["ksppath"]+"kem/"+modname)
    else:
        print("Mod is not Available")
    update()

def list():
    if update_config():
        return
    for mod in [f.path for f in os.scandir(config["ksppath"]+"/kem") if f.is_dir()]:
        print(mod.split("/")[-1])
def install(modname):
    if update_config():
        return
    if not (config["ksppath"]+"/kem/"+modname in [f.path for f in os.scandir(config["ksppath"]+"/kem") if f.is_dir()]):
        print("mod not avaialable")
        return
    installlist=open(config["ksppath"]+"/kem/installed.txt","a")
    installlist.write(modname+"\n")
    installlist.close()
    shutil.copytree(config["ksppath"]+"/kem/"+modname,config["ksppath"]+"/GameData/",dirs_exist_ok=True)
def help():
    print("help")
def uninstall(modname):
    if update_config():
        return
    if not is_modinstalled(modname):
        print(modname+" is not installed")
        return
    file=open(config["ksppath"]+"kem/installed.txt","r")
    list=[i.replace("\n","") for i in file.readlines()]
    file.close()
    list.remove(modname)
    print(list)
    os.remove(config["ksppath"]+"kem/installed.txt")
    file=open(config["ksppath"]+"kem/installed.txt","w")
    file.writelines(list)
    file.close()
    
    update()
    
def update():
    dirlist=os.listdir(config["ksppath"]+"/GameData/")
    print(dirlist)
    dirlist.remove("Squad")
    dirlist.remove("SquadExpansion")
    for fdir in dirlist:
        if os.path.isfile(config["ksppath"]+"GameData/"+fdir):
            os.remove(config["ksppath"]+"GameData/"+fdir)
        else:
            shutil.rmtree(config["ksppath"]+"GameData/"+fdir)
    file=open(config["ksppath"]+"kem/installed.txt","r")
    list=[i.replace("\n","") for i in file.readlines()]
    file.close()
    file=open(config["ksppath"]+"kem/installed.txt","w")
    for mod in list:
        if os.path.isdir(config["ksppath"]+"kem/"+mod):
            install(mod)
            file.write(mod+"\n")
    file.close()
    
    
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
elif sys.argv[1]=="install":
    if len(sys.argv)==3:
        install(sys.argv[2])
    else:
        print ("Wrong argument number. Install has <Name of Mod> as argument")
elif sys.argv[1]=="uninstall":
    if len(sys.argv)==3:
        uninstall(sys.argv[2])
    else:
        print ("Wrong argument number. Install has <Name of Mod> as argument")
else:
    print("Unknown command. try <kme help>")

