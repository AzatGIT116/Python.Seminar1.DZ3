# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
N = int(input('Введите количество чисел: '))
s = [random.randint (0, 15) for _ in range(N)]
print(s)
sum = 0
for i in range(1, len(s), 2):
    sum= sum + s[i]   
print(sum)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
N = int(input('Введите количество чисел: '))
s = [random.randint (0, 15) for _ in range(N)]
print(s)
p_s = []
for i in range(len(s) // 2 + len(s) % 2):
    p_s.append(s[i] * s[len(s) - 1 - i])
print(p_s)


# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


A_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]
B_list = [round(i % 1, 2) for i in A_list if i % 1 != 0]
print(f'Разница между макс и мин значением дробной части элементов = {max(B_list) - min(B_list)}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
print(format(number, 'b'))


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
def f(num):
    fibo = []
    n1 = n2 = 1
    for i in range(num):
        fibo.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for i in range(num+1):
        fibo.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibo
print(f(n))