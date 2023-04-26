# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
count = int(input("Введите размер массива: "))
min_number = int(input("Введите минимальное значение диапазона: "))
max_number = int(input("Введите максимальное значение диапазона: "))
list_1 = [random.randint(1, 20) for i in range(count)]
print(list_1)
for i in range(len(list_1)):
    if min_number < list_1[i] < max_number:
        print(list_1[i], end=",")
