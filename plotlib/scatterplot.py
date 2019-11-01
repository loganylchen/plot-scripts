#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 1/11/2019 10:47 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : scatterplot
# @Software: PyCharm

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


def scatter2d(df, x, y, title=None, x_label=None, y_label=None, hue=None, style=None, legend='full', alpha=1, width=25,
              height=25):
    '''

    :param df:
    :param x:
    :param y:
    :param x_label:
    :param y_label:
    :param hue:
    :param style:
    :param alpha:
    :param width:
    :param height:
    :return:
    '''
    plt.figure(figsize=(width, height))
    plotdict = {
        'data': df,
        'x': x,
        'y': y,
        'alpha': alpha,
        'legend': legend
    }
    print(df.columns)

    setdict = {
        'xlabel': x,
        'ylabel': y,
        'title': title,
    }
    if hue:
        plotdict['hue'] = hue
        plotdict['palette'] = sns.color_palette('hls', len(df[hue].unique()))
    if style:
        plotdict['style'] = style

    p = sns.scatterplot(**plotdict)
    if x_label:
        setdict['xlabel'] = x_label
    if y_label:
        setdict['ylabel'] = y_label
    p.set(**setdict)
    return p.get_figure()
