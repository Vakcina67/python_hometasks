
def thesaurus(*args):
    dict_1 = {}
    list_1 = list(sorted(args))
    for name in list_1:
        first_letter = name[0]
        dict_1[first_letter] = dict_1.get(first_letter, []) + [name]
    return print(dict_1)

thesaurus("Иван", "Мария", "Петр", "Илья")

def thesaurus_adv(*args):
    list_1 = list(args)
    dict_surnames = {}
    dict_end = {}
    for fullname in list_1:
        surname = fullname.split(' ')[-1]
        first_letter_surname = surname[0]
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [fullname]
    for namelist in dict_surnames.values():
        dict_names = {}
        for name in namelist:
            surname = name.split(' ')[-1]
            first_letter_surname = surname[0]
            first_letter = name[0]
            dict_names[first_letter] = sorted(dict_names.get(first_letter, []) + [name])
            dict_end[first_letter_surname] = dict_end.get(first_letter_surname, dict_names)
    return print(dict_end)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")