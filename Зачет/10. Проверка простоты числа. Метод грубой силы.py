"Метод грубой силы - Brute force"
def bf(n):
    d = 2
    while n % d != 0:
        d = d + 1
    return d == n


print(bf(int(input())))

"Временная сложность алгоритма - O(n)"


"Быстрый способ"
def func(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(func(int(input())))

"Временная сложность алгоритма - O(sqrt(n))"
