# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X

# *Пример:*

# 5
#     7 -2 3 5 1
#     6
#     -> 7
import random
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число для поиска: "))
list_1 = [random.randint(0, 10) for i in range(n)]
differense = abs(x-list_1[0])
number_next = list_1[0]
for _ in list_1:
    if abs(_-x) < differense:
        number_next = _
        differense = abs(_-x)
print(f"В массиве {list_1} самый близкий по величине элемент к заданному числу {x} будет {number_next}")