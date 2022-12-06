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

