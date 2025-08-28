#### 进程（封装） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. multiprocessing.Process()可以创建独立的进程而非内存共享的线程。
# 2. 进程对象的daemon属性设置为True时，主进程退出，子进程会一起退出。
# 3. 使用join()函数可以使主进程阻塞等待子进程完成后再继续往后执行。
import multiprocessing
import time


class ClockProcess(multiprocessing.Process):

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        n = 3
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


def sleeper(x):
    print("将要睡三秒...")
    time.sleep(x)


if __name__ == '__main__':
    s = multiprocessing.Process(target=sleeper, args=(3,))
    s.start()
    s.join()  # 等待子进程结束，阻塞主进程。

    p = ClockProcess(2)
    p.daemon = True  # 设置为守护进程，主进程退出，子进程也退出。
    p.start()
    time.sleep(2)

    print("CPU核的个数为: " + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("子进程的信息: " + p.name + "\tp.id: " + str(p.pid))
    print("主进程结束!!!!!!!!!!!!!!!!!")
