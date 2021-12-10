import datetime
from urllib.request import urlopen
import itertools
from json import loads


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE%2C_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8', 'ignore'))
rev = data['query']['pages']['192203']['revisions']
a = itertools.groupby(rev, lambda x: datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d'))
for item in a:
    print(item[0], len(list(item[1])))

# тут также рекордное количество правок приходится на день смерти