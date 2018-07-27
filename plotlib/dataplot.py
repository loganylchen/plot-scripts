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
import statsmodels.api as sa
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def density(data, column, title='density', out='density.pdf'):
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


def pairplot(data,type_column,title='pairplot',out='pairplot.pdf'):
    '''

    :param data:
    :param type_column:
    :param title:
    :param outdir:
    :return:
    '''
    ax = sns.pairplot(data,hue=type_column)
    # ax.set_title(title)
    fig = ax.get_figure()
    fig.savefig(out)

def cdf(data, type_column, value_column, title='CDF', out='cdf.pdf'):
    '''

    :param data:
    :param type_column:
    :param value_column:
    :param title:
    :param out:
    :return:
    '''
    data[value_column] = data[value_column].astype(float)
    if type_column != '':
        uniq = data[type_column].unique()
        for tp in uniq:
            ecdf = sa.distributions.ECDF(data[data[type_column] == tp][value_column])
            if tp == uniq[0]:
                x = np.linspace(min(data[data[type_column] == tp][value_column]),
                                data[data[type_column] == tp][value_column].median()*1.5)
                pd_data = pd.DataFrame(ecdf(x),x,columns=[tp])
                # pd_data[tp] = ecdf(x)
            else:
                pd_data[tp] = ecdf(x)
    else:
        ecdf = sa.distributions.ECDF(data[value_column])
        x = np.linspace(min(data[value_column]),
                        data[value_column].median()*1.5)
        pd_data = pd.DataFrame(ecdf(x), x, columns=['depth'])
    ax = sns.lineplot(palette="tab10", linewidth=2.5,data=pd_data)
    ax.set_title(title)
    ax.legend()
    fig = ax.get_figure()
    fig.savefig(out)



def main():
    data = pd.read_csv('/Users/chenyl/PycharmProjects/python-lib-test/demo_data/CG.txt',sep='\t')
    cdf(data,'type','depth','test','/Users/chenyl/Desktop/test.pdf')


if __name__ == '__main__':
    main()
