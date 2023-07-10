""" Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что ф(n)=A.
Если А не является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6 
"""

n = int(input("Введите число: "))
if n == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    i = 1
    while fib_next <= n:
        if fib_next == n:
            print(i)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        i += 1
    else:
        print(-1)