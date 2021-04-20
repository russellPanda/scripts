#!/usr/bin/env python

# @Time    :   2021/04/18 22:52:29
# @Author  :   russell 
# @File    :   handleYaml.py

# -*- encoding: utf-8 -*-


import yaml
from handlefile import read_file
from attrdict import AttrDict  # 按照属性访问字典

from pprint import pprint


def read_yaml(path: str) -> list:
    content = read_file(path)
    yaml_datas = yaml.load_all(content)

    return [AttrDict(data) for data in yaml_datas]


def write_yaml(full_data: dict, path: str):
    with open(path, 'a+', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(full_data, f)
