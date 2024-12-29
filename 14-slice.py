L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])
#前10个数，每两个取一个
print(L[:10:2])
#所有数每5个取一个
print(L[::5])
print(L[:])

print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

def trim(s):
    while s[0:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')