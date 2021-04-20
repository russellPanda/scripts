#!/usr/bin/env python

# @Time    :   2021/04/18 22:52:29
# @Author  :   russell 
# @File    :   handleYaml.py

# -*- encoding: utf-8 -*-


import yaml
from handlefile import read_file
from attrdict import AttrDict  # 按照属性访问字典


def read_yaml(path: str) -> list:
    content = read_file(path)
    yaml_data = yaml.load_all(content)

    return [AttrDict(data) for data in yaml_data]


def write_yaml(full_data: list, path: str):
    with open(path, 'a+', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump_all(full_data, f)
