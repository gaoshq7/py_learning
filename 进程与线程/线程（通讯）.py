#### 进程与线程（通讯） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 使用队列实现线程间通讯
import time
from queue import Queue
from threading import Thread

isRead = True


def write(q):
    print('正在写入数据...')
    time.sleep(3)
    # 写数据进程
    for value in ['大西瓜', '小番茄', '卡布奇诺']:
        print('写进队列的值为：{0}'.format(value))
        q.put(value)


def read(q):
    # 读取数据进程
    global isRead
    while isRead:
        value = q.get(True)  # 阻塞等待数据
        print('从队列读取的值为：{0}'.format(value))
        if value == '卡布奇诺':
            isRead = False
            print('数据读取完毕退出...')


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=read, args=(q,))
    t2 = Thread(target=write, args=(q,))
    t1.start()
    t2.start()
