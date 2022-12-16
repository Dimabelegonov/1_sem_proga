def binary_search(arr, a):              # нужно быстро найти элемент a в отисортированном массиве arr

    l = -1
    r = len(arr)

    while r - l > 0:
        c = (l + r) // 2
        if arr[c] > a:
            r = c
        elif arr[c] < a:
            l = c
        else:
            l = r = c

    return l


print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))


def check(coords, x, k):
    cnt = 1
    last_cow = coords[0]
    for c in coords:
        if c - last_cow >= x:
            cnt += 1
            last_cow = c

    return cnt >= k


def binary_search_answer(coords, k):         # coords - координаты стоил, k - количество коров
    right = coords[-1] - coords[0] + 1
    left = 0
    while right - left > 0:
        mid = (right + left) // 2
        if check(coords, mid, k):
            left = mid
        else:
            right = mid

    return left


