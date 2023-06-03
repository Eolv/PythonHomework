"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""

#Задача 26
a = int(input('Input a: '))
b = int(input('Input b: '))
def RecursivePower(a, b):
        if b >= 1:
            return a * RecursivePower(a, b - 1)
        elif b == 0:
              return 1
        else:
              print('Error')
print(f"a to the power of b = {RecursivePower(a, b)}\n")

#Задача 28
a = int(input('Input a: '))
b = int(input('Input b: '))
def RecursiveSum(a, b):
    if a == 0:
          if b == 0:
               return 0
          else:
            return 1 + RecursiveSum(a, b - 1)      
    else:
          return 1 + RecursiveSum(a - 1, b)
print(f"a + b = {RecursiveSum(a, b)}")