# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_name = scrapy.Field()
    image_path = scrapy.Field()
