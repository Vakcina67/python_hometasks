from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as f_1, open('hobby.csv', 'r', encoding='utf-8') as f_2:
    names = f_1.read().splitlines()
    hobby = f_2.read().splitlines()

users_hobby = ((names, hobby) for names, hobby in zip_longest(names, hobby, fillvalue=None))

with open('users_hobby(4).txt', 'w', encoding='utf-8') as f:
    for line in users_hobby:
        f.write(f'{line[0]}: {line[1]}\n')
