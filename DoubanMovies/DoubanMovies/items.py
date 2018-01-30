# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    info = scrapy.Field()
    pic = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    pass
