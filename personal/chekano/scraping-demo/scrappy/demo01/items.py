# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class IngredientsList(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    items = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(separator=u'|')
    )


