'''
File:          show_daily_info.py
File Created:  Wednesday, 26th December 2018 10:47:28 am
Author:        xss (callmexss@126.com)
Description:   Some interesting daily things I want to
               know.
-----
Last Modified: Wednesday, 26th December 2018 11:03:28 am
Modified By:   xss (callmexss@126.com)
-----
'''

import requests
import bs4
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.ERROR)


class StoryTeller:
    def __init__(self):
        self.url = 'https://m.juzimi.com'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        }
        self.proxies = {"http": "http://218.76.253.201:61408", "https": "http://218.76.253.201:61408"}
        # self.proxies = {}
        self.sentence = ""
        self.writer = ""
        self.book = ""
        self.contents = ""

    def get_one_sentence(self, num=0):
        if num == 0 or not isinstance(num, int):
            num = random.randrange(1, 1000000)
        url = self.url + '/ju/' + str(num)
        self.url = url
        try:
            logging.debug('parse {}'.format(url))
            # wb_data = requests.get(url, headers=self.headers, proxies=self.proxies)
            wb_data = requests.get(url, headers=self.headers)
            if wb_data.status_code == 200:
                soup = bs4.BeautifulSoup(wb_data.text, 'lxml')
                content_block = soup.select_one('.sentence')
                self.sentence = content_block.getText().strip()
                try:
                    writer_block = soup.select_one('#sencon > div > span.field.field-type-content-taxonomy.field-field-oriwriter > a')
                    self.writer = writer_block.getText().strip()
                    book_block = soup.select_one('#sencon > div > span.field.field-type-content-taxonomy.field-field-oriarticle > a')
                    self.book = book_block.getText().strip()
                    self.contents = '\n'.join([self.sentence, '\t'.join([self.writer, "《" + self.book + "》"])])
                except AttributeError:
                    self.writer = ""
                    self.book = ""
                    self.contents = self.sentence
                logging.debug('get {}'.format(self.contents))
        except Exception as err:
            print(err)

    def read_one_story(self, num=0):
        if self.sentence:
            print(self.sentence)
        else:
            self.get_one_sentence(num)
            while not self.sentence:
                time.sleep(random.randint(11, 15))
                self.get_one_sentence(num)
            print(self.contents)

    def ask_save(self):
        flag = input("Do you like this story?(y/n) ")
        if flag.lower() == 'y':
            with open('data/sentences.privd', 'a') as f:
                f.write(time.asctime() + "\n")
                f.write(self.url + "\n")
                f.write(self.contents + "\n")
                f.write("\n")

    def start(self):
        self.read_one_story()
        self.ask_save()


def tell_stroy():
    teller = StoryTeller()
    teller.start()


if __name__ == '__main__':
    tell_stroy()
    