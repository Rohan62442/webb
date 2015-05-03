#!/usr/bin/python3
from run.checking import *

def remove_all():
    apps=get_all_apps()
    for app in apps:
        if check_installed(app):
            remove(app)

def remove(app_str):
    import shutil
    app=load_json(app_str)
    app_dir=webb_dir+"app-epiphany-"+app['name']+"-"+app['profile']
    if not check_installed(app_str):
        print(app['label']+" is not installed.")
    else:
        shutil.rmtree(app_dir)
        os.remove(local_path+"/epiphany-"+app['name']+"-"+app['profile']+".desktop")
        print(app['label']+" removed successfully.")
