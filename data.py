# -*- coding: utf-8 -*-

"""
@author chen.jiahao
@version 1.0.0
@since 1.0.0
@description 
@createDate 2023/5/10 10:23
"""
import sqlite3
import jsonlines
from urllib.parse import urlparse


def get_domain_by_urllib(url):
    o = urlparse(url)
    domain = o.hostname
    return domain


article_size = 50000


if __name__ == '__main__':
    con = sqlite3.connect('database.sqlite')
    c = con.cursor()
    c.execute("select * from main.articles where article_id < " + str(article_size))
    articles = c.fetchall()
    f = jsonlines.open("./articles.jsonl", "w")
    list_a = []
    domain_set = set()
    for a in articles:
        line = {
            'article_id': a[0],
            'url': get_domain_by_urllib(a[2])
        }
        domain_set.add(get_domain_by_urllib(a[2]))
        list_a.append(line)
    print("articles_size:" + str(len(list_a)))
    f.write_all(list_a)

    c.execute("select * from main.quotes where article_id < " + str(article_size))
    articles = c.fetchall()
    f = jsonlines.open("./quotes.jsonl", "w")
    list_a = []
    phrase_set = set()
    for a in articles:
        line = {
            'article_id': a[0],
            'phrase': a[1]
        }
        list_a.append(line)
        phrase_set.add(a[1])
    print("quotes_size:" + str(len(list_a)))
    f.write_all(list_a)

    f = jsonlines.open("./domains.jsonl", "w")
    list_a = []
    id = 0
    for i in domain_set:
        line = {
            'id': id,
            'domain': i
        }
        id += 1
        list_a.append(line)
    print("domains_size:" + str(len(list_a)))
    f.write_all(list_a)

    f = jsonlines.open("phrase.jsonl", "w")
    list_a = []
    id = 0
    for i in phrase_set:
        line = {
            'id': id,
            'phrase': i
        }
        id += 1
        list_a.append(line)
    print("phrase_size:" + str(len(list_a)))
    f.write_all(list_a)


