#### 进程与线程（线程锁） ####

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. threading.Lock()是一个互斥锁，同一线程获取多次的话会进入死锁状态。
# 2. threading.RLock()是一个可重入锁，同一线程可以获取多次，不会进入死锁状态。
import threading, time

class MyThread(threading.Thread):

    def __init__(self, lock, name):
        super().__init__()
        self.lock = lock
        self.name = name

    def run(self):
        lock.acquire()
        print('老子{}来啦！'.format(self.name))
        time.sleep(1)
        lock.release()


lock = threading.RLock()
lock.acquire()
ts = [MyThread(lock, name) for name in ('张三', '李四', '王五')]
for x in ts:
    x.start()
time.sleep(3)
lock.release()
print('来吧，孙子们！')