import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def save_json(path, attributes):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(attributes, file, ensure_ascii=False, indent=3)


if __name__ == "__main__":
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)[0].findall('item')
    save_json('news2.json', [{element.tag: element.text for element in elements} for elements in root])