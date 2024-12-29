#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#获取编码
print(ord('A'))
print(ord('中'))

#转为字符
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

#bytes类型
x = b'ABC' #每个字符都只占用一个字节

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#计算字符数
print(len('ABC'))
print(len('中文'))
#计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#占位符
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('Hello, %s' % 'world')
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1)) #整数位数 是否补0
print('%.2f' % 3.1415926) #小数位数
print('growth rate: %d %%' % 7)
# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# f-string
# :后面的.2f指定了格式化参数（即保留两位小数）
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')