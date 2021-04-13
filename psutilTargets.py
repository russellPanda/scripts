# @Time : 2021/4/9 17:17
# @Author : russell
# @File : MonitorHost.py

# -*- coding: utf-8 -*-
# doc: https://psutil.readthedocs.io/en/latest/

import psutil
from pprint import pprint



#%%
print("逻辑cpu:",psutil.cpu_count()) # 逻辑cpu数量
print("cpu数量:",psutil.cpu_count(logical=False))
print("stats:",psutil.cpu_stats())
print("time:",psutil.cpu_times())
print("percent:",psutil.cpu_percent())
print("percent every:",psutil.cpu_percent(percpu=True)) # 散着统计
print("t/p:",psutil.cpu_times_percent())
print("t/p/every:",psutil.cpu_times_percent(percpu=True))
print(psutil.cpu_freq())
print(psutil.getloadavg())

print("虚拟内存:",psutil.virtual_memory())
print("交换内存:",psutil.swap_memory())



print("磁盘按驱动:",psutil.disk_partitions())
print("路径占磁盘:",psutil.disk_usage("C:\\"))
print("磁盘IO:",psutil.disk_io_counters(perdisk=True))


print("网络IO:",psutil.net_io_counters())
print("网络类型链接:",psutil.net_connections(kind='inet'))
print("网络适配器:",psutil.net_if_addrs())
print("网络适配器:",psutil.net_if_stats())

psutil.boot_time()
psutil.users()



#Process