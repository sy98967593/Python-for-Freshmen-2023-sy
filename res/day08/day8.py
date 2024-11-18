"""
https://adventofcode.com/2021/day/8
len函数可以获取列表元素的个数N，而range(N)则构成了从0到N-1的范围，刚好可以作为列表元素的索引。
"""


"""
将一颗色子掷6000次，统计每种点数出现的次数

Author: 骆昊
Version: 1.1
"""
import random

counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')