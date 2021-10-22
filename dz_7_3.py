import os
import shutil

my_path = r'my_project\templates'
for root, dirs, files in os.walk('my_project'):
    if root == my_path:
        break
    for file in files:
        if file.endswith('.html'):
            new_dir = root.split('\\')[-1]
            os.makedirs(os.path.join(my_path, new_dir), exist_ok=True)
            shutil.copyfile(os.path.join(root, file), os.path.join(my_path, os.path.join(new_dir, file)))