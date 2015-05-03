#!/usr/bin/python3
import os

home_dir=os.getenv('HOME')
webb_dir=home_dir+"/.config/epiphany/"
local_path=home_dir+"/.local/share/applications"

def load_json(app_str):
    import json, sys
    try:
        with open("apps/"+app_str+".json") as app_file:
            return json.loads(app_file.read().replace("\n",""))
    except FileNotFoundError:
        sys.exit("Error: This web app is not available.")

def get_all_apps():
    all_apps=os.listdir("apps")
    all_apps.remove("README.md")
    for i in range(0, len(all_apps)):
        all_apps[i]=all_apps[i].replace(".json","")
    return all_apps

def check_installed(app_str):
    app=load_json(app_str)
    if os.path.exists(webb_dir+"app-epiphany-"+app['name']+"-"+app['profile']+"/epiphany-"+app['name']+"-"+app['profile']+".desktop"):
        return True
    return False
