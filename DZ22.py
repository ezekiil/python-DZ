'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
'''

# a = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# b = {3, 6, 9, 12, 15, 18}

import random
n = int(input('введите кол-во элементов первого множества: '))
m = int(input('введите кол-во элементов второго множества: '))
a = {random.randint(1, 10) for i in range(n)}
b = {random.randint(1, 10) for i in range(m)}
print (a)
print (b)

c = sorted(a.intersection(b))
print(f'повторяющиеся элементы: {c}')