#### 基本数据类型（布尔运算） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 布尔值和布尔代数的表示完全一致，一个布尔值只有 True 、 False两种值。
flag = True or False
flag = True and False
flag = None
flag = not flag
flag = 1 in (1,2,3,4,5)

if flag:
    print("对了")
else:
    print("错了")