import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)

    items = root.find('channel').findall('item')
    tags_to_find = ['pubDate', 'title']
    extract_tags(items, tags_to_find, 'news.json')
    extract_all(items, 'news2.json')


def extract_all(items, filename):
    result = []
    for item in items:
        data = {}
        for i in item.iter():
            if i == item:
                continue
            data[i.tag] = i.text
        result.append(data)
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(result, f)


def extract_tags(items, tags_to_find, filename):
    result = []
    for item in items:
        for tag in tags_to_find:
            result.append({tag: item.find(tag).text})
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()
