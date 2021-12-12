from json import dump
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = ET.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))
news_list = []

for i in data.findall('channel/item'):
    news_list.append({j.tag: j.text for j in i})

with open("text_news.json", "w", encoding='UTF-8') as file:
    dump(news_list, file, indent=1, ensure_ascii=False)
