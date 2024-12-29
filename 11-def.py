def my_abs(x):
    if x >= 0: 
        return x
    else:
        return -x
print(my_abs(-99))

def nop():
    pass

age = 20
if age >= 18:
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# my_abs('A')

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)
print(r)

def quadratic(a, b, c):
    list = [a,b,c]
    for i in list:
        if not isinstance(i,(int,float)):
            raise ValueError(i,"请输入一个数字")
    n  = b ** 2 - 4 * a * c
    if n > 0:
        x1 = (-b + math.sqrt(n)) / (2 * a)
        x2 = (-b - math.sqrt(n)) / (2 * a)
        return x1, x2
    elif n == 0:
        return -b / (2 * a)
    else:
        return '无解'

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
