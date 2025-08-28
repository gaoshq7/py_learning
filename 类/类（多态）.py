#### 类（多态） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程的多态。
class User(object):
    def __init__(self, name):
        self.name = name
    def hi(self):
        print(f'来啦，老灯：{self.name}')

class VipUser(User):
    def hi(self):
        print(f'你好，爸爸：{self.name}')

class TopUser(User):
    def hi(self):
        print(f'我给您跪下，爷爷：{self.name}')

def hello(user):
    user.hi()

hello(User('梁博'))
hello(VipUser('张碧晨'))
hello(TopUser('张靓颖'))