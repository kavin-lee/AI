#!/usr/bin/python3
# !coding=utf-8

'''
多个窗口的展示
'''
import numpy as np

import matplotlib.pyplot as mp

mp.figure('Figure A', facecolor='gray')
mp.figure('Figure B', facecolor='lightgray')

mp.title('Figure B', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.tight_layout()

mp.show()
