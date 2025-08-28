#### 生成器（generator） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 生成器是一个返回迭代器的对象，它不像数组直接占用内存空间，而是边循环边推算出下一元素，
# 2. 在函数中使用‘yield’关键字会立刻返回，下次调用函数时会继续计算。
def create(n):
    for x in range(n):
        yield x ** 2


g = create(10)
print(type(g))
print(next(g), next(g), next(g), next(g), next(g), sep='\n')
for x in g:
    print(x)

print('---------------------------------------------------------------------------------------------------------')

g = (x**2 for x in range(1, 11) if x % 2 == 0)

print('g的数据类型是：{0}'.format(type(g)))

for i in g:
    print(i)
