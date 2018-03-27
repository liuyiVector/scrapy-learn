# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    rate = scrapy.Field()
    date = scrapy.Field()
    intro = scrapy.Field()
    pass
