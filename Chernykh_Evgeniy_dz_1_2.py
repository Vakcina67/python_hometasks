odd_list = []
for i in range(1, 1001, 2):
    odd_list.append(i ** 3)

sum_of_numbers_1 = 0

for number in odd_list:
    sum_of_digits = 0
    n = number
    while n:
        digit = n % 10
        sum_of_digits += digit
        n = n // 10
    if sum_of_digits % 7 == 0:
        sum_of_numbers_1 += number
print(sum_of_numbers_1)

sum_of_numbers_2 = 0

for number in odd_list:
    sum_of_digits = 0
    n = number + 17
    while n:
        digit = n % 10
        sum_of_digits += digit
        n = n // 10
    if sum_of_digits % 7 == 0:
        sum_of_numbers_2 += number + 17
print(sum_of_numbers_2)
