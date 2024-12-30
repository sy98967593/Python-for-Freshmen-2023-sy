def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True