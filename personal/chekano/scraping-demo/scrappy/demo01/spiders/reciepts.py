# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from demo01.items import IngredientsList

class RecieptsSpider(scrapy.Spider):
    name = 'reciepts'
    allowed_domains = ['aniastarmach.pl']
    start_urls = ['https://aniastarmach.pl/przepisy/']

    def __init__(self, max_pages=None, *args, **kwargs):
        super(RecieptsSpider, self).__init__(*args, **kwargs)

        self.max_pages = int(max_pages)
        self.crawled_pages = 1

    def parse(self, response):
        # Get all przepisy listed on the page

        for url in response.xpath('//div[@class="recipe"]/div/a/@href'):

            if url.get() != "#":
                # yield {'url': url.get()}
                yield scrapy.Request(url.get(), self.get_reciept_info_2)

        # Load next page
        next_page = response.xpath('//div[@class="button-load-more-wrapper"]/a/@href').get()
        if next_page != None:
            if self.max_pages is not None and self.crawled_pages < self.max_pages:

                if next_page:
                    self.crawled_pages += 1
                    yield(scrapy.Request(response.urljoin(next_page)))

    def get_reciept_info(self, response):
        ingredients = response.xpath('//div[@class="recipe-what-to-buy"]/ul/li/span[span]//text()').getall()

        yield {
                'url': response.url,
                'text': ingredients
        }

    def get_reciept_info_2(self, response):
        loader = ItemLoader(item=IngredientsList(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('items', '//div[@class="recipe-what-to-buy"]/ul/li/span[span]')

        yield loader.load_item()