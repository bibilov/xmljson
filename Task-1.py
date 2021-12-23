import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    items = root.find('channel').findall('item')
    tags = ['pubDate', 'title']
    create_json(items, tags, 'news.json')


def create_json(items, tags, filename):
    result = []
    for item in items:
        for i in range(len(tags)-1):
            result.append(
                {
                    tags[i]: item.find(tags[i]).text,
                    tags[i+1]: item.find(tags[i+1]).text
                 }
            )
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(result, file, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
