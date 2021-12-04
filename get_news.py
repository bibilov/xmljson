import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

tree = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(tree)


def get_date_and_title():
    news = []
    for item in root.iter('item'):
        fields = {}
        for field in item:
            fields["title"] = item.find('title').text
            fields["pubDate"] = item.find('pubDate').text
        news.append(fields)

    with open('new.json', "wb") as write_file:
        write_file.write(json.dumps(news, ensure_ascii=False).encode('utf8'))
    write_file.close()


get_date_and_title()


def get_all_tags():
    news = []
    for item in root.iter('item'):
        fields = {}
        for field in item:
            fields[field.tag] = field.text
        news.append(fields)

    with open('new1.json', "wb") as write_file:
        write_file.write(json.dumps(news, ensure_ascii=False).encode('utf8'))
    write_file.close()


get_all_tags()
