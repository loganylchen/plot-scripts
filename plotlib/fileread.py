#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:44
# @Author  : Chen Yuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : fileread.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os, sys
import gzip
import pandas as pd

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def main():
    pass


def read_gz(file, header,sep='\t'):
    '''

    :param file:
    :param header:
    :param sep:
    :return:
    '''
    data = []
    with gzip.open(file, 'rb') as f:
        if header:
            title = f.readline()
            columns = title.strip('\n').split(sep)
            line = f.readline()
        else:
            line=f.readlines()
            columns = list(range(1,len(line.split('\t'))+1))
        while line:
            cells = line.strip('\n').split(sep)
            data.append(cells)
    pd_data = pd.DataFrame(data, columns=columns)
    return pd_data


def read(file,header,sep='\t'):
    '''

    :param file:
    :param header:
    :param sep:
    :return:
    '''
    pd_data = pd.read_csv(file,sep=sep,header=header)
    return pd_data

if __name__ == '__main__':
    main()
