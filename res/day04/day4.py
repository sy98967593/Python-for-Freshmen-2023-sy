print('hello world')

"""
将华氏温度转换为摄氏温度V1
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c)) # '%.nf' 表示格式化输出为指定精度的浮点数


"""
将华氏温度转换为摄氏温度V2
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度') # f'{变量:.n小数位f}' 表示格式化输出为指定精度的浮点数

"""
圆周长面积V1
"""
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

"""
圆周长面积V2
"""
import math # 导入math模块

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius # math.pi 表示圆周率
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}') # f'{变量:.n小数位f}' 表示格式化输出为指定精度的浮点数
print(f'面积: {area:.2f}')

"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 # 闰年判断条件
print(f'{is_leap = }')