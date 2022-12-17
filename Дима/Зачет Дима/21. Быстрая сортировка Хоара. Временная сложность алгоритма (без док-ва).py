"""
Сложность O(nlogn)
"""


def quicksort(arr, a):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    left = []
    middle = []
    right = []

    for el in arr:
        if el == a:
            middle.append(el)
        elif el >= a:
            right.append(el)
        else:
            left.append(el)

    left = quicksort(left, left[len(left) // 2] if len(left) != 0 else 0)
    right = quicksort(right, right[len(right) // 2] if len(right) != 0 else 0)
    return left + middle + right


print(quicksort([8, 10, 9, 45, 32, 2, 3, 5], 4))
