import xml.etree.ElementTree as ET
from json import dump
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

response_arr = [{item.tag: item.text for item in elem}
		for elem in root.findall('channel/item')]

with open("news.json", "w", encoding = 'UTF-8') as news:
   dump(response_arr, news, indent = 1, ensure_ascii = False)