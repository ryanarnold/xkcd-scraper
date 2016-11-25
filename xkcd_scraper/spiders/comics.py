# -*- coding: utf-8 -*-
import scrapy
from xkcd_scraper.items import ComicItem
from hashlib import sha1

class ComicsSpider(scrapy.Spider):
    name = "comics"
    allowed_domains = ["xkcd.com"]
    start_urls = ['http://xkcd.com/' + str(x) for x in range(100)]

    def parse(self, response):
        comic = ComicItem()
        comic['title'] = response.xpath('//div[@id="ctitle"]/text()').extract_first()
        comic['desc'] = response.xpath('//div[@id="comic"]/img/@title').extract_first()

        comic_url = 'https:' + response.xpath('//div[@id="comic"]/img/@src').extract_first()

        comic['filename'] = sha1(comic_url.encode('utf-8')).hexdigest() + '.jpg'
        comic['file_urls'] = [comic_url,]
        
        yield comic