# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
b=16
i=0
while 2**i<=b:
    print(2**i, end=",")    
    i+=1