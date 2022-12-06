def merge(L, R):
    i, j = 0, 0
    data = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            data += [L[i]]
            i += 1
        else:
            data += [R[j]]
            j += 1

    data += L[i:] + R[j:]

    return data


def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)  # состояние переменных при вызове

    #  ваша реализация сортировки

    if len(A) == 1:
        return A

    elif len(A) >= 2:
        m = len(A) // 2
        a1 = merge_sort(A[:m], depth + 1, "left")
        a2 = merge_sort(A[m:], depth + 1, "right")
        data = list(merge(a1, a2))

        for i in range(len(data)):
            A[i] = data[i]
        #  внимание
        #    разбиение массива производить по индексу len(A) // 2
        #    элемент, стоящий на индексе разбиения, относить к правой части
        #    при рекурсивном вызове сначала сортировать левую часть от разбиения массива, затем правую

        print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)  # состояние переменных перед выходом из
        # функции
        #  если функция не вызвала сама себя, состояние переменных перед выходом из функции не должно выводиться,
        #  поскольку гарантированно известно, что массив A в таком случае не изменяется
        if depth != 1:
            return A

