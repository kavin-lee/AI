#!/usr/bin/python3
# !coding=utf-8

'''
组合与拆分
'''
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print("a:", a)
print("b:", b)
# 水平方向操作
c = np.hstack((a, b))
print(c)
a, b = np.hsplit(c, 2)
print("a:", a)
print("b:", b)

#垂直方向操作
c=np.vstack((a,b))
print(c)
a,b=np.vsplit(c,2)
print("a:",a)
print("b:",b)

#深度方向操作
c=np.dstack((a,b))
print("c:",c)
a,b=np.dsplit(c,2)
print("a:",a)
print("b:",b)