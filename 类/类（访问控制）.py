#### 类（访问控制） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 一个下划线表示‘不推荐访问’；两个下划线表示‘禁止访问’，存储的时候会‘*_类名__属性名’；
# 2. 前后都加两个下划线的函数是“魔法函数”，会自动在某些行为下自动触发，例如：__str__会在‘print()’的时候触发提供展示信息。
class A:
    def __init__(self):
        self._no = "不推荐访问属性"
        self.__secret = "隐藏的属性"

    def __str__(self):
        return '去你妹的吧'

a = A()
print(a._no)
print(a._A__secret)   # 真正的存储名
a._no = '依然可以改1'
a._A__secret = '依然可以改2'
print(a._no)
print(a._A__secret)
print(a)
a.__str__()