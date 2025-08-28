#### 函数（返回值） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数可以返回一个或多个值，没有返回值的话默认返回‘None’，再返回多个值的情况下，返回的实际上是一个元组。
# 判断是否是闰年
def isRun(year: int) -> ():
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        return True, '{0}是闰年！' .format(year), 'OK'
    else:
        return False, '{0}非闰年！' .format(year), 'NO'
r1 = isRun(2016)
r2 = isRun(2017)
print(r1, r2, sep='\n')