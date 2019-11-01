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
from plotlib.scatterplot import scatter2d

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

def pairplot_pipeline(args):
    '''

    :param args:
    :return:
    '''
    if os.path.splitext(args.data)[1] == '.gz':
        data = read_gz(args.data,args.header,sep=args.sep)
    else:
        data = read(args.data,args.header,sep=args.sep)
    for column in args.column:
        output = '{}.{}.pdf'.format(args.prefix,column)
        pairplot(data,column,args.title,output)

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

def scatter_pipeline(args):
    df = read(args.data,args.header,sep=args.sep)
    figure = scatter2d(df,args.x,args.y,args.title,
                       args.x_label,args.y_label,args.hue,args.style,args.legend,args.alpha,args.width,args.height)
    if args.output.endswith('png'):
        figure.savefig(args.output,dpi=300)
    elif args.output.endswith('pdf'):
        figure.savefig(args.output)
    else:
        raise ValueError("output can only be png file or pdf file")

if __name__ == '__main__':
    main()