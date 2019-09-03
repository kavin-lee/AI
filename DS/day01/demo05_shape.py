#!/usr/bin/python3
# !coding=utf-8
'''
维度操作
'''
import numpy as np

# 视图变维(胡数据共享)    ==>reshape()  ravel()
a = np.arange(1, 10)
print(a, a.shape)
b = a.reshape(3, 3)  # 视图变维(数据共享)
print(b, b.shape)
b[0, 0] = 999
print(a, a.shape)
c = b.ravel()
print(c, c.shape)

# 复制变维(数据独立) flatten()  copy()
d = b.flatten()
print('d(1):', d)
b[0, 0] = 1
print('d(2):', d)

# 就地变维 a.shape   a.resize()
d.shape = (3, 3)
print(d)
d.resize((9,))
print(d)
