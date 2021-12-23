from urllib.request import urlopen
from json import loads
import itertools
import datetime


def main():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0' \
           '%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
    get_statistic(url, '192203', 'revisions1.txt')


def get_statistic(url, page_id, filename):
    data = loads(urlopen(url).read().decode('utf8'))
    sorted_revisions = sorted(data['query']['pages'][page_id]['revisions'], key=get_date, reverse=True)
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