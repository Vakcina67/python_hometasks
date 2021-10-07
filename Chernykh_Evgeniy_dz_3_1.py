numbers = {'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}

def num_translate(num):
    print(numbers.get(num.lower()))

num_translate('three')


def num_translate_adv(num):
    for key in numbers:
        if key.capitalize() == num:
            print(numbers[key].capitalize())
            break
    else:
        return print(numbers.get(num))

num_translate_adv('Eight')
