#!/usr/bin/python3
# !coding=utf-8

'''
series  测试pandas的series对象
'''
import numpy as np
import pandas as pd

data = np.array(['TOM', 'LILI', 'LE', 'KAVIN'])
s = pd.Series(data)
print(s)
s = pd.Series(data, index=[10, 20, 30, 40])
print(s)
# 访问Series中的元素
print(s[10])

# 通过字段创建series的对象
print('--' * 20)
data = {'a': 0, 'b': 1, 'c': 3}
s = pd.Series(data)
print(s)
print(s['a'])

# 通过标量创建series对象
print('--' * 20)
s = pd.Series(5, index=[0, 1, 2, 3, 4])
print(s)

# 使用索引检索元素
s = pd.Series([75, 33, 59, 60, 90],
              index=['a', 'b', 'c', 'd', 'e'])
# 访问下标为0的元素,访问index为'a'的元素
print(s[0], s['a'])
# 切片也是适用的
print(s[:3])

# todo pandas对日期的支持
print('--' * 20)
dates = pd.Series([
    '2011', '2011-02', '2011-03-01', '2011/04/01', '2011/05/01 01:01:01', '01 Jun 2011'
])
print(dates)
dates = pd.to_datetime(dates)
print(dates)

# 日期运算
delta = dates - pd.to_datetime('1970-01-01')
print(delta, type(delta))

#通过series的dt接口,访问 偏移量数据
print(delta.dt.days)
print(delta.dt.year)