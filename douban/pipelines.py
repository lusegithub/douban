# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douban.MysqlDB import DAO


class DoubanMoviePipeline(object):
    def __init__(self):
        self.db = DAO()

    def process_item(self, item, spider):
        title = ''.join(item['title'])
        movie_type = ''.join(item['type'])
        score = ''.join(item['score'])
        date = ''.join(item['date'])
        length = ''.join(item['length'])
        introduction = ''.join(item['introduction'])
        self.db.insert_item(title, movie_type, score, date, length, introduction)
        return item

    def close_spider(self, spider):
        self.db.close_db()
        print('database douban closed...')
