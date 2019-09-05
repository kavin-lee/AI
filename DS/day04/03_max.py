#!/usr/bin/python3
# !coding=utf-8
'''
最值问题
'''
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    '''日期格式的修改'''
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    # 修改为2011-1-1格式
    return t


# 接受处理后的数据结果,分别为,日期,开盘价,最高价,最低价,收盘价
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes \
    = np.loadtxt('../da_data/aapl.csv',
                 delimiter=',',
                 usecols=(1, 3, 4, 5, 6, 7),
                 unpack=True,
                 dtype='M8[D],f8,f8,f8,f8,f8',
                 converters={1: dmy2ymd},
                 )

# 30天股票的波动区间 最低价~最高价
max_price = highest_prices.max()
min_price = np.min(lowest_prices)
print(max_price, min_price)

# 最高点和最低点都是那一天
max_ind = np.argmax(highest_prices)
min_ind = np.argmin(lowest_prices)
print("max date:", dates[max_ind])
print("max date:", dates[min_ind])

# maximum 与 minimum
# 将两个同维数组中对应元素中最大/最小元素构成一个新的数组
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(np.maximum(a, b))
print(np.minimum(a, b))
