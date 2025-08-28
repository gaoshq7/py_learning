#### 迭代器 ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 使用iter() 和 next()两个函数来实现对象的迭代。
# 2. 迭代器一定可以用循环语句进行迭代；可迭代对象不一定是迭代器，迭代器必须有'next()'函数，但可迭代对象有‘iter()’函数就可以了
#    在使用for循环迭代的时候，语法会根据可迭代对象的‘iter()’函数生成与其对应的迭代器。
l1 = [1,2,3,4,5]
# 两种遍历方式（for / while）
li1 = iter(l1)
li2 = iter(l1)
for x in li1:
    print(x, end='\t')
print('\n')
while True :
    try :
        print(next(li2), end='\t')
    except StopIteration :
        break