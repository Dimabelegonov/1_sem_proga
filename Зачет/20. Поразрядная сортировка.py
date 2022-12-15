def radix_sort(arr):
    max_len = len(str(max(arr)))
    data = [[] for i in range(11)]
    for i in range(max_len):
        for el in arr:
            data[(el // 10 ** i) % 10].append(el)

        arr.clear()

        for el in data:
            arr += el
            el.clear()

    return arr


print(radix_sort([5, 3, 10, 4, 2, 1]))

