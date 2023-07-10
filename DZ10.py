""" На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

5 -> 1 0 1 1 0
2
"""
import random # для генерации случайных чисел
N = int(input('Введите количество монет: '))
orel = reshka = 0
for i in range(N): # перебор
    # x = int(input('Орел(1) или решка(0)? '))
    x = random.randint(0, 1) # генерация случайного числа в диапазоне [0, 1]
    print(x, end=' ') # вывод результата в строку через пробел
    if x == 1:
        orel += 1
    else:
        reshka += 1
print()
print(f'Орел: {orel}, решка: {reshka}')
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))