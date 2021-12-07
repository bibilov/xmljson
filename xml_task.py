import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    items = root.find('channel').findall('item')
    tags_to_find = ['pubDate', 'title']
    parse_tags(items, tags_to_find, 'news.json')
    parse_items(items, 'news1.json')


def parse_tags(items, tags_to_find, filename):
    result = []
    for item in items:
        for tag in tags_to_find:
            result.append({tag: item.find(tag).text})
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(result, file, indent=1, ensure_ascii=False)


def parse_items(items, filename):
    result = []
    for item in items:
        data = {}
        for i in item.iter():
            if i == item:
                continue
            data[i.tag] = i.text
        result.append(data)
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(result, file, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
