def reverse_arr(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]

    return arr


print(reverse_arr(list(map(int, input().split()))))
