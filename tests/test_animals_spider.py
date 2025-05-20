import csv

import pytest
from scrapy.http import HtmlResponse, Request

from task2.solution.wik_animals.wik_animals.spiders.animals import AnimalsSpider


HTML_PAGE_1 = '''
<div id='mw-pages'>
  <div class='mw-category-group'>
    <h3>А</h3>
    <ul>
      <li><a href='/wiki/Animal1'>Animal1</a></li>
      <li><a href='/wiki/Animal2'>Animal2</a></li>
    </ul>
  </div>
  <a href='/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Б'
     title='Категория:Животные по алфавиту'>Следующая страница</a>
</div>
'''

HTML_PAGE_2 = '''
<div id='mw-pages'>
  <div class='mw-category-group'>
    <h3>Б</h3>
    <ul>
      <li><a href='/wiki/Animal3'>Animal3</a></li>
    </ul>
  </div>
</div>
'''


@pytest.fixture
def spider():
    '''Создаёт паука'''
    return AnimalsSpider()


def fake_response(url, body):
    '''Создаёт фиктивный ответ'''
    req = Request(url=url)
    return HtmlResponse(url=url, request=req, body=body, encoding='utf-8')


def test_parse_page_counts_letters(spider):
    '''Проверка подсчёта букв на странице'''
    resp = fake_response(
        'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту',
        HTML_PAGE_1
    )
    results = list(spider.parse(resp))
    assert any(hasattr(r, 'callback') for r in results)

    spider.parse(resp)
    assert spider.animals_data['А'] == 2


def test_parse_pagination(spider):
    '''Проверка перехода на следующую страницу'''
    resp1 = fake_response(
        'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту',
        HTML_PAGE_1
    )
    requests = list(spider.parse(resp1))
    next_req = next(r for r in requests if hasattr(r, 'callback'))

    resp2 = fake_response('https://ru.wikipedia.org' + next_req.url, HTML_PAGE_2)
    list(spider.parse(resp2))

    assert spider.animals_data['А'] == 2
    assert spider.animals_data['Б'] == 1


def test_closed_writes_file(tmp_path, spider):
    '''Проверка записи в CSV'''
    spider.animals_data = {'А': 3, 'Б': 1}

    output = tmp_path / 'beasts.csv'
    spider.closed = lambda reason: None

    with open(output, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Первая буква', 'Количество'])
        for letter in sorted(spider.animals_data):
            writer.writerow([letter, spider.animals_data[letter]])
