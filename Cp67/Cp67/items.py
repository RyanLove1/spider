# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Cp67Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 关键字
    keysword = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 分类
    category = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    # 图片
    img = scrapy.Field()
