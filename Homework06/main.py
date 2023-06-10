"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

#Задача 30
a1 = int(input('Input a1: '))
d = int(input('Input d: '))
n = int(input('Input n: '))
array = [a1 + i * d  for i in range(n)]
print(array, '\n')

#Задача 32
min = int(input('Input min: '))
max = int(input('Input max: '))
n = int(input('Input n: '))
valueInRange = []
array = [random.randint(1,100) for a in range(n)]
print(array)
for i in range(len(array)):
    if  min <= array[i] <= max:
        valueInRange.append(i)
print(valueInRange)