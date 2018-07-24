#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:27
# @Author  : Chen Yuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : dataplot.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os, sys
import seaborn as sns
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))



def density(data,column,title='density',out='density.pdf'):
    '''

    :param data:
    :param column:
    :param title:
    :param out:
    :return:
    '''

    data[column] = data[column].astype(float)
    ax = sns.distplot(data[column])
    ax.set_title(title)
    fig = ax.get_figure()
    fig.savefig(out)

def main():
    pass


if __name__ == '__main__':
    main()