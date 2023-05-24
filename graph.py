# -*- coding: utf-8 -*-

"""
@author chen.jiahao
@version 1.0.0
@since 1.0.0
@description 
@createDate 2023/5/10 13:03
"""

from scipy import sparse
import jsonlines
import numpy as np


def load_phrase():
    f = jsonlines.open('phrase.jsonl', 'r')
    phrase_map = dict()
    index = 0
    for line in f:
        phrase = line['phrase']
        phrase_map[phrase] = index
        index += 1
    return phrase_map


def load_domain():
    f = jsonlines.open('domains.jsonl', 'r')
    domains_map = dict()
    index = 0
    for line in f:
        domain = line['domain']
        domains_map[domain] = index
        index += 1
    return domains_map


def load_articles():
    f = jsonlines.open('articles.jsonl', 'r')
    article_map = list()
    for line in f:
        domain = line['url']
        article_map.append(domain)
    return article_map


# 获取矩阵
def get_graph():
    domain_map = load_domain()
    phrase_map = load_phrase()
    article_domain_list = load_articles()

    hub_size = len(domain_map)
    auth_size = len(phrase_map)
    print("矩阵大小：", str(hub_size), "x", str(auth_size))

    matrix = np.zeros((hub_size, auth_size))

    f = jsonlines.open('quotes.jsonl', 'r')
    for line in f:
        article_id = line['article_id']
        phrase = line['phrase']
        phrase_id = phrase_map[phrase]

        domain = article_domain_list[article_id]
        domain_id = domain_map[domain]

        matrix[domain_id, phrase_id] = 1

    return matrix


if __name__ == '__main__':
    print('Python')
    get_graph()
