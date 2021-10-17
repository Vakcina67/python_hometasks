from collections import Counter
my_list = []
list_ip = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_2 = line.replace(' - - ', '"').split('"')
        my_list.append((line_2[0], line_2[2].split(' ')[0], line_2[2].split(' ')[1]))
        list_ip.append(line_2[0])

print(*my_list, sep=',\n')

dict_ip = Counter(list_ip)
spam = dict_ip.most_common(1)
print(f'ip спамера: {spam[0][0]}, количество запросов: {spam[0][1]}')
print(dict_ip)


