def my_sort(arr):
    t = len(arr)
    for i in range(t):
        for j in range(1, t):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


n = int(input())
data = list(map(int, input().split()))
data = my_sort(data)

print(abs(sum(data[:(n // 2)]) - sum(data[(n // 2):])))
