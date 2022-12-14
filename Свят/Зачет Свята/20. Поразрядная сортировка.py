def func(n):
    length = len(str(max(n)))
    A = [list() for _ in range(10)]
    for i in range(length):
        for x in n:
            A[x // 10 ** i % 10].append(x)
        n.clear()
        for l in A:
            for x in l:
                n.append(x)
            l.clear()
    return n

data = list(map(int, input().split()))
print(func(data))

"Временная сложность алгоритма - O(n*m), гду m- кол-во рарзядов"
