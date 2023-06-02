import time

from bs4 import BeautifulSoup
import requests


class LentaParser:
    categories = []
    category = ''
    items = []

    def __init__(self, category=None):
        self.url = 'https://lenta.ru/rss'
        self.f_name = 'parser_' + str(time.time()) + '.txt'
        if category:
            self.category = category
        self.items = self.parse()
        self.set_categories()

    def parse(self):
        responce = requests.get(self.url)
        bs = BeautifulSoup(responce.text, features='xml')
        return bs.find_all('item')

    def set_category(self, category):
        self.category = category


    def get_f_name(self):
        return self.f_name

    def set_categories(self):
        res = self.parse()
        for item in res:
            self.categories.append(item.category.text)

    def get_categories(self):
        return set(self.categories)

    def save_to_file(self):
        with open(self.f_name, 'w', encoding='utf-8') as f:
            if self.category:
                for new in self.items:
                    if new.category.text == self.category:
                        title = new.title.text
                        link = new.link.text
                        cat = new.category.text
                        f.write(title + ' -- ' + link + ' -- ' + cat + '\n')
            else:
                for new in self.items:
                    title = new.title.text
                    link = new.link.text
                    cat = new.category.text
                    f.write(title + ' -- ' + link + ' -- ' + cat + '\n')