import os

with open('config.yaml', 'r', encoding='utf-8') as f:
    lines = dict(map(str.split, f.readlines()))

main_dir = lines.pop('main')
print(main_dir)

for key, value in lines.items():
    os.makedirs(os.path.join(os.curdir, main_dir, key), exist_ok=True)

    for file in value.split(','):
        with open(os.path.join(os.curdir, main_dir, key, file), 'w') as f:
            pass