def my_sort(arr, t):
    for _ in range(t):
        for j in range(1, t):
            if float(arr[j - 1][0]) < float(arr[j][0]):
                arr[j - 1][0], arr[j][0] = arr[j][0], arr[j - 1][0]
                arr[j - 1][1], arr[j][1] = arr[j][1], arr[j - 1][1]
            elif arr[j - 1][0] == arr[j][0]:
                if arr[j - 1][1] < arr[j][1]:
                    arr[j - 1][0], arr[j][0] = arr[j][0], arr[j - 1][0]
                    arr[j - 1][1], arr[j][1] = arr[j][1], arr[j - 1][1]

    return arr


def merge(arr_1, arr_2):
    ans = []
    i = 0
    j = 0
    while i < len(arr_1) and j < len(arr_2):
        if float(arr_1[i][0]) > float(arr_2[j][0]):
            ans.append(arr_1[i])
            i += 1
        elif arr_1[i][0] == arr_2[j][0]:
            if arr_1[i][1] > arr_2[j][1]:
                ans.append(arr_1[i])
                i += 1
            else:
                ans.append(arr_2[j])
                j += 1
        else:
            ans.append(arr_2[j])
            j += 1

    ans += arr_1[i:] + arr_2[j:]
    return ans


n = int(input())
data = []
for _ in range(n):
    a = int(input())
    c = []
    for q in range(a):
        b = list(map(str, input().split()))
        c.append(b)
    c = my_sort(c, a)
    data = merge(data, c)

print(len(data))
for x in data:
    print(*x)
