"""1定义类"""
class Student: # 定义一个类

    def study(self, course_name): # 定义一个方法,方法名是study,
        # 参数是course_name,表示课程名称，
        # self表示对象本身，表示该方法属于类的一个实例，
        # self用于引用类的实例本身，以便访问该实例的属性和其他方法
        print(f'学生正在学习{course_name}.')
        # 括号里f'的意思是格式化字符串，作用是将字符串中的占位符{}替换为变量值

    def play(self): # 定义一个方法,方法名是play
        print(f'学生正在玩游戏.')

"""2创建和使用对象"""
stu1 = Student() # 创建一个Student类的实例对象stu1
stu2 = Student() # 创建一个Student类的实例对象stu2
print(stu1)    # 输出实例对象在内存中的地址（十六进制形式）
print(stu2)    # 输出实例对象在内存中的地址（十六进制形式）
print(hex(id(stu1)), hex(id(stu2)))    # 用id函数查看同上0x10ad5ac50 0x10ad5acd0

"""2.5使用对象，也就是给对象发消息，来执行之前定义的方法"""
# 1.通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 2.通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数课程名称
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)                      # 学生正在玩游戏.
stu2.play()                             # 学生正在玩游戏.

"""1初始化方法"""
class Student:
    """学生"""

    def __init__(self, name, age): #给实例添加姓名和年龄两个属性
        """初始化方法"""
        self.name = name # self.name表示实例的name属性，name表示传入的参数
        self.age = age # self.age表示实例的age属性，age表示传入的参数

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

# 调用Student类的构造器创建对象并传入初始化参数
stu1 = Student('骆昊', 44)
stu2 = Student('王大锤', 25)
stu1.study('Python程序设计')    # 给对象发消息，执行方法中的代码
stu2.play()                    # 给对象发消息，执行方法中的代码


'''案例1 定义一个类，描述数字时钟'''
import time

# 定义时钟类
class Clock:
    """数字时钟"""

    def __init__(self, day=0, hour=0, minute=0, second=0):
        """初始化方法
        :param day: 天
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.day = day
        self.hour = hour
        self.min = minute
        self.sec = second


    def run(self):
        """走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
                    self.day += 1

    def show(self):
        """显示时间"""
        return f'{self.day:0>2d}:{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'
        #>表示右对齐，0表示用0填充，2表示宽度为2


# 创建时钟对象实例
clock = Clock(0,23, 59, 58)
while True:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠1秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    clock.run()

'''7'''
class Point:
    """平面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx * dx + dy * dy) ** 0.5
        print(distance)
        # return (dx * dx + dy * dy) ** 0.5 # return返回值

    def __str__(self): # 定义对象的字符串表示， 返回一个字符串
       return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)  # 调用对象的__str__魔法方法
print(p2)
p1.distance_to(p2)
#print(p1.distance_to(p2))