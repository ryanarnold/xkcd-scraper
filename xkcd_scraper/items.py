# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    filename = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
