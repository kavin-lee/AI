#!/usr/bin/python3
# !coding=utf-8

'''
简单的动画
'''
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

# 初始化构建所有样本
n = 100
balls = np.zeros(100, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4),
])
# 数据的初始化
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 50, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

# 绘制图像
mp.figure('Bubble', facecolor='lightgray')
mp.title('Bubble', fontsize=16)
sc = mp.scatter(balls['position'][:, 0],
                balls['position'][:, 1],
                balls['size'],
                color=balls['color'])


# 实现动画
def update(number):
    # 更新界面,让每个点不断的变大
    balls['size'] += balls['growth']

    index = number % 100
    balls['size'][index] = np.random.uniform(40, 50, 1)
    balls['position'][index] = np.random.uniform(0, 1, (1, 2))
    # 更新界面
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


# 每隔30毫秒,执行一次update函数
anim = ma.FuncAnimation(mp.gcf(), update, interval=50)
mp.show()
