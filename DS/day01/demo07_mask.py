#!/usr/bin/python3
# !coding=utf-8
'''
数组的掩码操作
'''
import numpy as np

# 基于掩码从大数组中截取小数组(即子集)
a = np.arange(1, 100)
# 截取可以被3整除的
print(a[a % 3 == 0])

# 3 7的公倍数
print(a[(a % 3 == 0) & (a % 7 == 0)])

# 使用掩码把数组中的元素重新排列
b = np.array(['A', 'B', 'C', 'D'])
mask = [3, 0, 2, 0, 0, 1, 3, 0, 1]
print("b[mask]:",b[mask])
