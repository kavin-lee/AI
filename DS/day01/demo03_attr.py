#!/usr/bin/python3
# !coding=utf-8
'''
数组属性的基本操作
'''

import numpy as np

# 1. shape 维度
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, ary.shape)  # [1 2 3 4 5 6] (6,)
# 修改shape的属性
ary.shape = (2, 3)
print(ary, ary.shape)  # [[1 2 3] [4 5 6]] (2, 3)

# 2. dtype 元素数据类型
print('dtype:', ary.dtype)  # dtype: int64

# 3.元素索引
print("元素索引的练习....")
ary = np.arange(1, 9)
ary.shape = (2, 2, 2)
print(ary)
print(ary[1])
print(ary[1][1])
print(ary[1][1][0])
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k],end=' ')
