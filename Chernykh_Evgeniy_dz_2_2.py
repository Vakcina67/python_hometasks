list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(list_1)

for element in list_1:
    if element[-1].isdigit():
        list_1.insert(list_1.index(element) + 1, '"')
list_1.reverse()

for element in list_1:
    if element[-1].isdigit():
        list_1.insert(list_1.index(element) + 1, '"')
list_1.reverse() # получили исходный список, дополненный кавычками
print(list_1)

for element in list_1:
    if element[-1].isdigit() and len(element) == 1:
        num_element = list_1.index(element)
        new_element = '0' + element
        list_1.pop(num_element)
        list_1.insert(num_element, new_element)
    elif element[-1].isdigit() and element[0] in '+-':
        num_element = list_1.index(element)
        new_element = element[0] + '0' + element[-1]
        list_1.pop(num_element)
        list_1.insert(num_element, new_element)
list_1 = ' '.join(list_1)
print(list_1)
