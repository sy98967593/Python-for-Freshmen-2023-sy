"""
调用列表方法
list.append()：在列表末尾添加一个元素
list.insert(i, x)：在列表第i个位置插入元素x
list.remove(x)：删除列表中第一个值为x的元素
list.pop(i)：删除列表中第i个位置的元素，并返回该元素
list.clear()：清空列表
list.index(x)：返回列表中第一个值为x的元素的索引
list.count(x)：返回列表中值为x的元素个数
list.sort()：对列表进行排序
list.reverse()：将列表中的元素反转
list.copy()：返回列表的一个副本
list.bar()：返回列表中所有元素组成的字符串
list.extend(iterable)：将可迭代对象中的元素添加到列表末尾
list.join(iterable)：将可迭代对象中的元素用指定的分隔符连接成一个字符串
"""

#添加删除列表元素
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
temp1=languages.pop()
print(temp1)      # JavaScript
print(languages)  # ['Python', 'SQL', C++']
temp = languages.pop(1)
print(temp)       # SQL
print(languages)  # ['Python', C++']
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

#元素位置和频次
items = ['Python', 'Java', 'Java', 'C++', 'kotlin', 'Python']
print(items.index('Python')) # 0
print(items.index('Python', 1)) # 5
print(items.count('Python')) # 2
print(items.count('kotlin')) # 1
print(items.count('Swfit')) # 0
print(items.index('Java', 2))

#列表生成式 场景1 未应用生成式
items = []
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
#列表生成式 场景1 应用生成式
items = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0]
print(items)

"""
强烈建议用生成式语法来创建列表
"""