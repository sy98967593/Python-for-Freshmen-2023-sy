xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)


person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
print(len(person))  # 5
for key in person:
    print(key)


person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)  # True, key在字典中,返回True,注意不是value,而是key
print('tel' in person)   # False, key不在字典中,返回False,注意不是value,而是key

# 索引运算
print(person['name']) # 王大锤,注意是value,不是key
print(person['addr']) # 成都市武侯区科华北路62号1栋101,注意是value,不是key
person['age'] = 25
person['height'] = 178
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}') # key是变量名,可以换成其他名字,如k, i, j等,但key是约定俗成的变量名,表示key的意思,即键的意思