#### 包管理 ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 包：管理模块，里面有若干模块和若干子包。‘目录 + __init__.py’是一个包的标识，有这个结构的目录就是一个包，目录名就是包名，__init__.py里面有函数信息。
# 2. 模块：一个.py文件就是一个模块，里面有若干个变量和若干个函数，他是函数管理的最小单位

import numpy          # 导入整个包
from numpy import linalg as kc  # 导入子包
from numpy.linalg import norm as da  # 导入具体函数 注意：numpy.linalg是一个子包，它可以不用指定模块直接导入函数，是因为__init__.py暴露了函数信息。
from numpy.linalg import linalg as cc  # 导入具体函数
from numpy.linalg.linalg import __getattr__ as jb  # 导入具体函数

a = kc.norm([3, 4, 5, 6])
print(a)

#cc.__getattr__("裤衩")

#jb("裤衩")