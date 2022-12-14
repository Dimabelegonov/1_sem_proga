def func(data):
    if len(data) == 1:
        return data[0][0]

    s = 0
    for j in range(len(data)):
        new_data = [[0 for x in range(len(data) - 1)] for y in range(len(data) - 1)]
        for x in range(1, len(data)):
            for y in range(len(data)):
                if y < j:
                    new_data[x - 1][y] = data[x][y]
                elif y > j:
                    new_data[x - 1][y - 1] = data[x][y]

        s += data[0][j] * func(new_data) * ((-1) ** (j % 2))
        # print(data[0][j])
        # print(func(new_data))
        # print(new_data)
        # print((-1) ** (j % 2))

    return s


n = int(input())
data = [list(map(int, input().split())) for j in range(n)]

print(func(data))
