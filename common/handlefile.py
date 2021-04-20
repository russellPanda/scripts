#!/usr/bin/env python

# @Time    :   2021/04/18 22:52:22
# @Author  :   russell 
# @File    :   handlefile.py

# -*- encoding: utf-8 -*-



import os
from difflib import HtmlDiff, unified_diff
import filecmp


####################################################################

def is_file(path: str):

    if not os.path.isfile(path):
        print(f"{path} is not file")
    else:
        return os.path.abspath(path)


def read_file(path: str):

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


def read_file_lines(path: str):

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return lines


def read_file_line(path: str):

    with open(path, 'r', encoding='utf-8') as f:
        yield f.readline()


def write_file(path: str, data: str):

    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)


def append_write_file(path: str, data: str):

    with open(path, 'a', encoding='utf-8') as f:
        f.write(data)


def empty_file(path: str):

    with open(path, 'w+', encoding='utf-8') as f:
        f.truncate()


def diff_files(path1: str, path2: str):
    file1 = read_file_lines(path1)
    file2 = read_file_lines(path2)
    result = unified_diff(file1, file2)
    # sys.stdout.writelines(result)
    return result


def diff_files_as_html(path1: str, path2: str, html_path: str):

    html_diff = HtmlDiff()
    file1 = read_file_lines(path1)
    file2 = read_file_lines(path2)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_diff.make_file(file1, file2))



#####################################################################

def is_dir(dir_path: str):

    if not os.path.isdir(dir_path):
        print(f'{dir_path} is not dir')
    else:
        return os.path.abspath(dir_path)


def diff_dirs(dir_path1: str, dir_path2: str):

    cmp = filecmp.dircmp(dir_path1, dir_path2)
    print(cmp.report_full_closure())
