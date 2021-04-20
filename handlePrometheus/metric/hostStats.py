#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 19:45
# @Author  : russell
# @File    : hostStats.py

import psutil
from collections import namedtuple
import platform

class HostInfo():
    def __init__(self):
        self.hostname=platform.uname().node


    def cpuTimeList(self) -> list:
        return psutil.cpu_times(percpu=True)
    def cpuPercentList(self) -> list:
        CPUPercent = namedtuple('cpu_percent', ['number', 'percent'])
        cpus = list(enumerate(psutil.cpu_percent(percpu=True)))
        return [CPUPercent(cpu[0], cpu[1]) for cpu in cpus]
    def cpuTimePercentList(self) -> list:
        return psutil.cpu_times_percent(interval=None, percpu=True)
    def readCPUCount(self)-> int:
        return psutil.cpu_count(logical=False)
    def logicalCPUCount(self) -> int:
        return psutil.cpu_count(logical=True)
    def cpuStatsList(self) -> list:
        return psutil.cpu_stats()
    def cpuFreqList(self) -> list:
        return psutil.cpu_freq(percpu=True)
    def cpuLoadList(self) -> list:
        return psutil.getloadavg()

