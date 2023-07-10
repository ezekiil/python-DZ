'''Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d

Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''

text = 'a a a b c a a d c d d'
a = list(text.split()) # преобразуем строку в список
letter = {} # создаем словарь
result = ''
# for i in a:
#     if i not in letter: # проверяем наличие элемента в словаре
#         letter[i] = 1 # добавляем элемент
#         result += f'{i} ' 
#     else:
#         result += f'{i}_{letter[i]} '
#         letter[i] += 1
# print(result)

for i in a:
    if i in letter:
        print(f'{i}_{letter[i]}', end=' ')
    else:
        print(i, end=' ')
    letter[i] = letter.get(i, 0) + 1 # накопитель (счетчик)