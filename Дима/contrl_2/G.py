def func(i):
    if i > n - 3:
        return 0
    if m[i] == 0:
        m[i] = arr[i + 1] - arr[i] + max(func(i + 2), func(i + 3))
    return m[i]


arr = list(map(int, input().split()))
arr = sorted(arr)
n = len(arr)
m = [0 for i in range(n)]
print(arr[-1] - arr[0] - max(func(1), func(2)))
