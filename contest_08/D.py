def split_barrier(A, barrier):
    a1 = []
    a2 = []
    a3 = []
    for i in A:
        if i < barrier:
            a1.append(i)
        elif i == barrier:
            a2.append(i)
        else:
            a3.append(i)

    data = a1 + a2 + a3
    for i in range(len(A)):
        A[i] = data[i]


def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)

    if len(A) == 0:
        return []

    if len(A) == 1:
        return A

    a = A[0]
    split_barrier(A, a)

    t = 0
    for i in range(len(A)):
        if A[i] == a:
            t = i
            break

    k = 0
    for i in range(len(A)):
        if A[i] == a:
            k = i

    a1 = hoar_sort(A[:t], depth + 1, "left")
    a2 = hoar_sort(A[k + 1:], depth + 1, "right")
    data = a1 + A[t:k + 1] + a2

    for i in range(len(data)):
        A[i] = data[i]

    print('depth:', depth, 'part:', part, 'array after:', A)
    if depth != 1:
        return A

