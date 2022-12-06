def reverse_array(arr, N):
    for i in range(N // 2):
        arr[i], arr[N - 1 - i] = arr[N - i - 1], arr[i]
