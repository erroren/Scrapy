# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs


class JobspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('51job.csv', 'w', 'utf-8')
        self.wr = csv.writer(self.file, dialect='excel')
        self.wr.writerow(['name'])
        print("初始化")

    def process_item(self, item, spider):
        self.wr.writerow([item['name']])
        print("返回item")
        return item

    def close_spider(self, spider):
        print("关闭文件")
        self.file.close()