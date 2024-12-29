# 高阶函数
# 变量可以指向函数
print(abs(-10))
print(abs)

x = abs(-10)
print(x)
f = abs
print(f)
print(f(-10))

# 函数名也是对象
# abs = 10
#abs(-10)

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# 编写高阶函数，就是让函数的参数能够接收别的函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式