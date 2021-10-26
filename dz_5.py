import os
import json

my_list = []
for root, dirs, files in os.walk(os.curdir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        my_list.append(file_size)
max_size = max(my_list)
ext_list = []
my_dict = {}
i = 0
while max_size > 0:
    for root, dirs, files in os.walk(os.curdir):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            if max_size // 10 < file_size <= max_size:
                ext = file.rsplit('.')[-1]
                ext_list.append(ext)
                i += 1
    my_set = set(ext_list)
    ext_list_2 = list(my_set)
    my_dict.setdefault(max_size, (i, ext_list_2))
    i = 0
    ext_list.clear()
    max_size = max_size // 10

with open('file_size_dict.json', 'w') as f:
    json.dump(my_dict, f)
with open('file_size_dict.json', 'r') as f:
    print(json.load(f))

