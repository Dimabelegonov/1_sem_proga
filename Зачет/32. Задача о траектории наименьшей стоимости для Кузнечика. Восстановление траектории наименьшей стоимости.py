"""
Пусть теперь за нахождение в каждой клетке взимается определенная сумма денег.
Необходимо определить минимальную сумму, к-рую требуется заплатить, чтобы добраться до нужной клетки.
Задаем список цен нахождения в каждой клетке Price и список C, в который для
каждой клетки будет задаваться минимальная стоимость ее достижения.
Стоимость достижения i-ой клетки будет равна сумме стоимости нахождения в  ней
и минимальной из стоимостей достижения соседних клеток.
Вторая часть алгоритма - нахождение, какая именно траектория обладает наименьшей
стоимостью.
Сделаем массив Path, который будем заполнять номерами клеток, через которые проходила
искомая траектория.
Нужно двигаться с конца, выбирая ту клетку из двух, стоимость пребывания в которой
меньше. В конце массив нужно перевернуть
"""


def grasshooper_cash(n, price):
    dp = [0 for _ in range(n + 1)]
    dp[1] = price[0]
    for i in range(2, n + 1):
        dp[i] = price[i - 1] + min(dp[i - 1], dp[i - 2])

    return dp


path = []
N = int(input())
Price = list(map(int, input().split()))
dp = grasshooper_cash(N, Price)
path.append(N)
while path[-1] != 0:
    i = path[-1]
    if dp[i - 1] < dp[i - 2]:
        path.append(i - 1)
    else:
        path.append(i - 2)
Path = path[::-1]
print(Path)
