import datetime
from itertools import groupby
from json import loads
from urllib.request import urlopen

#Адреса
url1 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
url2 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

def date(rev):
    return datetime.datetime.strptime(rev['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()

def stat(rev):
    res = {}
    for key, group_items in groupby(rev, key=date):
        res[key] = sum(1 for i in group_items)
    return sorted(res.items(), key=lambda item: item[1], reverse=True)[0:10]

def result(url1, url2):
    gradski = stat(loads(urlopen(url1).read())['query']['pages']["183903"]['revisions'])
    belmondo = stat(loads(urlopen(url2).read())['query']['pages']["192203"]['revisions'])
    print("Градский")
    for key, value in gradski:
        print("{} {}".format(key, value)) 
    print("Бельмондо")
    for key, value in belmondo:
        print("{} {}".format(key, value)) 
    
result(url1, url2)

