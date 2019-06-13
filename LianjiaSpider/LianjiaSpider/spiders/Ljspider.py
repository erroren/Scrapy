# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import LianjiaspiderItem
class LjspiderSpider(scrapy.Spider):
    name = 'Ljspider'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sh.lianjia.com/ershoufang/']
    url = 'https://sh.lianjia.com/ershoufang/'
    offset = 0
    page = 1
    def parse(self, response):
        House_lists = response.xpath('//ul[@class="sellListContent"]/li//div[@class="title"]/a/@href').extract()
        for house in House_lists:
            yield Request(house, callback=self.parse_item)
        if self.offset <= 3000:
            self.offset += 30
            self.page += 1
            # linklist = response.xpath('//div[@class="page-box fr"]/div[1]/a[1]/@href').extract()[0]
            linklist = self.url + 'pg{}/'.format(str(self.page))
            print(linklist)
            yield Request(linklist,callback=self.parse)


    def parse_item(self,response):
        item = LianjiaspiderItem()
        title = response.xpath('//h1[@class="main"]/text()').extract()[0]
        url = response.url
        unit_price = response.xpath('//span[@class="unitPriceValue"]/text()').extract()[0]
        total_price = response.xpath('//div[@class="price "]/span[@class="total"]/text()').extract()[0]
        communtity_name = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()[0]
        area1 = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract()[0].strip()
        area2 = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[2]/text()').extract()[0]
        area = area1 + " " + area2
        basic_message_lists = response.xpath('//div[@id="introduction"]//div[@class="base"]/div[@class="content"]/ul/li')
        basic_message = ' '
        for basic_message_list in basic_message_lists:
            label = basic_message_list.xpath('./span[@class="label"]/text()').extract()[0]
            message = basic_message_list.xpath('./text()').extract()[0]
            basic_message = basic_message + label + ' ' + message + '|'
        # print(basic_message)
        original_tags = response.xpath('//div[@class="tags clear"]/div[1]/text()').extract()[0]
        original_tags_lists = response.xpath('//div[@class="tags clear"]/div[2]/a')
        for original_tags_list in original_tags_lists:
            original_tags = original_tags +' ' + original_tags_list.xpath('./text()').extract()[0]
        original_message_lists = response.xpath('//div[@class="baseattribute clear"]')
        baseattribute =''
        for original_message_list in original_message_lists:
             label = original_message_list.xpath('./div[1]/text()').extract()[0]
             content = original_message_list.xpath('./div[2]/text()').extract()[0].strip()
             baseattribute = baseattribute + label + ' ' + content + '\n'
        original_message = original_tags +'\n' + baseattribute
        # print(title,url,unit_price,total_price,communtity_name,area)
        item['title'] = title
        item['url'] = url
        item['unit_price'] = unit_price
        item['total_price'] = total_price
        item['communtity_name'] = communtity_name
        item['area'] =area
        item['basic_message'] = basic_message
        item['original_message'] = original_message
        yield item