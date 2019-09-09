#!/usr/bin/python3
# !coding=utf-8

'''
日期序列
'''
import pandas as pd

# 以日为频率
datelist = pd.date_range('2019/08/21', periods=5)
print(datelist)
# 以月为频率
datelist = pd.date_range('2019/08/21', periods=5, freq='M')
print(datelist)

start = pd.datetime(2019, 8, 1)
end = pd.to_datetime('2019/08/15')
dates = pd.date_range(start, end)
print(dates)
print(pd.Series(dates).dt.day)

# bdate_range()
dates = pd.bdate_range('2019/08/01', periods=7)
print(dates)
