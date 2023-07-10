'''Хакер Василий получил доступ к классному журналу
и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот:
все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

# n = [1, 3, 3, 3, 4]

import random
n = int(input("Укажите количество оценок Василия: "))
spisok = []
for i in range(n):
    spisok.append(random.randint(1, 5))
print(spisok)

for i in spisok:
    if i == max(spisok):
        spisok[spisok.index(i)] = min(spisok)
print(spisok)