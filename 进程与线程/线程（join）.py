#### 进程与线程（join） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. python实现多线程并行有两种方式：threading 和 thread。
# 2. join()函数让主线程阻塞等待当前线程完成后再执行后面逻辑。
import time
import threading as td

class MyThread(td.Thread):
    def run(self):
        for x in range(5):
            print('进程与线程：{}, 编号：{}'.format(self.name, x), end='\n')
            time.sleep(1)

if __name__ == '__main__':
    ts = [MyThread() for x in range(3)]
    for x in ts:
        x.start()
    for x in ts:
        x.join()
    print('完事666')