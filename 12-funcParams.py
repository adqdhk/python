def power(x):
    return x * x
print(power(5))
print(power(15))

def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(power(5, 2))
print(power(5, 3))
print(power(5))

#默认参数必须指向不变对象！
def add_end(L = []):
    L.append('END')
    return L
print(add_end())
print(add_end())

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

#可变参数
def calc(numbers):
    sum = 0;
    for n in numbers:
        sum += n * n
    return sum

print(calc([1, 2, 3]))
print(calc([1, 3, 5, 7]))
#参数接收tuple 可以传任意个参数 包括0个
def calc(*numbers):
    sum = 0;
    for n in numbers:
        sum += n * n
    return sum

print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))
print(calc())

#关键字参数
#运输输入0个或任意个含参数名的参数，自动组装为dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Bob', 45, gender='M', job='Enginner')

extra = {'city': 'Beijing', 'job': 'Enginner'}
person('Jack', 24, **extra)

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# person('Jack', 24, 'Beijing', 'Engineer')
person('Jack', 24, city = 'Beijing', job='Engineer')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

def mul(x, *arg):
    result = x;
    for item in arg:
        result *= item
    return result

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')