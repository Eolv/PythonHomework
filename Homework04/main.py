"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random

#Задача 22
#arr_1 = set(random.randint(1,10) for x in range(20))
arr_1 = set(int(a) for a in input('Input array 1: ').split())

#arr_2 = set(random.randint(1,15) for x in range(15))
arr_2 = set(int(a) for a in input('Input array 2: ').split())

arr_3 = list(arr_1.intersection(arr_2))
arr_3.sort()

print(f"Array 1 unique elements: {arr_1}")
print(f"Array 2 unique elements: {arr_2}")
print(f"Ascending intersection: {arr_3}\n")

#Задача 24
N = int(input('Input N: '))
bushes = [random.randint(1,100) for a in range(N)]
bushes.append(bushes[0])
print(bushes)
max = 0
for i in range(1, N):
    if (bushes[i-1]+bushes[i]+bushes[i+1]) > max:
        max = bushes[i-1]+bushes[i]+bushes[i+1]
print('Max berries to be collected: ', max)
    
