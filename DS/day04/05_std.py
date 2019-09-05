#!/usr/bin/python3
# !coding=utf-8
'''
标准差的计算
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
# 标准差的计算
std = np.std(closing_prices)
print(std)

# 样本标准差
std = np.std(closing_prices, ddof=1)
print(std)

# 自己实现标准差的计算
m = closing_prices.mean()
d = (closing_prices - m) ** 2
v = np.mean(d)
s = np.sqrt(v)
print(s)
