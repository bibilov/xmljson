import datetime
from urllib.request import urlopen
from json import loads
import itertools


def main():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80' \
          '%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,' \
          '_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8' \
          '%D1%87 '
    get_statistics(url, '183903', 'revisions.txt')


def get_statistics(url, pageid, filename):
    data = loads(urlopen(url).read().decode('utf8'))
    sorted_revisions = sorted(data['query']['pages'][pageid]['revisions'], key=get_date, reverse=True)
    groups = itertools.groupby(sorted_revisions, get_date)
    statistics = {}
    for date, group in groups:
        statistics[date] = list(group)
    with open(filename, 'w', encoding='utf8') as file:
        for date in statistics:
            print(date, len(statistics[date]), file=file)


def get_date(x):
    return datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


if __name__ == '__main__':
    main()
