# -*- coding: utf-8 -*-

"""
@author chen.jiahao
@version 1.0.0
@since 1.0.0
@description 
@createDate 2023/5/10 10:23
"""
import jsonlines

import graph
import numpy as np


def standard(a):
    sum_a = 0
    for i in a:
        sum_a += pow(i, 2)
    sum_a = pow(sum_a, 0.5)
    for i in range(len(a)):
        a[i] = a[i]/sum_a
    return a


def iterate(hub, matrix):
    auth = np.dot(matrix.transpose(), hub)
    hub = np.dot(matrix, auth)

    auth = standard(auth)
    hub = standard(hub)

    return auth, hub


if __name__ == '__main__':
    matrix = graph.get_graph()  # 图矩阵
    hubs = matrix.shape[0]
    auths = matrix.shape[1]
    hub = np.ones(hubs)    # hub向量
    auth = np.ones(auths)  # authority向量
    hub = standard(hub)
    auth = standard(auth)

    domains = []
    f = jsonlines.open('domains.jsonl', 'r')
    for l in f:
        domains.append(l['domain'])

    phrase = []
    f = jsonlines.open('phrase.jsonl', 'r')
    for l in f:
        phrase.append(l["phrase"])

    iter_k = 20
    for i in range(iter_k):
        auth, hub = iterate(hub, matrix)
        print("iter:", i)
        print("最热短语：", phrase[np.argmax(auth)])
        print(auth.max())
        print("最热网站", domains[np.argmax(hub)])
        print(hub.max())



