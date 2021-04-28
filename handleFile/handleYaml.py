#!/usr/bin/env python

# @Time    :   2021/04/18 22:52:29
# @Author  :   russell 
# @File    :   handleYaml.py

# -*- encoding: utf-8 -*-


import yaml
from handlefile import read_file
from attrdict import AttrDict  # 按照属性访问字典


class HandleYaml:

    def __init__(self, path=None) -> None:
        if path is None:
            self.data = []
        else:
            self.data = HandleYaml.load_yaml(path)

    @staticmethod
    def load_yaml(path: str) -> list:
        content = read_file(path)
        yaml_data = yaml.safe_load_all(content)
        return [data for data in yaml_data]

    def write_yaml(self, path: str):
        with open(path, 'a+', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump_all([dict(content) for content in self.data], f)
