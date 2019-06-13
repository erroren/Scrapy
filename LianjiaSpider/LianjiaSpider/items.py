# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    communtity_name = scrapy.Field()
    area = scrapy.Field()
    basic_message = scrapy.Field()
    original_message = scrapy.Field()


