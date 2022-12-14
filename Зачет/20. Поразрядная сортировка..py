def func(n):
    length = len(str(max(n)))
    a = [[] for _ in range(10)]
    for i in range(length):
        for j in range(len(n)):
            ch = n[j] // 10 ** i % 10
            a[ch].append(n[j])
        n = []
        for j in range(10):
            n = n + a[j]
        a = [[] for _ in range(10)]
    return n

data = list(map(int, input().split()))
print(func(data))

"Временная сложность алгоритма - O(?)"