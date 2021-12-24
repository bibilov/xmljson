import datetime
import itertools
from json import loads
from urllib.request import urlopen


# Градский %D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87
# page_id: 183903
# page_id: Жан-Поля Бельмондо: 192203
# Жан-Поль Бельмондо: %D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C


def main():
    Alex_Grad_page_title = '%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    Jan_Pol_page_title = '%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
    Alex_Grad_page_id = '183903'
    Jan_Pol_page_id = '192203'

    save_as_json(get_stat(Alex_Grad_page_id, Alex_Grad_page_title), 'StatAlexGrad.txt')
    save_as_json(get_stat(Jan_Pol_page_id, Jan_Pol_page_title), 'StatJanPol.txt')


def get_stat(page_id, page_title):
    data = read_wiki(page_id, page_title)
    revisions = sorted(data, key=get_date, reverse=True)
    groups_rev = itertools.groupby(revisions, get_date)
    res = {}
    for date, group in groups_rev:
        res[date] = list(group)
    return res


def read_wiki(page_id, page_title):
    url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles={page_title}'
    data = loads(urlopen(url).read().decode('utf8'))
    return data['query']['pages'][page_id]['revisions']


def get_date(revision):
    return datetime.datetime.strptime(revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


def save_as_json(revisions, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for date in revisions:
            file.write(f'{date} {len(revisions[date])}\n')


if __name__ == "__main__":
    main()
#
#Всплеск правок звазян со смертью Александра Градского.
#Дата смерти Жан-Поля Бельмондо 6 сентября 2021, что совпадает со "всплеском"
#правок его странички. Но пользоваться такой метрикой,на мой взгляд, ошибочно,
#так как события другого характера могут вызывать больший всплекс активности правок.
#


