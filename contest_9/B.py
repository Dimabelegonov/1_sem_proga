def search(i, j):
    if i + 1 == j:
        return -1

    m = (i + j) // 2

    if data[m] < k:
        return search(m, j)
    elif data[m] > k:
        return search(i, m)
    else:
        return m + 1


data = list(map(int, input().split()))
k = int(input())

print(search(-1, len(data)))
