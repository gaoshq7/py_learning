#### 类（继承） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 子类在调用没有覆盖的父类函数时，会先从最左侧的父类找起。
# 2. 如果想使用特定类里面的对应函数可以直接调用或者使用‘super(F, a)’，意思是从‘F’类开始往后寻找函数，不包括当前的‘F’类。
import types

class G(object):
    t = '爷爷种的西瓜'
    def t_1(a):
        print('爷爷的函数')

class F(object):
    t = '爸爸种的番茄'
    def t_1(a):
        print('爸爸修改爷爷的函数')
    def t_2(a):
        print('爸爸自己的函数')

class Y(F, G):
    t = '你种的黄瓜'
    def t_1(a):
        print('改良版继承函数')
    def get(a):
        return super(F, a).t

you = Y()
you.t_1()

def t3(self):
    G.t = '变成大粪'

you.t_3 = types.MethodType(t3, you)
you.t_3()

super(F, you).t_1()

print(you.get())