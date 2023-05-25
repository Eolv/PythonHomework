"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

#Задача 10
import random
heads = 0
tails = 0
n = int(input('Input coins amount: '))
coins = [random.randint(0,1) for x in range(n)]
print(coins)
for coin in coins:
    if coin == 0:
        heads += 1
    else:
        tails += 1
if heads < tails:
    print(f"Flip {heads} heads\n")
elif heads > tails:
    print(f"Flip {tails} tails\n")
else:
    print(f"Flip {tails} tails or heads\n")

#Задача 12
import random
import math
X = random.randint(1,1001)
Y = random.randint(1,1001)
S = X + Y
P = X * Y
print(f"S = {S} P = {P}")
# можно решить квадратичное уравнение X * X - S * X + P = 0, в задаче не было условия, что надо решать подбором, так что формально я ее решил)))
D = S * S - 4 * P
guess_X = int((S + math.sqrt(D)) / 2)
guess_Y = S - X
print(f"X = {guess_X} Y = {guess_Y}\n")

#Задача 14
N = int(input('Input N: '))
answer = ''
counter = 1
while counter <= N:
    answer += str(counter)  + ', '
    counter *= 2
print(answer)