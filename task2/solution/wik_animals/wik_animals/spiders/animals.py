from collections import defaultdict
import csv
import re
from typing import Generator, Optional

import scrapy


class AnimalsSpider(scrapy.Spider):
    name: str = 'animals'
    allowed_domains: list[str] = ['ru.wikipedia.org']
    start_urls: list[str] = [
        'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    ]

    def __init__(self) -> None:
        '''Счётчик животных по первой букве'''
        self.animals_data: defaultdict[str, int] = defaultdict(int)

    def parse(
            self,
            response: scrapy.http.Response
    ) -> Generator[scrapy.Request, None, None]:
        '''Парсим страницу, считаем животных по буквам'''
        groups = response.css('div#mw-pages div.mw-category-group')

        for group in groups:
            letter: Optional[str] = group.css('h3::text').get()
            if letter and re.fullmatch(r'[А-ЯЁ]', letter.strip().upper()):
                count = len(group.css('li'))
                self.animals_data[letter.strip().upper()] += count

        next_page: Optional[str] = response.css(
            '#mw-pages a:contains("Следующая страница")::attr(href)'
        ).get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason: str) -> None:
        '''Сохраняем результаты в CSV'''
        with open(
            'beasts.csv', 'w', encoding='utf-8', newline=''
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Первая буква', 'Кол-во'])

            for letter in sorted(self.animals_data.keys()):
                writer.writerow([letter, self.animals_data[letter]])

        self.logger.info('Результаты сохранены в beasts.csv')
