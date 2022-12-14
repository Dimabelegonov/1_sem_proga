def func(arr):
    mx = int(arr[0])
    for i in range(1, len(arr)):
        if int(arr[i]) > mx:
            mx = int(arr[i])
            num = []
            num.append(i)
        elif int(arr[i]) == mx:
            num.append(i)
    return num


print(func(input().split()))

"Временная сложность алгоритма - O(n)"
