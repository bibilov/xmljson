import xml.etree.ElementTree as ET
import json
from urllib.request import urlopen


def save_as_json(name, out):
    json.dump(out, open(name, 'w', encoding='utf8'))


def save_pd_title(articles):
    out = []
    for article in articles:
        out.append({'pubDate': article.find('pubDate').text, 'title': article.find('title').text})
    save_as_json('news.json', out)


def save_all(articles):
    out = []
    for article in articles:
        out.append({items.tag: items.text for items in article.iter() if not items.tag == 'item'})
    save_as_json('full_news.json', out)


def read_lenta():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)

    articles = root.find('channel').findall('item')

    save_pd_title(articles)
    save_all(articles)


if __name__ == "__main__":
    read_lenta()
