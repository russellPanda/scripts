#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 10:18
# @Author  : russell
# @File    : metric.py


import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        g = GaugeMetricFamily("MemoryUsage", 'Help text', labels=['instance'])
        g.add_metric(["instance01.us.west.local"], 20)
        yield g



if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)