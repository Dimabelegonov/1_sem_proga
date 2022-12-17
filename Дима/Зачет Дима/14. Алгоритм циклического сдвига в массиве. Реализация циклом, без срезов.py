def cyclic_moved(arr, m, side="left"):      # массив, размер сдвига, сторона сдвига
    if side == "left":
        k = -1
    else:
        k = 1

    arr_ans = [0 for i in range(len(arr))]

    for i in range(len(arr)):
        arr_ans[(i + k * m + len(arr)) % len(arr)] = arr[i]

    return arr_ans


print(cyclic_moved([1, 2, 3, 5], 3))
