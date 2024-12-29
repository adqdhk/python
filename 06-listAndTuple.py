classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

#tuple 元组
t = (1, 2)
print(t)
t = ()
print(t)
t = (1) # 定义的是1
print(t)
t = (1,)
print(t)

# 元素不可变，但元组中的数组的元素可以变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)