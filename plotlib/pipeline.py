#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:41
# @Author  : Chen Yuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : pipeline.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os, sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from plotlib.fileread import read_gz,read
from plotlib.dataplot import *

def main():
    pass

def density_pipeline(args):
    '''

    :param args:
    :return:
    '''

    if os.path.splitext(args.data)[1] == '.gz':
        data = read_gz(args.data,args.header,sep=args.sep)
    else:
        data = read(args.data,args.header,sep=args.sep)
    density(data,args.column,args.title,args.output)

def cdf_pipeline(args):
    '''

    :param args:
    :return:
    '''
    if os.path.splitext(args.data)[1] == '.gz':
        data = read_gz(args.data,args.header,sep=args.sep)
    else:
        data = read(args.data,args.header,sep=args.sep)
    # print(data.head())
    cdf(data, args.type_column, args.value_column, args.title, args.output)



if __name__ == '__main__':
    main()