#!/usr/bin/python3
# !coding=utf-8

'''
散点图
'''

import numpy as np

import matplotlib.pyplot as mp

n = 300
x = np.random.normal(173, 5, n)
y = np.random.normal(65, 10, n)

# 绘图
mp.figure('Persons', facecolor='lightgray')
mp.title('Persons', fontsize=16)
mp.xlabel('Height', fontsize=14)
mp.ylabel('Weight', fontsize=14)
mp.grid(linestyle=':')
# mp.scatter(x,y,marker='o',s=70,
#            color='dodgerblue',label='Persons')
d = (x - 173) ** 2 + (y - 65) ** 2
mp.scatter(x, y, marker='o', s=70,
           label='Persons', c=d, cmap='jet')
mp.legend()
mp.show()
