# Функция раскладывает заданное число на простыне делители#
def factorize_number(x):
    divisor = 2                         # Cамый простой делитель - 2
    while x > 1:                        # Пока x - не единица действуем след образом:
        if x % divisor == 0:            # Если x делится на делитель, то выписываем очередное значение
            print(divisor, end=' ')     # делителя и уменьшаем x
            x //= divisor
        else:
            divisor += 1                 # Иначе, смотрим следующий делитель


"Сложность алгоритма - O(sqrt(n))"


def factorize_number_fast(x):
    """Бытсрый способ"""
    for divisor in range(2, int(x ** 0.5) + 1):
        while x > 1 and x % divisor == 0:
            print(divisor, end=" ")
            x //= divisor


print(factorize_number_fast(100))
