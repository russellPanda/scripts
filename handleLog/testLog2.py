# @Time : 2021/4/28 10:43
# @Author : russell
# @File :  testLog2

# -*- coding: utf-8 -*-
import logging
from testLog import get_logger

format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = get_logger("test", logging.DEBUG, format_str, 'testlog.log')

# Log
logger.info('Start')
logger.warning('Something maybe fail.')
try:
    result = 10 / 0
except Exception:
    logger.error('Faild to get result', exc_info=True)
logger.info('Finished')

