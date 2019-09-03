#!/usr/bin/python3
# !coding=utf-8
'''
网格布局 支持单元格合并
'''

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid layout', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(
    0.5, 0.5, 1, size=36, ha='center', va='center'
)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
