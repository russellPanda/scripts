# @Time : 2021/4/8 11:41
# @Author : russell
# @File : handlefile.py

# -*- coding: utf-8 -*-

path1="./text1"
path2="./text2"

#%%
from os import path
import sys
import filecmp
from difflib import HtmlDiff,unified_diff

# 比较文件夹结构



def is_dir(dir_path:str):
    if not path.isdir(dir_path):
        print(f'{dir_path} is not a dir')
        # sys.exit(0)
def is_file(file_path:str):
    if path.isfile(file_path):
        print(f'{file_path} is not a file')
        # sys.exit(0)

def read_filelines(file_path:str):
    with open(file_path,'r',encoding='utf-8') as f:
        file=f.readlines()
    return file

def diff_dirs(dir_path1:str,dir_path2:str):
    is_dir(dir_path1)
    is_dir(dir_path2)

    cmp = filecmp.dircmp(dir_path1, dir_path2)
    print(cmp.report_full_closure())


# 比较文件内容


def diff_files(path1:str,path2:str):
    file1 = read_filelines(path1)
    file2 = read_filelines(path2)

    result = unified_diff(file1, file2)
    sys.stdout.writelines(result)

def diff_files_Html(path1:str,path2:str,html_path:str):
    htmlDiff = HtmlDiff()
    file1 = read_filelines(path1)
    file2 = read_filelines(path2)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(htmlDiff.make_file(file1, file2))




