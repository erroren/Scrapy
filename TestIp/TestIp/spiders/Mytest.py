# -*- coding: utf-8 -*-
import scrapy
from ..items import TestipItem


class MytestSpider(scrapy.Spider):
    name = 'Mytest'
    # allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        movieList = response.xpath('//ol[@class="grid_view"]/li')
        print(len(movieList))
        for movie in movieList:
            item = TestipItem()
            moviename = movie.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()').extract()
            moviedesc = movie.xpath('normalize-space(.//div[@class="bd"]/p[1]/text())').extract()
            movierate = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()
            moviequote = movie.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            print(moviename[0], moviedesc[0], movierate[0], moviequote[0])
            item['movieName'] = moviename[0]
            item['movieDesc'] = moviedesc[0]
            item['movieRate'] = movierate[0]
            item['movieQuote'] = moviequote[0]
            yield item

