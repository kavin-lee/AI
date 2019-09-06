#!/usr/bin/python3
# !coding=utf-8

'''
函数矢量化
'''
import numpy as np
import math as m


def foo(x, y):
    return np.sqrt(x ** 2 + y ** 2)


a, b = 3, 4
a = np.arange(3, 9).reshape(2, 3)
b = np.arange(4, 10).reshape(2, 3)
print('a:', a)
print('b:', b)
print('foo:', foo(a, b))

# 矢量化处理函数foo函数,使之可以处理矢量数据
foo_vec = np.vectorize(foo)
print("foo_vec:", foo_vec(a, 6))
