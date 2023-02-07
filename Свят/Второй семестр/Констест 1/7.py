def func(K, M, N):
    if N == M:
        return K
    elif N < M:
        return 2 * K + func(K + 1, M, N + 1)


K, M = int(input()), int(input())
print(func(K, M, 1))
