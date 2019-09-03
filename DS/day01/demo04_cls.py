#!/usr/bin/python3
# !coding=utf-8

'''
ndarray存储复合类型数据
'''
import numpy as np

data = [
    ('zs', [90, 70, 88], 15),
    ('ls', [91, 71, 81], 16),
    ('ww', [92, 72, 82], 17),
]
# 第一种.设置dtype的方式
ary = np.array(data, dtype='U2,3int32,int32')
print(ary, '\nww age:', ary[2]['f2'])

# 第二种.若字段较多,则可以使用第二种设置的dtype的方式
ary = np.array(data,
               dtype=[
                   ('name', 'str', 2),
                   ('scores', 'int32', 3),
                   ('age', 'int32', 1),
               ])
print(ary, '\nww age:', ary[2]['age'])

# 第三种.设置dtype的方式
c = np.array(data, dtype={
    'names': ['name', 'scores', 'age'],
    'formats': ['U2', '3int32', 'int32'],
})
print(ary, '\nls scores:', ary[1]['scores'])

# 测试日期数据类型 datetime64
data = ['2011', '2011-01-02', '2012-01-01', '2012-02-01']
dates = np.array(data)
print(dates, dates.dtype)
dates = dates.astype('M8[M]')  # 精确到Day的datetime64的类型
print(dates, dates.dtype)
print(dates[2]-dates[0])