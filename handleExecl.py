# @Time : 2021/4/8 17:44
# @Author : russell
# @File : handleExecl.py

# -*- coding: utf-8 -*-

# 表格第一行必须为标题

from pandas import ExcelFile
from collections import namedtuple


class HandleExecl():

    def __init__(self, execl_path: str):
        self.path = execl_path
        self.execl = ExcelFile(execl_path)
        self.sheets = self.execl.sheet_names

    def sheetData(self, sheet: str):
        data = self.execl.parse(sheet)
        fill_data = data.fillna(method='pad')
        columns = fill_data.columns.to_list()
        row_tuple = namedtuple(target_sheet, columns)
        return [row_tuple(*i) for i in fill_data.values]

execl_path = r'smoke_data.xlsx'
target_sheet = r'config'

case_execl = HandleExecl(execl_path)
data=case_execl.sheetData(target_sheet)
