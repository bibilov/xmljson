# XML
Некоторые сайты все еще поддерживают самое простое API к своим новостям в формате XML: RSS-фиды.

Например, RSS Lenta.ru доступен по адресу: https://lenta.ru/rss

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <language>ru</language>
    <title>Lenta.ru : Новости</title>
    <description>Новости, статьи, фотографии, видео. Семь дней в неделю, 24 часа в сутки.</description>
    <link>https://lenta.ru</link>
    <image>
      <url>https://lenta.ru/images/small_logo.png</url>
      <title>Lenta.ru</title>
      <link>https://lenta.ru</link>
      <width>134</width>
      <height>22</height>
    </image>
    <atom:link rel="self" type="application/rss+xml" href="http://lenta.ru/rss"/>
<item>
  <guid>https://lenta.ru/news/2021/11/28/saakashvili/</guid>
  <author>Алевтина Запольская</author>
  <title>Врачи диагностировали у Саакашвили ПТСР</title>
  <link>https://lenta.ru/news/2021/11/28/saakashvili/</link>
  <description>
```

Считать дерево элементов можно, например, вот так:

```python
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
```

Сами новости хранятся в элементах `channel/item`.

```xml
<item>
  <guid>https://lenta.ru/news/2021/11/28/fake/</guid>
  <author>Степан Костецкий</author>
  <title>Канадская чиновница оказалась ненастоящим аборигеном и потеряла работу</title>
  <link>https://lenta.ru/news/2021/11/28/fake/</link>
  <description>
    <![CDATA[Канадская чиновница в области здравоохранения Кэрри Бурасса, эксперт по здоровью коренного населения и профессор института, занимающегося соответствующими исследованиями, оказалась ненастоящим аборигеном и потеряла работу. Она заявляла, что принадлежит к канадским метисам, но это оказалось ложью.]]>
  </description>
  <pubDate>Sun, 28 Nov 2021 20:17:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2021/11/28/19/20211128194927643/pic_cc5f23c3e6478a543d384b86578881d2.jpeg" type="image/jpeg" length="43556"/>
  <category>Мир</category>
</item>
```

## 1 

Создайте JSON с заголовками и датами пуликации новостей. Сохраните его на диске как `news.json`.

У файла будет такая структура:

```python
[{'pubDate': 'Sun, 28 Nov 2021 20:56:39 +0300',
  'title': 'Совбез Белоруссии заявил о возможном заочном суде над '
           'оппозиционерами'},
 {'pubDate': 'Sun, 28 Nov 2021 20:45:53 +0300',
  'title': 'Футболист «Рубина» сломал ногу в матче РПЛ с «Динамо»'},
 {'pubDate': 'Sun, 28 Nov 2021 20:29:00 +0300',
  'title': 'Врачи диагностировали у Саакашвили ПТСР'},
```

Помните, что JSON хоть и очень похож и почти совместим с словарем в Питоне, это разные форматы, и для конвертации надо использовать модуль `json`. При сохранении указывайте кодировку `utf8`.

## 2

Сделайте подобный JSON, только с текстовым содержимым всех тегов внутри `item`, не перечисляя их, а перебирая потомков xml-узла.

```python
 {'author': 'Евгения Черкасова',
  'category': 'Мир',
  'description': '\n'
                 '    Пресс-секретарь президента РФ Дмитрий Песков в ходе '
                 'видеоконференции с журналистами рассказал о надеждах на '
                 'скорую встречу Байдена и Путина. По словам Пескова, общение '
                 'глав государств пройдет в формате видеоконференции. Он '
                 'добавил, что дата встречи еще не выбрана, но в Кремле '
                 'надеются, что она состоится до конца года.\n'
                 '  ',
  'enclosure': None,
  'guid': 'https://lenta.ru/news/2021/11/28/vstrecha/',
  'link': 'https://lenta.ru/news/2021/11/28/vstrecha/',
  'pubDate': 'Sun, 28 Nov 2021 20:27:00 +0300',
  'title': 'В Кремле понадеялись на встречу Байдена и Путина до нового года'}
```

# API, ДЗ

Познакомимся с примером публичного API [на примере](https://www.mediawiki.org/wiki/API:Main_page) с данными из Википедии. Отметим, что у Википедии регулярно генерируются общедоступные базы данных, поэтому если необходим массовый скрепинг и парсинг, лучше получить доступ к исходному дампу.

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
