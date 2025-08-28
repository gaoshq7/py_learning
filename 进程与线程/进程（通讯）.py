#### 进程（通讯） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 使用terminate()函数可以强制停止进程。
from multiprocessing import Process, Queue
import os, time, random


def write(q):
    # 写数据进程
    print('写进程的PID：{0}'.format(os.getpid()))
    for value in ['大西瓜', '小番茄', '拿铁']:
        q.put(value)
        time.sleep(random.random())


def read(q):
    # 读取数据进程
    print('读进程的PID：{0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从队列中读取的值为：{0}'.format(value))


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    time.sleep(3)
    pr.terminate()  # 强制结束进程读取进程
