'''Дан список чисел.
Определите, сколько в нем встречается различных чисел.

[1,1,2,0,-1,3,4,4] -> 6
'''

import random
n = int(input('Введите количество чисел: '))
for i in range(n):
    list = [random.randint(1, 10) for i in range(n)]
print(list)
print(len(set(list))) # set - уникальные элементы в списке