#### 类（构造器） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class T:

    def __init__(m, p1, p2):
        print(f'构造完成：{m}，{p1}{p2}')

t = T('你好', '吗？')
del t