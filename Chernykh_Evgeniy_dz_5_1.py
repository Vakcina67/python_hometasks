def odd_to_nums(max_n):
    for num in range(1, max_n + 1, 2):
        yield num

odd_to_15 = odd_to_nums(15)
print(sum(odd_to_15))
print(sum(odd_to_15)) # должно быть 0

n = int(input('Введите число: '))
nums_gen = (num for num in range(1, n + 1, 2))

print(sum(nums_gen))
print(sum(nums_gen)) # должно быть 0