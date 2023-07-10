'''Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи

Input:8
Output: 21

Задание необходимо решать через рекурсию
'''

n = int(input("Введите искомое число Фибоначчи: "))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(n))

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(n))