"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
"""
import random

#Задача 16
N = int(input('Input array length: '))
array = [random.randint(1,10) for x in range(N)]
print(array)
X = int(input('Input X: '))
counter = 0
for A in array:
    if A == X:
        counter += 1
print(f"Х occurs times: {counter}\n")

#Задача 18
N = int(input('Input array length: '))
array = [random.randint(1,10) for x in range(N)]
print(array)
X = int(input('Input X: '))
closestElement = array[0]
deviation = abs(X - array[0])
for A in array:
    if abs(X - A) < deviation:
        deviation =  abs(X - A)
        closestElement = A
print(f"The value closest in value to X: {closestElement}\n")

#Задача 20
dictionary = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
              'D': 2, 'G': 2,
              'B': 3, 'C': 3, 'M': 3, 'P': 3,
              'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
              'K': 5,
              'J':8, 'X':8,
              'Q': 10, 'Z':10}
inputString = (input('Input the English word: ')).upper()
score = 0
for char in inputString:    
    score += dictionary.get(char, 0)
print(f"Word cost {score} points")