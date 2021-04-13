#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:23
# @Author  : russell
# @File    : collector.py
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from hostStats import HostInfo


class HostCollector(object):
    def __init__(self):
        pass

    def collect(self):
        """ 收集主机信息到指标"""

        host=HostInfo()

        cpu_metric=GaugeMetricFamily("cpu_Usage", 'psutil cpu percent', labels=['cpu_number'])
        for mes in host.cpuPercentList():
            cpu_metric.add_metric([str(mes.number)],mes.percent)
        yield cpu_metric

