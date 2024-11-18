"""
每隔1秒输出一次“hello, world”，持续10s

Author: 骆昊
Version: 1.0
"""
import time

for i in range(10):
    print('hello, world')
    time.sleep(1)

"""
大家可能已经注意到了，上面的输出和休眠操作都没有用到循环变量i，
对于不需要用到循环变量的for-in循环结构，
按照 Python 的编程惯例，我们通常把循环变量命名为_，
修改后的代码如下所示。虽然结果没什么变化，但是这样写显得你更专业。
"""
import time

for _ in range(10):
    print('hello, world')
    time.sleep(1)


"""
从1到100整数求和
"""
total = 0
for i in range(1,101):
    total += i
print(total) # print(total)这条语句前是没有缩进的，它不受for-in循环的控制，不会重复执行

"""
从1到100的偶数求和
"""
total = 0
for i in range(1,101):
    if i % 2 == 0: # if语句前是有缩进的，它受for-in循环的控制，会重复执行
        total += i
print(total)

"""
从1到100的偶数求和
"""
total = 0
for i in range(2,101,2):
    total += i
print(total)

"""
内置sum偶数求和
"""
print(sum(range(2,101,2)))  # sum函数的参数是一个可迭代对象，它会自动遍历这个对象并求和


"""
while循环,通过布尔值或能产生布尔值的表达式来控制循环，
当布尔值或表达式的值为True时，循环体（while语句下方保持相同缩进的代码块）中的语句就会被重复执行，
当表达式的值为False时，结束循环。
"""
"""
从1到100的整数求和
"""
total = 0
i = 1
while i <= 100:
    total += i
    i += i
print(total)

"""
从1到100的偶数求和
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)

"""
从1到100的偶数求和
break的应用
"""
total = 0
i = 2
while True: # while True表示条件永远为True，循环会一直执行下去
    total += i
    i += 2
    if i > 100: # 当i大于100时，条件为True，执行break语句，结束循环
        break # break语句会立即结束循环，不再执行循环体中剩余的语句
print(total)

"""
从1到100的偶数求和
continue的应用
"""
total = 0
for i in range(1, 101):
    if i % 2 != 0: # 如果i是奇数，执行continue语句，结束本次循环，继续下一次循环
        continue # continue跳过了i是奇数的情况，只有在i是偶数的前提下，才会执行到total += i。
    total += i
print(total)

"""
打印乘法口诀表
end='\t'表示在每行打印完一个乘法表达式后，添加一个制表符（\t）而不是换行符。
这样，所有的乘法表达式都会在同一行打印，直到内层循环结束，即打印完一行的所有乘法表达式。
然后，外层循环会执行print()函数，没有参数，所以会添加一个换行符，开始打印下一行的乘法表达式。
"""
for i in range(1, 10):
    for j in range(1, i + 1): # 内层循环的次数由外层循环的变量控制，内层循环变量j的取值范围是1到i+1
        print(f'{i}×{j}={i * j}', end='\t') # end参数用于指定print函数输出内容的结尾字符，默认是换行符
    print() # print函数输出一个空行，用于换行

"""
剩下的例子没看完
"""


