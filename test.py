# -*- coding: utf-8 -*-

"""
@author chen.jiahao
@version 1.0.0
@since 1.0.0
@description 
@createDate 2023/5/10 15:16
"""

import numpy as np


if __name__ == '__main__':
    matrix = np.ones((3, 5))
    print(matrix)
    a = np.ones(5)
    print(a)
    print(np.dot(matrix, a))
