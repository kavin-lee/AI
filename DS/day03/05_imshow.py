#!/usr/bin/python3
# !coding=utf-8

'''
热成像图
'''

import numpy as np
import matplotlib.pyplot as mp

# 整理数据
n = 500
x, y = np.meshgrid(
    np.linspace(-3, 3, n),
    np.linspace(-3, 3, n),
)
# print(x)
# print(y)
# 记住就好
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# print(z)

# 绘制热成像图
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=18)
mp.grid(linestyle=':')

mp.imshow(z, cmap='jet',origin='lower')
mp.colorbar()
mp.show()
