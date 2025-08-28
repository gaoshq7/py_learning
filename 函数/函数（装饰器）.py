#### 函数（装饰器） ####

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 装饰器的原理是在闭包函数的基础上加了一层语法糖。
# 2. 装饰器可以嵌套实现多参数传递。
def decorator(func):
    def wrapper(*args, **kwargs):
        print("函数要开始了...")
        result = func(*args, **kwargs)
        print("函数已经结束了...")
        return result

    return wrapper


def decorator_with_args(prefix):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} 函数要开始了...")
            result = func(*args, **kwargs)
            print(f"{prefix} 函数已经结束了...")
            return result

        return wrapper

    return actual_decorator


@decorator  # 使用装饰器的语法糖
def hello1(name):
    print(f"你好啊，{name}")


@decorator_with_args(">>>")
def hello2(name):
    print(f"你好哈，{name}")


if __name__ == "__main__":
    hello1("裤衩")
    print('-------------------------')
    hello2("拖鞋")
