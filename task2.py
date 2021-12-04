import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json
data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []
for event in root.findall(r'./channel/item'):
    event_dict = {}
    for child in event:
        event_dict[child.tag] = child.text
    news.append(event_dict)
with open('news2.json', 'w', encoding='utf-8') as end_file:
    json.dump(news, fp=end_file, ensure_ascii=False, indent=4, sort_keys=True)