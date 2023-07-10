'''Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes
'''

# n = int(input("Введите число: "))

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(n))

n = 'а роза упала на лапу Азора'

def polindrom(n):
    n = n.lower().replace(' ', '')
    if n == 0 or n == 1:
        return True
    if n == n[::-1]:
        return True
    else:
        return False
print(polindrom(n))