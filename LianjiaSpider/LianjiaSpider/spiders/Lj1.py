# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import LianjiaspiderItem
class Lj1Spider(CrawlSpider):
    name = 'Lj1'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['https://sh.lianjia.com/ershoufang/']
    content_link = LinkExtractor(restrict_xpaths=('//ul[@class="sellListContent"]/li//div[@class="title"]/a'))
    rules = [
        Rule(content_link, callback='parse_item'),
    ]

    def parse_item(self, response):
        item = LianjiaspiderItem()
        title = response.xpath('//h1[@class="main"]/text()').extract()[0]
        url = response.url
        unit_price = response.xpath('//span[@class="unitPriceValue"]/text()').extract()[0]
        total_price = response.xpath('//div[@class="price "]/span[@class="total"]/text()').extract()[0]
        communtity_name = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()[0]
        area1 = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract()[0].strip()
        area2 = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[2]/text()').extract()[0]
        area = area1 + " " + area2
        basic_message_lists = response.xpath(
            '//div[@id="introduction"]//div[@class="base"]/div[@class="content"]/ul/li')
        basic_message = ' '
        for basic_message_list in basic_message_lists:
            label = basic_message_list.xpath('./span[@class="label"]/text()').extract()[0]
            message = basic_message_list.xpath('./text()').extract()[0]
            basic_message = basic_message + label + ' ' + message + '|'
        # print(basic_message)
        original_tags = response.xpath('//div[@class="tags clear"]/div[1]/text()').extract()[0]
        original_tags_lists = response.xpath('//div[@class="tags clear"]/div[2]/a')
        for original_tags_list in original_tags_lists:
            original_tags = original_tags + ' ' + original_tags_list.xpath('./text()').extract()[0]
        original_message_lists = response.xpath('//div[@class="baseattribute clear"]')
        baseattribute = ''
        for original_message_list in original_message_lists:
            label = original_message_list.xpath('./div[1]/text()').extract()[0]
            content = original_message_list.xpath('./div[2]/text()').extract()[0].strip()
            baseattribute = baseattribute + label + ' ' + content + '\n'
        original_message = original_tags + '\n' + baseattribute
        # print(title,url,unit_price,total_price,communtity_name,area)
        item['title'] = title
        item['url'] = url
        item['unit_price'] = unit_price
        item['total_price'] = total_price
        item['communtity_name'] = communtity_name
        item['area'] = area
        item['basic_message'] = basic_message
        item['original_message'] = original_message
        yield item
