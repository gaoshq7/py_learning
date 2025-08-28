#### 类（变量） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. class里面出现的变量都是静态变量使用‘类.变量’就可以访问。
class T1:
    var1 = '大西瓜'

    @staticmethod
    def test_1():
        global a
        global b
        a = '我成为了你的父亲'
        b = '我"test_1"修改了b'

    @staticmethod
    def test_2():
        b = ''
        def nb():
            nonlocal b
            b = '我"test_2_内部"修改了b'

print(T1.var1)
T1.var1 = "小香蕉"
T1.var2 = "大香蕉"
print(T1.var1, T1.var2, sep='\n')
print("----------------------------")

# 2. 实例对象的变量是私有变量，外部访问不到。
t1 = T1()
t2 = T1()
t1.a = '癞蛤蟆'
t2.b = '娃娃鱼'
print(t1.a, t2.b, t1.var1, t2.var2, sep='\n')
print("----------------------------")

# 3. 实例的属性与类重名时，实例没有给该属性赋值则使用类的值，赋值了只能更新实例本身该属性值，不能修改类中的值。
t3 = T1()
print(f'修改前的var1：{t3.var1}', T1.var1, sep='\n')
t3.var1 = '大菠萝'
print(f'修改后的var1：{t3.var1}', T1.var1, sep='\n')
print("----------------------------")

# 4. global 和 nonlocal可以在函数的作用域里面定义全局变量和上层调用者作用域变量。
b = '哈哈'
T1.test_1();
print(a, b, sep='\n')
T1.test_2();
print(b)