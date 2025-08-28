#### 列表生成式 ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式是python一个基础语法：[表达式 迭代语句 筛选条件 [迭代语句 筛选条件 ...]]。
d = {'a': 1, 'b': 2, 'c': 3}
r1 = [(k, v, b) for k, v in d.items() if k != 'c' for b in range(1, 7) if b % 2 == 0]

l1 = [x * x for x in range(1, 11) if x % 2 == 0]

print('r1 和 l1对象的类型都是：{0}'.format(type(r1)), r1, l1, sep='\n')

g = (x**2 for x in range(1, 11) if x % 2 == 0)

print('g的数据类型是：{0}'.format(type(g)))

for i in g:
    print(i)