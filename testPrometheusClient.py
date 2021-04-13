#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 18:24
# @Author  : russell
# @File    : testPrometheusClient.py

import psutil
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import make_wsgi_app
from flask import Flask
from collections import namedtuple
from werkzeug.middleware.dispatcher import DispatcherMiddleware



def cpusPercent():
    CPU = namedtuple('cpu', ['number', 'percent']) #这一行放在哪里?
    cpu_data = list(enumerate(psutil.cpu_percent(percpu=True)))
    cpus = [CPU(*item) for item in cpu_data]
    return cpus

class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        cpu_metric=GaugeMetricFamily("CPUUsage", 'get data from psutil', labels=['cpu_number'])
        for mes in cpusPercent():
            cpu_metric.add_metric([str(mes.number)],mes.percent)
        yield cpu_metric


app=Flask(__name__)
app.wsgi_app=DispatcherMiddleware(app.wsgi_app,{
    '/metrics':make_wsgi_app()
})

@app.route('/')
def hello():
    return "test"



if __name__ == '__main__':
    REGISTRY.register(CustomCollector())
    app.run(host='0.0.0.0',port=8082,debug=True)
    # start_http_server(8000)
    # REGISTRY.register(CustomCollector())
    # while True:
    #     time.sleep(1)