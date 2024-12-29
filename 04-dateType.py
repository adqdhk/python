print(10_000_000)
print(1.23e9, 1.23e-5)
print('I\'m ok.')
print('I\'m learning\nPython')
print('\\\n\\')
print('\\\t\\')
#r''标识''中的字符串默认不转义
print(r'\\\t\\')
#多行输出
print('''line1
line2
line3''')
print(r'''hello,\n
world''')
# print(True and True)
# print(True and False)
# print(False and False)
# print(5 > 3 and 3 > 1)

# print(True or True)
# print(True or False)
# print(False or False)
# print(5 > 3 or 3 > 1)

# print(not True)
# print(not False)
# print(not 1 > 2)

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

a = 1
t_007 = 'T007'
Answer = True

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

#内存指向
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#除法的结果是浮点数
print(9 / 3)
#地板除
print(9 // 3)

print(10 % 3)