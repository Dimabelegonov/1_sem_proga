"""
НОД
"""


def NOD(a, b):
    return a if b == 0 else NOD(b, a % b)


print(NOD(9, 27))

"""
НОК
"""


def NOK(a, b):
    return a * b // NOD(a, b)


print(NOK(5, 120))

"""
Нам даны два числа a и b. Пусть d - их НОД => a%d==0, b%d==0
a=q*b+r, r<b => (b*q+r)%d==0 => r%d==0 = > вместо a мы можем использовать r. 
Получаем НОД(b,r).... В итоге получаем НОД(d,0)=d.
"""
