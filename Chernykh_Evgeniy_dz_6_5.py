import sys

users, hobby, users_hobby = sys.argv[1:]

if __name__ == '__main__':
    from itertools import zip_longest
    with open(users, 'r', encoding='utf-8') as f_1, open(hobby, 'r', encoding='utf-8') as f_2:
        names = f_1.read().splitlines()
        hobbies = f_2.read().splitlines()

    gen_hobbies = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies, fillvalue=None))

    with open(users_hobby, 'w', encoding='utf-8') as f:
        for line in gen_hobbies:
            f.write(f'{line[0]}: {line[1]}\n')
    exit()
