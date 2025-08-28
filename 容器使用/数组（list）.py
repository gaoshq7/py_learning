#### 数组（list） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list数组是有序、可重复的。
l1 = ['哈哈', '呵呵', '哦哦', '嘻嘻']

print(l1[3]) # 获取数组中的元素
print(l1[1:3]) # 截取数组中的元素

l1.append('喔喔') # 添加元素
del l1[3] # 删除元素
print(l1)

l = len(l1) # 数组长度
j = l1 + ['啦啦', '呜呜'] # 组合
y = l1 * 2 # 复制
i = '呜呜' in l1 # 判断是否存在
m = max(y) # 返回最大值
n = min(y) # 返回最小值
c = j.count('呜呜') # 统计出现次数
j.extend(['嘘嘘', '嘟嘟']) # 扩展数组，返回‘None’
x = j.index('喔喔') # 找出第一批配元素的位置
j.insert(4, '哇哇') # 按序号插入一个元素
j.pop() # 最后一个元素出栈，可填写位置参数
j.remove('呜呜') # 移除一个元素
j.reverse() # 反转数组
j.sort(key=str.lower) # 排序
print(j)