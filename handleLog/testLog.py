# @Time : 2021/4/28 10:38
# @Author : russell
# @File :  testLog

# -*- coding: utf-8 -*-

import logging


def get_logger(name: str, level_int: int, formatter_str: str, log_path:str , stream=True):
    logger = logging.getLogger(name)
    # level
    logger.setLevel(level=level_int)
    # Formatter
    formatter = logging.Formatter(formatter_str)
    # FileHandler
    if log_path:
        fh = logging.FileHandler(log_path)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # StreamHandler
    if stream:
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger

#
#
#
# # Log
# logger.info('Start')
# logger.warning('Something maybe fail.')
# try:
#     result = 10 / 0
# except Exception:
#     logger.error('Faild to get result', exc_info=True)
# logger.info('Finished')