from urllib.request import urlopen
from json import loads
from itertools import groupby


def get_date(revision):
    return revision['timestamp'][:10]


def get_stats(url, page_id):
    data = loads(urlopen(url).read().decode('utf8'))
    revisions = data['query']['pages'][page_id]['revisions']
    grouped_revisions = groupby(revisions, get_date)
    result = {}
    for k, v in grouped_revisions:
        result[k] = list(v)
    sorted_result = {k: len(v) for k, v in sorted(result.items(), key=lambda item: len(item[1]), reverse=True)}

    print(sorted_result)


def read_wiki():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    page_id = '183903'
    get_stats(url, page_id)
    # На дату 2021.11.28 приходится 153 правки, что связано со смертью данной персоны

    url2 = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,%20%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
    page_id2 = '192203'
    get_stats(url2, page_id2)
    # На дату 2021.09.06 приходится 58 правок, что так же совпадает со смертью "владельца" страницы. Зачастую можно
    # наблюдать именно такую закономерность: на дату с наибольшим количеством правок приходится смерть персоны. Однако
    # полагаться на это нельзя, т.к. другие события могут вызвать большую волну правок, а так же сами правки могут
    # происходить уже после событий, так как сразу не будут оглашены публике


if __name__ == "__main__":
    read_wiki()
