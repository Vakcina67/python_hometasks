from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as f_1, open('hobby.csv', 'r', encoding='utf-8') as f_2:
    names = f_1.read().splitlines()
    hobby = f_2.read().splitlines()

if len(names) < len(hobby):
    print(1)
else:
    users_hobby = dict(zip_longest(names, hobby, fillvalue=None))
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        json.dump(users_hobby, f)
