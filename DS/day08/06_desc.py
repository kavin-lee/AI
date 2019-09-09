#!/usr/bin/python3
# !coding=utf-8

'''
dataframe 描述型数据统计
'''
import pandas as pd
import numpy as np

# 创建DF
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)
print(df)
# 测试描述性统计函数
print(df.sum())
print('--' * 20)
print(df.sum(1))
print('--' * 20)
print(df.mean())
print('--' * 20)
print(df.mean(1))
