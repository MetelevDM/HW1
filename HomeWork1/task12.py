# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

a=360
b=66
for i in range(b//2+1):
    for j in range(a):
        if i*j==a and i+j==b:
            print (i, j)     
        