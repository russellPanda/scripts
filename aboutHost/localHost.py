#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 19:45
# @Author  : russell
# @File    : hostStats.py


import psutil
from psutil import Process

from collections import namedtuple
import platform


# boot time
def boot_time() -> float:
    return psutil.boot_time()


# user
def login_users() -> list:
    return psutil.users()


# hostname
def hostname():
    return platform.uname().node


# cpu
def cpu_count(logical=False) -> int:
    return psutil.cpu_count(logical)


def cpu_stats():
    return psutil.cpu_stats()


def cpu_times():
    return psutil.cpu_times()


def cpu_times_per() -> list:
    return psutil.cpu_times()


def cpu_percent() -> float:
    return psutil.cpu_percent()


def cpu_percent_per() -> list:
    CPUPercent = namedtuple('cpu_percent', ['number', 'percent'])
    cpus = list(enumerate(psutil.cpu_percent(percpu=True)))
    return [CPUPercent(cpu[0], cpu[1]) for cpu in cpus]


def cpu_times_percent():
    return psutil.cpu_times_percent(interval=None, percpu=False)


def cpu_times_percent_per() -> list:
    return psutil.cpu_times_percent(interval=None, percpu=True)


def cpu_freq():
    return psutil.cpu_freq()


def cpu_freq_per() -> list:
    return psutil.cpu_freq(percpu=True)


def cpu_load_list() -> tuple:
    return psutil.getloadavg()


# memory

def virtual_mem():
    return psutil.virtual_memory()


def swap_mem():
    return psutil.swap_memory()


# disk
def disk_partitions() -> list:
    return psutil.disk_partitions()


def disk_usage_by_path(disk_path: str):
    return psutil.disk_usage(disk_path)


def disk_io():
    return psutil.disk_io_counters()


def disk_io_per() -> dict:
    return psutil.disk_io_counters(perdisk=True)


# network

def net_if_addrs() -> dict:
    return psutil.net_if_addrs()


def net_if_stats() -> dict:
    return psutil.net_if_stats()


def net_con() -> list:
    return psutil.net_connections(kind='inet')


def net_io():
    return psutil.net_io_counters()


def net_io_per() -> dict:
    return psutil.net_io_counters(pernic=True)


# process

def all_pids() -> list:
    return psutil.pids()


def get_proc_by_pid(pid: int) -> Process:
    if pid in all_pids():
        return psutil.Process(pid)


def get_children_proc_by_pid(pid: int) -> list:
    return psutil.Process(pid).children()


def proc_info_filter(proc: Process, filter_list: list):
    """ 获取process特定的信息
    :param proc: Process实例
    :param filter_list: ["name", "exe", "cmdline",....]
    :return: [process(name='bash', exe='/usr/bin/bash', cmdline=['-bash']),]
    """
    if proc.is_running():
        process_Info = namedtuple('process', filter_list)
        filter_info = proc.as_dict(attrs=filter_list)
        return process_Info(**filter_info)


def all_proc_info_filter(filter_list: list) -> list:
    """获取过滤后的进程信息
    :param filter_list: ["name", "exe", "cmdline",.....]
    :return: [process(name='bash', exe='/usr/bin/bash', cmdline=['-bash']),]
    """
    process_info_list = []
    process_Info = namedtuple('process', filter_list)
    for process in psutil.process_iter(filter_list):
        info = process.info
        process_info_list.append(process_Info(**info))
    return process_info_list
