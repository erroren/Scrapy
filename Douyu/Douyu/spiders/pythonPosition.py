# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']

    def parse(self, response):
        jsonInfo = json.loads(response.text)
        datalist = jsonInfo['data']
        for data in datalist:
            print("data")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['image_urls'] = data['vertical_src']
            yield item
