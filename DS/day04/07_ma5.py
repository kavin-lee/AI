#!/usr/bin/python3
# !coding=utf-8

'''
移动平均线与卷积的用法
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

mp.plot(dates, closing_prices, color='dodgerblue', alpha=0.3,
        linewidth=2, linestyle='--', label='AAPL CP')

# 控制实体与影线 的颜色
rise = closing_prices >= opening_prices
color = np.array(['white' if x else 'green' for x in rise])
ecolor = np.array(['red' if x else 'green' for x in rise])

# 绘制实体
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=color,
       edgecolor=ecolor, zorder=3, alpha=0.2)

# 绘制影线
mp.vlines(dates, lowest_prices, highest_prices,
          color=ecolor, alpha=0.2)

# 绘制5日移动平均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i + 5].mean()

mp.plot(dates[4:], sma5, color='orangered', label='SMA-5')

# 基于卷积实现5日移动均线
# todo 卷积进行一个降噪的功能
kernel = np.ones(5) / 5
sma10 = np.convolve(
    closing_prices, kernel, 'valid'
)
mp.plot(dates[4:], sma10, color='orangered',
        label='SMA-52', linewidth=7, alpha=0.4)

# 基于卷积实现10日移动均线
kernel = np.ones(10) / 10
sma10 = np.convolve(
    closing_prices, kernel, 'valid'
)
mp.plot(dates[9:], sma10, color='blue',
        label='SMA-10')

# 基于卷积实现15日移动均线
kernel = np.ones(15) / 15

sma53 = np.convolve(
    closing_prices, kernel, 'valid'
)
mp.plot(dates[14:], sma53, color='red',
        label='SMA-15')

# 基于加权卷积实现5日移动均线
# 从y=e^x函数中找到递增的5个权重值作为卷积核
x = np.linspace(-1, 0, 5)
kernel = np.exp(x)[::-1]

# 卷积核元素之和为1
kernel /= kernel.sum()
sma53 = np.convolve(
    closing_prices, kernel, 'valid'
)
mp.plot(dates[4:], sma53, color='green',
        label='SMA-53')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
