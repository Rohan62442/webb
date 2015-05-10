#!/usr/bin/python3
from run.checking import *
from run.installing import *

def get_hash(name):
    import hashlib
    return hashlib.sha1(name.encode('utf-8')).hexdigest()

def get_json(name, sha, url):
    import json
    return json.dumps({"name": name.lower(),"label": name,"icon": "default.svg","comment": "","url": url,"profile": sha})

def create_new(name, url):
    import os
    sha=get_hash(name)
    js=get_json(name, sha, url)
    with open("apps/"+name.lower()+".json", 'w') as f:
        f.write(js)
    install(name.lower())
