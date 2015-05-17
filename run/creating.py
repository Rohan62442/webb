#!/usr/bin/env python3
from run.checking import *
from run.installing import *

def get_hash(name):
    import hashlib
    return hashlib.sha1(name.encode('utf-8')).hexdigest()

def get_json(name, label, sha, url):
    import json
    return json.dumps({"name": name,"label": label,"icon": "default.svg","comment": "","url": url,"profile": sha})

def create_new(label, url):
    name=label.lower().strip().replace(" ", "-")
    if name in get_all_apps():
        print(label+" is already available.")
        return
    with open("apps/"+name+".json", 'w') as f:
        f.write(get_json(name, label, get_hash(label), url))
    install(name)
