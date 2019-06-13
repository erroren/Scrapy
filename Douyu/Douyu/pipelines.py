# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class DouyuPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        print("++++", item)
        meta = {'item': item}
        yield Request(url=item['image_urls'], meta=meta)

    def file_path(self, request, response=None, info=None):
        nickname = request.meta['item']['nickname']
        return nickname+'.jpg'

    def item_completed(self, results, item, info):
        print(results)
        print(type(results))
