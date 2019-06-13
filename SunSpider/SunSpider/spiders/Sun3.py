# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import SunspiderItem
class Sun3Spider(CrawlSpider):
    name = 'Sun3'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    content_link = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))
    page_link = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]'))
    rules = [
        Rule(page_link, follow=True),
        Rule(content_link, callback='parse_item')
    ]

    def parse_item(self, response):
        item = SunspiderItem()
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        item['number'] = \
            response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].strip().split(':')[-1]
        item['detail_url'] = response.url
        temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        templs = temp.split(' ')
        item['author'] = templs[0].split('：')[-1].strip()
        item['pub_date'] = templs[1].split('：')[-1].strip()
        content = response.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"]//text()').extract()
        if len(content) > 0:
            item['content'] = ''.join(content)
        else:
            item['content'] = '空'
        yield item
