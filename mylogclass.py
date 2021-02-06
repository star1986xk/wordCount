# -*- coding: utf-8 -*-

import logging
import os


class MyLogClass(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler('my.log', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(lineno)d - %(funcName)s - %(process)d - %(processName)s - %(message)s',
            '%Y/%m/%d %H:%M:%S %p')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
