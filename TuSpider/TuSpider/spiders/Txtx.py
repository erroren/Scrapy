# -*- coding: utf-8 -*-
import scrapy
from ..items import TuspiderItem
from scrapy import Request
class TxtxSpider(scrapy.Spider):
    name = 'Txtx'
    allowed_domains = ['photophoto.cn']
    start_urls = ['http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5']

    def parse(self, response):
        Image_list = response.xpath('//ul[@id="list"]/li')
        for Image in Image_list:
            image_name = Image.xpath('.//div[@class="text2"]/a/text()').extract()[0]
            image_url = Image.xpath('.//div[@class="text2"]/a/@href').extract()[0]
            item = TuspiderItem()
            item['image_name']=image_name
            req = Request(image_url, callback=self.parse_image)
            req.meta['item'] = item
            yield req

    def parse_image(self,response):
        image_path = response.xpath('//div[@id="photo"]/img/@src').extract()[0]
        item = response.meta['item']
        item['image_path'] = image_path
        yield item
