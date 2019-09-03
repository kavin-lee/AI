#!/usr/bin/python3
# !coding=utf-8

'''
基本绘图
'''

import numpy as np
import matplotlib.pyplot as mp

# 绘制一条正弦曲线
x = np.linspace(-np.pi, np.pi, 1000)
print(x.shape)
sinx = np.sin(x)  # 矢量化的sin方法,返回每个x对应的y

# 绘制一条余弦曲线 cos(x)/
cosx = np.cos(x) / 2


# mp.plot(x, sinx)



mp.plot(x, cosx)
mp.plot(x, sinx)
mp.show()
