import datetime
from urllib.request import urlopen
import itertools
from json import loads


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8', 'ignore'))
rev = data['query']['pages']['183903']['revisions']
a = itertools.groupby(rev, lambda x: datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d'))
for item in a:
    print(item[0], len(list(item[1])))

# самый большой всплеск правок в день смерти Александра Градского
