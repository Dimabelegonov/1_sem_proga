def cycle_shift_M(arr, N, M):
    arr_1 = [arr[i] for i in range(N)]
    for i in range(N):
        arr[i] = arr_1[(i + M) % N]
