age = 20
if age >= 18:
    print('your age is', age)
    print('audlt')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

x = 1
if x: 
    print('True')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# height = 1.75
# weight = 80.5
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print('过轻')
# elif bmi > 18.5 and bmi < 25:
#     print('正常')
# elif bmi > 25 and bmi < 28:
#     print('过重')
# elif bmi > 28 and bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

h = 1.75
w = 80.5
bmi = w/(h**2)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<32:
    print('肥胖')
else:
    print('严重肥胖')