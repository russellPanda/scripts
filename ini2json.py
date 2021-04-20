# @Time : 2021/4/8 16:06
# @Author : russell
# @File : handle.py

# -*- coding: utf-8 -*-

import configparser
from configparser import ConfigParser
from pprint import pprint
import json

# ini_path = r'test.ini'
# js_path = r'test.js'


def ini2json(ini_path: str, js_path: str):
    conf = ConfigParser()
    conf.read(ini_path)
    d = {}
    for session in conf.sections():
        d[session] = conf.items(session)
    with open(js_path, 'w+', encoding='utf-8') as f:
        json.dump(d, f)
