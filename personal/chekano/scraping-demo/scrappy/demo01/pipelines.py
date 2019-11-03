# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time

from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter


class Demo01Pipeline(object):
    def process_item(self, item, spider):
        return item


class JSONPipeline(object):

    def open_spider(self, spider):

        if not os.path.exists(f'scrapped_data/{spider.name}'):
            os.makedirs(f'scrapped_data/{spider.name}')

        timestamp = int(time.time())
        filepath = f'scrapped_data/{spider.name}/{timestamp}.items'
        f = open(filepath, 'wb+')

        self.exporter = JsonItemExporter(f)
        self.exporter.start_exporting()

    def close_spider(self, spider):

        self.exporter.finish_exporting()
        self.exporter.file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
