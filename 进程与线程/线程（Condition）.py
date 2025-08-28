#### 进程与线程（Condition） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. threading.Condition() 相较 threading.Lock() 和 threading.RLock()在拥有锁功能的同时还可以使用wait()函数释放锁等待唤醒。
import threading
import time

condition = threading.Condition()
data_ready = False


def consumer():
    global data_ready
    with condition:
        while not data_ready:
            print("等待数据...")
            condition.wait()  # 释放锁，等待通知
        print("拿到数据...")


def producer():
    global data_ready
    with condition:
        print("准备数据中...")
        time.sleep(3)
        print("完成数据生产...")
        data_ready = True
        condition.notify()  # 唤醒等待的消费者


threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()