import os

main_dir = 'my_project'
subfolders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in subfolders:
    os.makedirs(os.path.join(os.curdir, main_dir, folder), exist_ok=True)