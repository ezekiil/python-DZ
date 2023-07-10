'''Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.

Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
'''

import random
n = int(input("Введите число: "))

def reverse(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        list = [random.randint(1, 10) for i in range(n)]
    print(list, end=' ')
    print()
    return list[::-1]
print(reverse(n))