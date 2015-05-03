#!/usr/bin/python3
from run.checking import *

def list_all():
    apps=get_all_apps()
    for app in apps:
        print(app)

def list_installed():
    apps=get_all_apps()
    for app in apps:
        if check_installed(app):
            print(app)
