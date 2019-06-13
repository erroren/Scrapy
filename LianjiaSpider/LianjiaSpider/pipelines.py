# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LianjiaspiderPipeline(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='lianjia')
            self.cur = self.conn.cursor()
        except Exception as e:
            print('error')
    def process_item(self, item, spider):
        try:
            sql = 'insert into message values (%s,%s,%s,%s,%s,%s,%s,%s)'
            params = [item['title'],item['url'],item['unit_price'],item['total_price'],item['communtity_name'],item['area'],item['basic_message'],item['original_message']]
            self.cur.execute(sql,params)
            self.conn.commit()
        except Exception as e:
            print('error1')
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()
