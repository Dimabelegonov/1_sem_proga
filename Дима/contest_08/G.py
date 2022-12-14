def sel_sort(arr, y):
    flag = False
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            flag = True

    if not flag:
        return

    k = 0
    for i in range(y, len(arr)):
        if arr[i] == min(arr[y:]):
            k = i
            break
    arr[y], arr[k] = arr[k], arr[y]

    if k != y:
        print(*arr)

    if y < len(arr) - 1:
        sel_sort(arr, y + 1)


data = list(map(int, input().split()))
sel_sort(data, 0)
