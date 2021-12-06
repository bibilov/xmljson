from json import dump
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_fields_from_xml(xml: list[ET.Element], tags):
    return [{tag: item.find(tag).text for tag in tags} for item in xml]


def get_all_from_xml(xml: list[ET.Element]):
    return [{field.tag: field.text for field in item} for item in xml]


def write_json_to(json_source, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        dump(json_source, file, ensure_ascii=False, indent=4)


data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

channel = root.find('channel').findall('item')

required_tags = ['pubDate', 'title']

required_fields = get_fields_from_xml(channel, required_tags)
write_json_to(required_fields, 'news.json')

all_fields = get_all_from_xml(channel)
write_json_to(all_fields, 'news2.json')
