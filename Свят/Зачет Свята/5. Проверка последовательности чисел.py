"""
Пусть свойство - делимость числа на 5
"""
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
    if a[i] % 5 == 0:
        print("Существует", i)
        cnt += 1
(print("Все элементы кратны 5") if cnt == len(a) else print("Не все элементы кратны 5"))
