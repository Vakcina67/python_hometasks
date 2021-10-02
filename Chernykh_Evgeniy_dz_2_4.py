list_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element in list_names:
    name = element.split(' ')
    print(f'Привет, {name[-1].capitalize()}!')
