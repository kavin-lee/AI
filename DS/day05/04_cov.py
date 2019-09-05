#!/usr/bin/python3
# !coding=utf-8
'''
斜方差
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
dates, bhp_closing_prices = np.loadtxt(
    '../da_data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8',
    converters={1: dmy2ymd})

vale_closing_prices = np.loadtxt(
    '../da_data/vale.csv', delimiter=',',
    usecols=(6,))

# 绘制收盘价折线图
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 设置x轴的刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator
                           (byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())

# 为了日期的显示合理,修改dates的dtype
dates = dates.astype(md.datetime.datetime)

dates = dates.astype(md.datetime.datetime)
mp.plot(dates, bhp_closing_prices,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='BHP')

mp.plot(dates, vale_closing_prices,
        color='orangered', linewidth=2,
        linestyle='--', label='VALE')

# 计算两只股票的斜方差
ave_bhp = bhp_closing_prices.mean()
ave_vale = vale_closing_prices.mean()
dev_bhp = bhp_closing_prices - ave_bhp
dev_vale = vale_closing_prices - ave_vale
cov = np.mean(dev_bhp * dev_vale)
# cov = (dev_bhp * dev_vale).sum() / (dev_bhp.size - 1)
print(cov)

# 相关性系数
k = cov / (np.std(bhp_closing_prices) * np.std(vale_closing_prices))
print(k)

# 相关矩阵
print(np.corrcoef(
    bhp_closing_prices, vale_closing_prices
))
# 斜方差矩阵
print(np.cov(
    bhp_closing_prices, vale_closing_prices
))
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
