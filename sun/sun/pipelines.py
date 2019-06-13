# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SunPipeline(object):
    def process_item(self, item, spider):
        print("SunPipeline 执行了 可以走自己的储存逻辑",item["title"])
        return item
