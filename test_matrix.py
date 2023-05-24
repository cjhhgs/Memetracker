# -*- coding: utf-8 -*-

"""
@author chen.jiahao
@version 1.0.0
@since 1.0.0
@description 
@createDate 2023/5/24 14:57
"""
import numpy as np
from main import iterate, standard


if __name__ == '__main__':
    hub = np.ones(3)  # hub向量
    auth = np.ones(4)  # authority向量
    matrix = np.array([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 1]])

    hub = standard(hub)
    auth = standard(auth)

    iter_k = 10
    for i in range(iter_k):
        auth, hub = iterate(hub, matrix)
        print("iter:", i)
        print("最热短语：", np.argmax(auth))
        print(auth.max())
        print("最热网站", np.argmax(hub))
        print(hub.max())
