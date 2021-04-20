#!/usr/bin/env python

# @Time    :   2021/04/18 22:52:17
# @Author  :   russell 
# @File    :   handleExecl.py

# -*- encoding: utf-8 -*-


from pandas import ExcelFile, DataFrame
from collections import namedtuple


class HandleExecl():

    def __init__(self, execl_path: str):
        self.path = execl_path
        self.execl = ExcelFile(execl_path)
        self.sheets = self.execl.sheet_names

    def read_sheet(self, sheet: str):
        data = self.execl.parse(sheet)
        fill_data = data.fillna(method='pad')
        columns = fill_data.columns.to_list()
        row_tuple = namedtuple(sheet, columns)

        return [row_tuple(*i) for i in fill_data.values]

    def write_sheet(self):
        pass

# execl_path = r'smoke_data.xlsx'
# target_sheet = r'config'

# case_execl = HandleExecl(execl_path)
# data = case_execl.sheetData(target_sheet)
