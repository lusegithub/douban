# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DoubanMovieTop250Item(Item):
    title = Field()
    type = Field()
    score = Field()
    date = Field()
    length = Field()
    introduction = Field()
