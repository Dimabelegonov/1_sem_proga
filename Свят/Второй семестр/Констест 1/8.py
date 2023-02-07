def func(N, a):
    arr = [0] * N
    for i in range(1, N):
        if i == 1:
            arr[i] = abs(a[i] - a[i - 1])
        else:
            arr[i] = min(arr[i - 1] + abs(a[i] - a[i - 1]), arr[i - 2] + 3 * abs(a[i] - a[i - 2]))
    return arr[-1]


N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
print(func(N, a))
