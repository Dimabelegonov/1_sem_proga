"""
Рекурсия
"""

def fib(n):
    return 1 if n < 2 else fib(n - 2) + fib(n - 1)

print(fib(int(input())))

"""
Динамическое программирование
"""

def fib(n):
    a = [1] * 2
    for i in range(2, n + 1):
        a.append(a[i - 2] + a[i - 1])
    return a[n]

print(fib(int(input())))
