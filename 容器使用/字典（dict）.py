#### 字典（dict） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字典就是‘Map’，是一个对象实例，键值对集合。
d1 = dict(x='张三', y=90, h=['唱歌', '跳舞'], u=(1,2,3)) # 创建字典
print(d1['x'], d1['y'], d1['h'], d1['u'], sep='\n') # 获取字典属性
print("------------------------------------------")
for x, y in d1.items():
    print(x, y, sep=':')