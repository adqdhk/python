def fact(n):
    if n==1:
        return 1
    return n*fact(n-1) 

print(fact(1))
print(fact(5))
print(fact(100))
# print(fact(1000))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# print(fact(1000))

def move(n, a, b, c):
    n = int(n)
    if (n <= 0):
        raise TypeError('bad operand n')
    if (n == 1):
        print(a, '-->', c)
    elif (n > 1):
        move(n - 1 , a, c, b) # a中的最大的底盘移动到c时，需要将n-1个盘子借助c移动到b上，然后再将最后的最大底盘移动到c
        print(a, '-->', c) # 把最底下的盘子从 a 移动到 c 上
        move(n - 1, b, a, c)# b上面有n-1个盘子借助a移动到c的问题

move(3, 'A', 'B', 'C')