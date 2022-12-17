def is_sorted(arr):                 # проверка на нестрогое возрастание (в зависимости от знакак в if)
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True


print(is_sorted([1, 2, 6, 4]))
