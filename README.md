# xmljson


# API

Познакомимся с примером публичного API [на примере](https://www.mediawiki.org/wiki/API:Revisions#Example_3:_Get_last_revision_of_a_page,_following_any_redirects) с данными из Википедии. Отметим, что у Википедии регулярно генерируются общедоступные базы данных, поэтому если необходим массовый скрепинг и парсинг, лучше получить доступ к исходному дампу.

Все страницы в Википедии версионируются, поэтому можно посмотреть на историю правок. 

Сделаем это на примере страницы об [Александре Градском](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87).

Посмотрим последние [500 правок](https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87).

Извлечем информацию о последней (самой свежей) правке:

```python
from urllib.request import urlopen
from json import loads


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
print(data['query']['pages']['183903']['revisions'][0])

```

```
{
  'revid': 118174295, 
  'parentid': 118174211,
  'user': '91.76.190.223',
  'anon': '', 
  'timestamp': '2021-11-28T16:48:39Z', 
  'comment': ''
}
```

При помощи `groupby` из `itertools` выведите статистику по количеству правок в следующем виде:
```
2021-11-28 142
2021-11-27 5
2021-11-26 9
2021-11-24 1
2021-11-16 1
2021-11-15 2
2021-11-14 1
...
```

Попробуйте соотнести всплески правок с событиями, связанными с Градским.

## Корреляция

Определите дату смерти Жан-Поля Бельмондо, найдя дату с самым большим количеством правок за последнее время в статье о нем. Можно ли пользоваться такой метрикой?
