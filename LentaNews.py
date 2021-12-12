from json import dump
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = ET.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))
news_list = []

for i in data.findall('channel/item'):
    news_list.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})

with open("lenta_news.json", "w", encoding='UTF-8') as file:
    dump(news_list, file, indent=1, ensure_ascii=False)
