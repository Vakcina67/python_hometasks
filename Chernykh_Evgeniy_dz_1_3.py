for i in range(1, 101):
    if i not in [11, 12, 13, 14] and i % 10 in [2, 3, 4]:
        print('{} процента'.format(i))
    elif i != 11 and i % 10 == 1:
        print('{} процент'.format(i))
    else:
        print('{} процентов'.format(i))
