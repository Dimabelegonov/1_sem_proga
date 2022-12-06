def cycle_shift(arr, N):
    k = arr[0]

    for i in range(1, N):
        arr[i - 1] = arr[i]

    arr[-1] = k
