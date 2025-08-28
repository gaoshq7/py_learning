#### 函数（匿名函数） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数使用‘lambda’关键字表示，封装一句表达式当作计算逻辑。
# 计算两个数和的平方
s = lambda x, y : (x + y) ** 2
print(s(1, 1))

# 按字符串长度排序
words = ["你的父亲", "是", "我本人"]
print(sorted(words, key=lambda w: len(w)))

# map：对每个元素平方
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)

# filter：筛选偶数
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)