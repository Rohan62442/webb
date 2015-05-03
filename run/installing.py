#!/usr/bin/python3
from run.checking import *

def install_all():
    apps=get_all_apps()
    for app in apps:
        install(app)

def install(app_str):
    import shutil
    app=load_json(app_str)
    app_dir=webb_dir+"app-epiphany-"+app['name']+"-"+app['profile']
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    desk_file=app_dir+"/epiphany-"+app['name']+"-"+app['profile']+".desktop"
    with open(desk_file, 'w') as laun:
        laun.write("#!/usr/bin/env xdg-open\n\n[Desktop Entry]\n")
        laun.write("Name="+app['label']+"\n")
        laun.write("Icon="+app_dir+"/"+app['icon']+"\n")
        laun.write("Comment="+app['comment']+"\n")
        laun.write("Exec=epiphany --application-mode --profile=\""+app_dir+"\" "+app['url']+"\n")
        laun.write("StartupNotify=true\nTerminal=false\nType=Application\n")
        laun.write("StartupWMClass=epiphany-"+app['name']+"-"+app['profile']+"\n")
    shutil.copy(desk_file, local_path)
    shutil.copy('cookies.sqlite', app_dir)
    shutil.copy("icons/"+app['icon'], app_dir)
    print(app['label']+" installed successfully.")
