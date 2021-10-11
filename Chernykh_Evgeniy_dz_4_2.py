from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

encodings = utils.get_encoding_from_headers(response.headers)
server_date = response.headers['Set-Cookie'].split(',')[1]

content = response.content.decode(encoding=encodings)

content = content.replace('>', ' ')
content = content.replace('<', ' ')
content = content.replace('  ', ' ')

my_list = content.split(' ')

list_valute = []
list_nominal = []
list_value = []

for i, subject in enumerate(my_list):
    if subject == 'CharCode':
        list_valute.append(my_list[i+1])
    elif subject == 'Nominal':
        list_nominal.append(my_list[i+1])
    elif subject == 'Value':
        list_value.append('.'.join(my_list[i+1].split(',')))
# получаем списки с аббревиатурой валюты, номиналом и значениями одинаковой длины

def currency_rates(value):
    if value.upper() in list_valute:
        num = list_valute.index(value.upper())
        print(f'За {list_nominal[num]} {value.upper()} дают {list_value[num]} рублей')
        print(f'Дата сервера: {server_date}')
    else:
        return None

currency_rates(input('Введите название валюты: '))