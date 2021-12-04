import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json
data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []
for event in root.findall(r'./channel/item'):
    date = event.findtext('pubDate')
    title = event.findtext('title')
    news.append({'pubDate': date, 'title': title})
with open('news.json', 'w', encoding='utf-8') as end_file:
    json.dump(news, fp=end_file, ensure_ascii=False, indent=4)