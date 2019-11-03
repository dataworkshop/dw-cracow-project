# -*- coding: utf-8 -*-
import scrapy


class Myspider1Spider(scrapy.Spider):
    name = 'myspider1'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
