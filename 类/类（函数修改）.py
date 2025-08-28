#### 类（函数修改） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 类中的函数也可以通过类似‘属性赋值’的方式进行修改。
import types

class T:

    def test_1(a, b):
        print(a, b, sep='\n')

def test(a):
    print(f'啥也不是：{a}')

T.test_1(9, 0)
T.test_1 = test
T.test_1("我")
print('---------------------------------')

# 2. 类中的函数被修改，实例对象中的函数也会随之被修改。
T.test_1 = lambda a, b, c : print(a, b, c, sep='\t')
t1 = T()
t1.test_1(9, 0)
print('---------------------------------')

# 3. 实例对象可以自行修改自己的函数，但是不会覆盖类中的函数，实例对象修改后的函数不会绑定自己到第一个参数，
#    如果需要达到绑定自己的效果，就要使用‘func1.__get__(obj, MyClass)’函数来实现，或者使用‘types.MethodType(func1, obj)’。
t1.test_1 = lambda a, b : print(a, b, sep='\t')

T.test_1('啊哈', '尼玛', '哈啊')
t1.test_1('尼玛', '啊啊')

t1.test_1 = test.__get__(t1, T)
t1.test_1()

t1.test_1 = types.MethodType(lambda a, b : print(f'来吧{a}，都别活{b}'), t1)
t1.test_1('啦！')