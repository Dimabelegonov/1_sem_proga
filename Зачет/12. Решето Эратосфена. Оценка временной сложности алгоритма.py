"""
Решето Эратосфена. n - конечное число, до которого мы хотим найти
простые числа
Идея - создаем массив с элементами равными True, потом пробегаем его. И
ндекс элемента и есть число.
Если число простое, то все кратные ему числа - составные.
"""

N = int(input()) + 1                # Необходимо найти все простые чилса меньшие либо равные n
data = []                           # Массив простых чисел
Erat = [True for i in range(N)]
Erat[0] = Erat[1] = False
for i in range(2, N):
    print(i)
    if Erat[i]:
        data.append(i)
        for k in range(2 * i, N, i):
            Erat[k] = False

print(data)
