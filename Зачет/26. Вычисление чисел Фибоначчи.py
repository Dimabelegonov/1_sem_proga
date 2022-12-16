"""
Рекурсия
"""


def fib(n):
    return 1 if n < 2 else fib(n - 2) + fib(n - 1)


print(fib(6))
