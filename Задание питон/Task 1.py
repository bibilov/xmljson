import xml.etree.ElementTree as ET
import json
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

date_header = []

for news in root.iter('item'):
    title = news.find('title').text
    pubDate = news.find('pubDate').text
    date_header.append({'title': title, 'pubDate': pubDate})

file = open('news.json', 'w', encoding='utf-8')
json.dump(date_header, file, indent=4, ensure_ascii=False)
