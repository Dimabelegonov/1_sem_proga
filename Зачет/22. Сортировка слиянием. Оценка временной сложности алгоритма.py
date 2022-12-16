def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr) // 2
    arr_1 = merge_sort(arr[:n])
    arr_2 = merge_sort(arr[n:])
    data = merge(arr_1, arr_2)
    return data


print(merge_sort([2, 3, 4, 5, 1, 1, 10, 2]))
