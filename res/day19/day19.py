class Student:
    __slots__ = ('name', 'age') # 使用__slots__可以限制实例的属性, 只允许添加name和age属性, 不允许添加其他属性

    def __init__(self, name, age): # 初始化方法, 用于给实例添加属性, name和age
        self.name = name
        self.age = age


stu = Student('王大锤', 20) # 创建实例, 并给实例添加属性
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'