print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# print([x for x in range(1, 11) if x % 2 == 0 else 0])
# print([x if x % 2 == 0 for x in range(1, 11)])

#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
print([x if x % 2 == 0 else -x for x in range(1, 11)])

x = 'abc'
y = 123
print(isinstance(x, str))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')