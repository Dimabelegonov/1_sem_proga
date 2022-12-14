"""
цикл for уже чуточку сложнее, чуть менее универсальный,
но выполняется гораздо быстрее цикла while.
Этот цикл проходится по любому итерируемому объекту (например строке или списку),
и во время каждого прохода выполняет тело цикла.

слово else, примененное в цикле for,
проверяет, был ли произведен выход из цикла инструкцией break,
или же "естественным" образом. Блок инструкций внутри else
выполнится только в том случае, если выход из
цикла произошел без помощи break.

continue - Оператор continue начинает следующий проход цикла,
минуя оставшееся тело цикла (for или while)

break - Оператор break досрочно прерывает цикл.

range(x, y) - 
"""

for i in range(10):

    if i % 2 == 1:
        continue

    if i == 8:
        break

    print(i)
