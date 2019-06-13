# -*- coding: utf-8 -*-
import scrapy
from ..items import XtxspiderItem
from scrapy import Request


class XtxSpider(scrapy.Spider):
    name = 'xtx'
    allowed_domains = ['xietd.com']
    start_urls = ['http://www.xietd.com/']

    def parse(self, response):
        shoe_lists = response.xpath('//div[@class="work-list-box"]/div')
        for shoe in shoe_lists:
            item = XtxspiderItem()
            title = shoe.xpath('./div[2]/p[1]/a/text()').extract()[0]
            path = shoe.xpath('./div[2]/p[1]/a/@href').extract()[0]
            item['name'] = title
            req = Request(path, callback=self.parse_item)
            req.meta['item'] = item
            yield req

    def parse_item(self, response):
        url = response.xpath('//div[@class="aimg"]/img/@file').extract()[0]
        item = response.meta['item']
        item['url'] = "http://www.xietd.com/"+url
        yield item