def func(arr):
    mx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mx:
            mx = arr[i]
            num = []
            num.append(i)
        elif arr[i] == mx:
            num.append(i)
    return num

data = list(map(int, input().split()))
print(func(data))


"Временная сложность алгоритма - O(n)"
