prices = [57.8, 46.51, 97, 33.35, 105.3, 25.98, 188, 45.69, 86.77, 72.04, 79.09]

for i in prices:
    print(f'{int(i)} руб {int(i * 100 % 100):02d} коп', end=', ')

print(f'\n\nid списка до сортировки: {id(prices)}')
print('Цены после сортировки:')
prices.sort()
print(prices)
print(f'id списка после сортировки: {id(prices)}')

new_prices = prices[:]
new_prices.reverse()
print('\nЦены по убыванию: ')
print(new_prices)
print(f'id нового списка: {id(new_prices)}')

print('\nЦены 5 самих дорогих товаров:')
print(prices[-5:])
