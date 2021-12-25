from json import loads
from urllib.parse import quote
from urllib.request import urlopen
from api_task import get_date_counts

url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=' \
      f'{quote("Бельмондо,_Жан-Поль")}'
data = loads(urlopen(url).read().decode('utf-8'))
revisions = data['query']['pages']['192203']['revisions']

date_counts = get_date_counts(revisions)

print(max(date_counts, key=lambda date: date_counts[date]))