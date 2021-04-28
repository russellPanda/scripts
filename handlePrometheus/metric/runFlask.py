#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:34
# @Author  : russell
# @File    : runFlask.py

from prometheus_client.core import REGISTRY
from prometheus_client import make_wsgi_app
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from collector import HostCollector

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})


@app.route('/')
def hello():
    return "test"


if __name__ == '__main__':
    REGISTRY.register(HostCollector())
    app.run(host='0.0.0.0', port=8082, debug=True)
