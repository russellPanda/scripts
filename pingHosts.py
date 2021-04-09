# @Time : 2021/4/9 15:05
# @Author : russell
# @File : pingICMP.py

# -*- coding: utf-8 -*-

from ping3 import ping
from multiprocessing import Pool,cpu_count

#%%


def pingHost(ip:str):
    print(ping(ip))


def main():
    ips=[ f'10.10.32.{str(i)}' for i in range(0,30) ]
    with Pool(cpu_count()) as p:
        p.map(pingHost,ips)


if __name__ == '__main__':
    main()
