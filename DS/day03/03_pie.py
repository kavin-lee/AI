#!/usr/bin/python3
# !coding=utf-8

'''
饼图
'''
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Pie', facecolor='lightgray')
# 整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
mp.figure('Pie', facecolor='lightgray')
mp.axis('equal')
mp.title('Pie', fontsize=20)
mp.pie(values, spaces, labels, colors,'%.2f%%',
       shadow=True, startangle=0, radius=1)
mp.show()
