# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
countCoin = count = 7
eagle = 0
while countCoin > 0:
    coint = random.randint(0, 1)
    if coint == 0:
        eagle += 1
    print(coint, end=" ")
    countCoin -= 1
if count / 2 <= eagle:
    print("\n", count-eagle)
else:
    print("\n", eagle)
