"""
НОД
"""

def func(a, b):
    return a if b == 0 else func(b, a % b)


a, b = int(input()), int(input())
print(func(a, b))

"""
НОК
"""

def func(a, b):
    return a if b == 0 else func(b, a % b)


a, b = int(input()), int(input())
print(int(1 / (func(a, b)) * a * b))

"""
Нам даны два числа a и b. Пусть d - их НОД => a%d==0, b%d==0
a=q*b+r, r<b => (b*q+r)%d==0 => r%d==0 = > вместо a мы можем использовать r. 
Получаем НОД(b,r).... В итоге получаем НОД(d,0)=d.
"""
