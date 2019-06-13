# -*- coding: utf-8 -*-
import scrapy
from ..items import JobspiderItem


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['51job.com']
    start_urls = [
        'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare',
    ]

    def parse(self, response):
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        item = JobspiderItem()
        for job in job_list:
            name = job.xpath('normalize-space(./p/span/a/text())').extract()[0]
            item['name'] = name
            yield item

