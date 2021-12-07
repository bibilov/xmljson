from urllib.request import urlopen
from json import loads
from itertools import groupby


print("1 task:")
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))

for date, content in groupby(data['query']['pages']['183903']['revisions'], lambda data: data['timestamp'].split('T')[0]):
    print(date, len(list(content)))
# Больше всего изменений (153) 2021-11-28, это связано с датой смерти А. Б. Градский


print("\n" + "\n" + "2 task:")
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

max = 0
result = {}

for date, content in groupby(data['query']['pages']['192203']['revisions'], lambda data: data['timestamp'].split('T')[0]):
    corrections = len(list(content))
    if(corrections > max):
        max = corrections
        result[corrections] = date

print("Дата смерти Жан-Поля Бельмондо: " + result[max])
