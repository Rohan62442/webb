#!/usr/bin/env python3
from run.checking import *

def list_all():
    #print(*get_all_apps(), sep='\n')
    apps=get_all_apps()
    for app in apps:
        print(app)

def list_installed():
    apps=get_all_apps()
    for app in apps:
        if check_installed(app):
            print(app)
