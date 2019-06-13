# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from sun.sun.items import SunItem

class SunspiderSpider(RedisSpider):
    name = 'sunSpider'
    redis_key = "sunSpider:start_urls"

    def parse(self, response):
        item = SunItem()
        title = response.xpath("//div[@class='pagecenter p3']//strong[@class='tgray14']/text()")
        item["title"] = title.extract()[0]
        yield item
