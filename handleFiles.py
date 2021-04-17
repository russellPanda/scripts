# @Time : 2021/4/8 11:41
# @Author : russell
# @File : handlefile.py

# -*- coding: utf-8 -*-
import os.path

path1="./text1"
path2="./text2"


from os import path
import sys
import filecmp
from difflib import HtmlDiff,unified_diff

# 比较文件夹结构



def is_dir(dir_path:str):
    if not path.isdir(dir_path):
        print(f'{dir_path} is not a dir')

def is_file(file_path:str):
    if path.isfile(file_path):
        print(f'{file_path} is not a file')


def diff_dirs(dir_path1:str,dir_path2:str):
    is_dir(dir_path1)
    is_dir(dir_path2)

    cmp = filecmp.dircmp(dir_path1, dir_path2)
    print(cmp.report_full_closure())





class handlefile:

    def __init__(self,path:str):
        self.path=path
        if not os.path.isfile(self.path):
            print(f'{self.path} is not a file')

    def read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            file_content=f.read()
        return file_content

    def read_lines(self,path=None):
        if path is not None:
            file_path=path
        else:
            file_path=self.path

        with open(file_path,'r',encoding='utf-8') as f:
            lines=f.readlines()
        return lines

    def empty_file(self):
        with open(self.path,'rw',encoding='utf-8') as f:
            f.truncate()


    def diff_files(self,path:str):
        file1= self.read_lines()
        file2=self.read_lines()
        result = unified_diff(file1, file2)
        sys.stdout.writelines(result)
        return result

    def diff_files_asHtml(self,path:str,html_path:str):
        htmlDiff = HtmlDiff()
        file1=self.read_lines(self.path)
        file2=self.read_lines(path)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(htmlDiff.make_file(file1, file2))





