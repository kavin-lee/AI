#!/usr/bin/python3
# !coding=utf-8
'''
简单的时间数据处理
统计每周一,周二,周三,周四,周五的数据
'''
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2wday(dmy):
    '''日期格式的修改'''
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.weekday()
    # 修改为2011-1-1格式
    return t


# 接受处理后的数据结果,分别为,日期,开盘价,最高价,最低价,收盘价
wdays, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes \
    = np.loadtxt('../da_data/aapl.csv',
                 delimiter=',',
                 usecols=(1, 3, 4, 5, 6, 7),
                 unpack=True,
                 dtype='f8,f8,f8,f8,f8,f8',
                 converters={1: dmy2wday},
                 )

# 用于存储最终的结果
ave_price = np.zeros(5)
for wday in range(ave_price.size):
    # 用掩码进行数据清洗
    ave_price[wday] = np.mean(closing_prices[wdays == wday])
print(ave_price)

# 数据的轴向汇总 apply_along_axis()
ary = np.arange(1, 21).reshape(4, 5)
print(ary)


def func(array):
    return array.mean(), array.max(), array.min()


# 汇总ary数组,每一行的均值
r = np.apply_along_axis(func, 1, ary)
print(r)


# 汇总ary数组,每一列的均值
r = np.apply_along_axis(func, 0, ary)
print(r)
