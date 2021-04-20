# @Time : 2021/4/8 15:41
# @Author : russell
# @File : handleProcess.py

# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool,cpu_count
import time
import os


def long_time_task(i):
    print(f'子进程:{os.getpid()}-任务:{i}')
    time.sleep(2)
    print(f"结果")


# if __name__ == "__main__":
#     print(f'当前主进程:{os.getpid()}')
#     start=time.time()
#     p1=Process(target=long_time_task,args=(1,))
#     p2=Process(target=long_time_task,args=(2,))
#     print("start")
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#     end=time.time()
#     print(f'总用时间{end-start}')

if __name__ == "__main__":
    print(f'当前主进程:{os.getpid()}')
    start=time.time()
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))

    print("start")
    p.close()
    p.join()
    end=time.time()
    print(f'总用时间{end-start}')
