from json import loads
from urllib.request import urlopen
from itertools import groupby


def date_of_death(gr):
    date, m = '', 0
    for d, e in gr:
        c = len(list(e))
        if c > m:
            date, m = d, c
    return date


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
data = loads(urlopen(url).read().decode('utf8'))

statistics = groupby([el['timestamp'][:10] for el in data['query']['pages']['192203']['revisions']])
print(date_of_death(statistics))
