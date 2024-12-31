"""
输出斐波那契数列中的前20个数
"""
a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)

"""
找出100到999范围内的水仙花数
"""
for num in range(100, 1000):
    low = num % 10 # 个位
    mid = num // 10 % 10 # 十位
    high = num // 100 # 百位
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


"""
Craps赌博游戏

Version: 1.0
Author: 骆昊
"""
import random

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break
print('你破产了, 游戏结束!')