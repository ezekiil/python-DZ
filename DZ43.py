'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список чисел.
Все числа списка находятся на разных строках

1 2 3 2 3 -> 2 пары: (2, 3) и (3, 2)
'''

a = [1, 2, 3, 2, 3, 6, 2, 5, 3]
print(a)
count = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
print(f'в заданном списке количество пар равных друг другу: {count}')