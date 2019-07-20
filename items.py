# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SlashdotMediaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    News_Headline = scrapy.Field()
    News_Author = scrapy.Field()
    News_date = scrapy.Field()
    User_loged = scrapy.Field()
    pass
