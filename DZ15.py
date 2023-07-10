""" Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
import random
n = int(input("Введите количество арбузов: "))
ar = []
for i in range(n):
    ar.append(random.randint(1, 10))
print(ar, end=' ')
min = max = ar[0]
for i in ar:
    if i < min:
        min = i
    if i > max:
        max = i

print ()
print('Минимальная масса арбуза: ', min)
print('Максимальная масса арбуза: ', max)