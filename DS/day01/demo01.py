#!/usr/bin/python3
# !coding=utf-8
'''
ndarry:测试数组的创建
'''
import numpy as np

a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1, a1.shape)  # shape:维度
a2 = np.arange(0, 10)
print(a2)
a3 = np.zeros(10, dtype="int32")
print(a3)
a4 = np.ones(10, dtype="float32")
print(a4)
a5 = np.zeros_like(a1)
print(a5)
