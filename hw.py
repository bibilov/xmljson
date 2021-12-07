from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))

for date, group in groupby(data['query']['pages']['183903']['revisions'], lambda data: data['timestamp'].split('T')[0]):
    print(date, len(list(group)))

#  28 ноября - дата смерти А.Б. Градского
print()
print()

url2 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data2 = loads(urlopen(url2).read().decode('utf8'))
d = {}
max = 0
for date, group in groupby(data2['query']['pages']['192203']['revisions'], lambda data2: data2['timestamp'].split('T')[0]):
    l = len(list(group))
    if(l > max):
        max = l
        d[l] = date

print('Дата смерти Жан-Поля Бельмондо: ')
print(d[max])