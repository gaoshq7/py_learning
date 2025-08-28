#### 内置函数 ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意：set是集合、是无序的、基于hash算法，list是数组。
int1 = int('99') # 字符串转整数
int2 = int(99.99) # 浮点数转整数
fl1 = float('99.99') # 字符串转浮点数
fl2 = float(99) # 整数转浮点数

str1 = str(99.99999) # 转字符串

print(int1, int2, fl1, fl2, str1, sep='\n')
print('----------------------------------')

g = [1,2,3,4,5]
t = (1,2,3,4,5)
di = [('x', 10), ('y', 20), ('z', 90)]
print(type(g), type(t), type(di), sep='\n')

t1 = tuple(g) # 转元组
l1 = list(t) # 转数组
d1 = dict(di) # 转字典
s1 = set(g) # 转集合
f1 = frozenset(g) # 转不可变集合
b1 = bytes(t) # 转不可变byte数组
a1 = bytearray(t) # 转可变byte数组

gx = reversed(g) # 逆转计算

del l1[2] # 删除list元素
del d1['y'] # 删除字典元素
s1.remove(3) # 删除set元素
del a1[2] # 删除byte数组元素

print(t1, l1, d1, s1, f1, b1, a1, gx, sep="\n")
print('----------------------------------')

names = ['张三', '李四', '王五']
ages = [18, 19, 20]
hars = ["打冰球", "羽毛球", "吃西瓜"]
z = zip(names, ages, hars) # 数组压缩

for x in z:
    print(x)