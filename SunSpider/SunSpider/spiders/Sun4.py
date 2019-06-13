# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import SunspiderItem
from scrapy import Request

class Sun4Spider(RedisSpider):
    name = 'Sun4'
    redis_key = 'Sun4:start_urls'
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Sun4Spider, self).__init__(*args, **kwargs)

    def parse(self, response):
        links = response.xpath('//a[@class="news14"]/@href').extract()
        for link in links:
            req1 = Request(link, callback=self.parse_item)
            yield req1
        # 翻页处理
        if self.offset < 60000:
            self.offset += 30
            self.log('next url:' + self.url + str(self.offset))
            req2 = scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)
            yield req2

    def parse_item(self, response):
        item = SunspiderItem()
        print(response.url)
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[1]/text()').extract()[0]
        item['number'] = \
        response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[2]/text()').extract()[0].strip().split(':')[-1]
        item['detail_url'] = response.url
        temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0]
        temps = temp.split(' ')
        item['author'] = temps[0].split('：')[-1].strip()
        item['pub_date'] = temps[1].split('：')[-1].strip()
        content = response.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"]//text()').extract()[0]
        if len(content) > 0:
            item['content'] = ''.join(content)
        else:
            item['content'] = '空'
        yield item
