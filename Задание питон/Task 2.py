import xml.etree.ElementTree as ET
import json
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

date_header = []

for item in root.iter('item'):
    news_object = {}
    for tag in item.iter():
        if tag.tag != 'item':
            news_object[tag.tag] = tag.text
    date_header.append(news_object)

file = open('news_all.json', 'w', encoding='utf-8')
json.dump(date_header, file, indent=4, ensure_ascii=False)
