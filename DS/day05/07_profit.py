# -*- coding: utf-8 -*-
"""
demo07_profit.py  研究两支股票收益率
"""
from __future__ import unicode_literals
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = time.date().strftime('%Y-%m-%d')
    return t

dates, bhp_closing_prices = np.loadtxt(
    '../da_data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8',
    converters={1: dmy2ymd})

vale_closing_prices = np.loadtxt(
    '../da_data/vale.csv', delimiter=',',
    usecols=(6,))


# 绘制收盘价折线图
mp.figure('Profits', facecolor='lightgray')
mp.title('Profits', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置x轴刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
ax.xaxis.set_minor_locator(md.DayLocator())

# 为了日期显示合理，修改dates的dtype
dates = dates.astype(md.datetime.datetime)

# 获取两支股票的收益率
bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[1:]

# 绘制收益线
mp.plot(dates, bhp_returns, color='dodgerblue',
        linestyle='--', label='bhp_returns',
        alpha=0.1)
mp.plot(dates, vale_returns, color='orangered',
        linestyle='--', label='vale_returns',
        alpha=0.1)

# 卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')
mp.plot(dates[7:], bhp_returns_convolved, color='dodgerblue',
        label='bhp_returns_convolved', alpha=0.3)
mp.plot(dates[7:], vale_returns_convolved, color='orangered',
        label='vale_returns_convolved', alpha=0.3)

# 对两条降噪收益率曲线，执行多项式拟合操作
days = dates.astype('M8[D]').astype('i4')
bhp_p = np.polyfit(days[7:], bhp_returns_convolved, 3)
bhp_polyfit_y = np.polyval(bhp_p, days[7:])
vale_p = np.polyfit(days[7:], vale_returns_convolved, 3)
vale_polyfit_y = np.polyval(vale_p, days[7:])
mp.plot(dates[7:], bhp_polyfit_y, color='dodgerblue',
        label='bhp_polyfit_y', alpha=0.9)
mp.plot(dates[7:], vale_polyfit_y, color='orangered',
        label='vale_polyfit_y', alpha=0.9)

# 求取两个收益率降噪拟合曲线的交点
diff_p = np.polysub(bhp_p, vale_p)
xs = np.roots(diff_p)
print(xs.astype('i4').astype('M8[D]'))

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
