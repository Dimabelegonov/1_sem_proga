def func(n):
    s = n
    A = []
    for i in range(2, int(n ** 0.5) + 1):
        if s % i == 0:
            while s % i == 0:
                A.append(i)
                s = s / i
    return A


print(func(int(input())))

"Сложность алгоритма - O(sqrt(n))"
