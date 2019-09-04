#!/usr/bin/python3
# !coding=utf-8
'''
柱状图
'''

import numpy as np
import matplotlib.pyplot as mp

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])

mp.figure('Bar Chart', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.xlabel('Month', fontsize=16)
mp.ylabel('Volume', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
x = np.arange(12)
mp.bar(x - 0.2, apples, 0.4, color='dodgerblue', label='Apple')
mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Orange')

# 修改x的刻度文本
mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
