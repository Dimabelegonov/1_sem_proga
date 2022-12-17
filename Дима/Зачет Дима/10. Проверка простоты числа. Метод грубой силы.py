"""Метод грубой силы - Brute force"""


# Программа проверяет простое ли число методом грубой силы, т.е проверяет делится ли оно на любое чило
# меньшее заданого


def is_simple(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def func(n):
    """Быстрый способ"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(func(int(input())))

"""Временная сложность алгоритма - O(sqrt(n))"""
