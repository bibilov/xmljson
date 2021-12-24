import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def main():
    items = read_lentaRU()
    save_as_json(write_pd_and_title(items), 'new1.json')
    save_as_json(write_all_in_item(items), 'new2.json')


def read_lentaRU():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root.find('channel').findall('item')


def write_pd_and_title(items):
    res = []
    for item in items:
        res.append(
            {
                "pubDate": item.find("pubDate").text,
                "title": item.find("title").text
            }
        )
    return res


def write_all_in_item(items):
    res = []
    for item in items:
        res_dict = {}
        for i in item.iter():
            if i.tag != 'item':
                res_dict[i.tag] = i.text
        res.append(res_dict)
    return res


def save_as_json(json_list, file_name):
    with open(file_name, 'w', encoding='utf8') as jsonFile:
        json.dump(json_list, jsonFile, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

