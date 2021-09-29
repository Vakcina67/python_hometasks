duration = int(input('Введите время в секундах: '))

if 0 <= duration < 60:
    print('{} сек'.format(duration))
elif 60 <= duration < 3600:
    print('{} мин {} сек'.format(duration // 60, duration % 60))
elif 3600 <= duration < 86400:
    print('{} час {} мин {} сек'.format(duration // 3600, duration % 3600 // 60, duration % 3600 % 60))
elif duration >= 86400:
    print('{} дн {} час {} мин {} сек'.format(duration // 86400, duration % 86400 // 3600,
                                              duration % 86400 % 3600 // 60, duration % 86400 % 3600 % 60))
