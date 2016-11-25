# -*- coding: utf-8 -*-
import scrapy
from xkcd_scraper.items import ComicItem


class ComicsSpider(scrapy.Spider):
    name = "comics"
    allowed_domains = ["xkcd.com"]
    start_urls = ['http://xkcd.com/' + str(x) for x in range(100)]

    def parse(self, response):
        comic = ComicItem()
        comic['file_urls'] = ['https:' + response.xpath('//div[@id="comic"]/img/@src').extract_first(),]
        
        yield comic