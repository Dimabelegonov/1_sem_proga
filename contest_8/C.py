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

