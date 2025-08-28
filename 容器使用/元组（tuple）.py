#### 元组（tuple） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 元组与数组类似，区别是里面的元素不可修改，指的是元素的地址不可修改，指向的元素如果支持修改仍然可以修改。
a, b, c = 1, 2, [3, 4, 5]
t1 = (a, b, c)
print(t1)
c.append(6)
print(t1)