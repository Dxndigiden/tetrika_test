from collections import defaultdict
import csv
import re

import scrapy


class AnimalsSpider(scrapy.Spider):
    name = 'animals'
    allowed_domains = ['ru.wikipedia.org']
    start_urls = [
        'https://ru.wikipedia.org/wiki/'
        'Категория:Животные_по_алфавиту'
    ]

    def __init__(self):
        self.animals_data = defaultdict(int)

    def parse(self, response):
        groups = response.css('div#mw-pages div.mw-category-group')

        for group in groups:
            letter = group.css('h3::text').get()
            if letter and re.fullmatch(r'[А-ЯЁ]', letter.strip().upper()):
                count = len(group.css('li'))
                self.animals_data[letter.strip().upper()] += count

        next_page = response.css(
            '#mw-pages a:contains("Следующая страница")::attr(href)'
        ).get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        with open(
            'beasts.csv', 'w', encoding='utf-8', newline=''
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Первая буква', 'Кол-во'])

            for letter in sorted(self.animals_data.keys()):
                writer.writerow([letter, self.animals_data[letter]])

        self.logger.info('Результаты сохранены в beasts.csv')
