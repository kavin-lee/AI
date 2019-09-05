#!/usr/bin/python3
# !coding=utf-8
'''
线性拟合
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
lowest_prices, closing_prices \
    = np.loadtxt('../da_data/aapl.csv',
                 delimiter=',',
                 usecols=(1, 3, 4, 5, 6),
                 unpack=True,
                 dtype='M8[D],f8,f8,f8,f8',
                 converters={1: dmy2ymd},
                 )
# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=16)
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

mp.plot(dates, closing_prices, color='dodgerblue',
        linewidth=2, linestyle='--', label='AAPL CP')

# 根据最高,最低,收盘求出趋势点
trend_points = (highest_prices + lowest_prices + closing_prices
                ) / 3
mp.scatter(dates, trend_points, marker='o', s=70, color='red',
           alpha=0.6, label='Trend Points')
# 针对趋势点执行线性拟合操作,得到k与b并绘制趋势线
# 组织A与B
days = dates.astype('M8[D]').astype('int32')
A = np.column_stack((days, np.ones_like(days)))
B = trend_points
x = np.linalg.lstsq(A, B)[0]
trend_line = x[0] * days + x[1]
mp.plot(dates, trend_line, linewidth=2,
        color='orangered', label='Trend Line')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
