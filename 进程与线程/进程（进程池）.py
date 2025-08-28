#### 进程（进程池） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 进程池可以传入容量，当过多的进程需要执行时会排队。
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('{0} 运行了 {1} 秒'.format(name, (end - start)))


if __name__ == '__main__':
    print('主进程的 PID：{0}'.format(os.getpid()))
    p = Pool(4)
    for i in range(8):
        p.apply_async(long_time_task, args=('进程_' + str(i),))
    p.close()
    p.join()    # 等待所有子进程结束后在关闭主进程
    print('【结束】')
