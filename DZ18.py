'''Требуется найти в массиве A[1..N] самый близкий повеличине элемент к заданному числу X.
Пользователь в первой строкевводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X

5
1 2 3 4 5
6

-> 5
'''

import random
n = int(input('укажите количество элементов в массиве: '))
items = [] # генерируем список случайных чисел
for i in range(n):
    items.append(random.randint(1, 10))
value = int(input('задайте число: ')) # вводим число
def nearest_value(items, value): # функция нахождения ближайшего значения
    found = items[0] # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
    for item in items: # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
        # проверяем условие если разница между item value по модулю меньше разницы found и value, то
        if abs(item - value) < abs(found - value): # если условие истинно (True)
            found = item # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
    return found # возвращаем ближайшее значение до value в списке items
 
print(f'Ближайшее число к {value} в списке {items} является {nearest_value(items, value)}')

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)