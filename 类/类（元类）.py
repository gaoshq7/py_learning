#### 类（元类） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 类是创建实例的模版；元类是创建类的模版。
# 2. type就是python内置的一个元类。
# 3. 可以通过继承‘type’函数的方式来自定义元类。
# 4. 元类创建类对象时，会调用元类的__new__方法，从而可以对类对象中的函数进行一些操作。
class Foo:
    pass


print(type(Foo))  # Foo对象是什么类型
print(isinstance(Foo, type))  # Foo对象是不是类型对象


# 定义元类
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"创建类: {name}")
        namespace['say_hello'] = lambda self: print("Hello from metaclass!")
        return super().__new__(mcs, name, bases, namespace)


# 使用自定义元类创建类对象
class MyClass(metaclass=MyMeta):
    pass


print(type(MyClass))
obj = MyClass()
obj.say_hello()
