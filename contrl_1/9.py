n = int(input())

data = [list(map(str, input().split())) for i in range(n)]

data_1 = [[data[i][j] for i in range(n)] for j in range(n)]


for i in data_1:
    print(*i)
