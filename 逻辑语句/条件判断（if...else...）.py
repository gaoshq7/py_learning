#### 条件判断（if...else...） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 非0数字、非空集合、非空数组、非空字符串都可以判定为True。
a, b, c, d, e = 'x', [1, 2, 3], 89, {'a': 90, 'b': 80}, set()
if a:
    print(f'{a}不是空')
if b or e:
    print(f'{b}不是空，{e}不一定是不是')
if c and d:
    print(f'{c}、{d}不是空')
if not e:
    print(f'{e}是空的')