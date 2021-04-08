# @Time : 2021/4/8 16:06
# @Author : russell
# @File : handle.py

# -*- coding: utf-8 -*-

import configparser
from configparser import ConfigParser
from pprint import pprint
import json


ini_path=r'test.ini'
js_path=r'test.js'


def ini2json(inipath:str,jspath:str):
    confP=ConfigParser()
    confP.read(inipath)
    d={}
    for session in confP.sections():
        d[session]=confP.items(session)
    with open(jspath,'w+',encoding='utf-8') as f:
        json.dump(d,f)
