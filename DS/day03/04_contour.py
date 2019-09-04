#!/usr/bin/python3
# !coding=utf-8

'''
等高线图
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

# 绘制等高线
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=18)
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, 8, colors='black', linewidths=0.5)
# 绘制等高线的高度标签文本
mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)

#填充等高线
mp.contourf(x,y,z,8,cmap='jet')
mp.show()
