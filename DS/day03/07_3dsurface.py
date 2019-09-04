#!/usr/bin/python3
# !coding=utf-8

import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 整理数据
n = 1000
x, y = np.meshgrid(
    np.linspace(-3, 3, n),
    np.linspace(-3, 3, n),
)

# 记住就好
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# print(z)

# 绘制3d平面图
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
ax3d.plot_surface(
    x, y, z, cmap='jet', rstride=2, cstride=2
)
mp.tight_layout()
mp.show()
