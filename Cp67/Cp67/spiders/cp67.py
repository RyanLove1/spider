# -*- coding: utf-8 -*-
import re

import scrapy
import time

from ..settings import *
from ..items import Cp67Item


# from scrapy_redis.spiders import RedisSpider

class Cp67Spider(scrapy.Spider):
    name = 'cp67'
    allowed_domains = ['www.cp67.com']
    start_urls = [MODULE_URL,]
    # redis_key = 'cp67:spider'

    # 解析一级页面获取二级链接
    def parse(self, response):
        two_links = response.xpath("//div[@class='grid box']/h5/a/@href").extract()
        for two_link in two_links:
            yield scrapy.Request(url=two_link, meta={"two_link": two_link}, callback=self.parse_two_link,
                                 dont_filter=True)

    # 处理二级链接
    def parse_two_link(self, response):
        link = response.meta["two_link"]
        # 获取二级链接后面拼接的内容
        list_str = response.xpath('//*[@id="pages"]/ul/li[2]/a/@href').extract_first()
        list_number = list_str.split('_')[0] + "_" + list_str.split('_')[1]
        two_url = link + list_number + "_{}.html"
        for item in range(PAGE_NUM):
            new_two_url = two_url.format(item + 1)
            yield scrapy.Request(url=new_two_url, callback=self.parse_three_link, dont_filter=True)

    # 获取三级页面链接
    def parse_three_link(self, response):
        three_links = response.xpath('//li/a[@class="title"]/@href').extract()
        print(three_links)
        for three_link in three_links:
            yield scrapy.Request(url=three_link, callback=self.parse_four_link, dont_filter=True)

    # 获取三级页面内容
    def parse_four_link(self, response):
        item = Cp67Item()
        item["title"] = response.xpath('//h1[@class="h1"]/center/text()').extract_first()
        item["desc"] = response.xpath('//div[@class="summary"]/text()').extract_first()
        # content = response.xpath('//div[@class="content_z"]/p/text()').extract()
        # join_content = "\n".join(content)
        # item["content"] = join_content
        html_content = response.text
        # print(html_content)
        pattern = re.compile('<div class="C_1nr">(.*?)</div>', re.S)
        r_list = pattern.findall(html_content)[0]
        item["content"] = r_list
        item["img"] = response.xpath('//p[@style="text-align: center;"]/img/@src').extract_first()
        # 相关热词列表
        ci_list = response.xpath('//div[@class="xg_rc"]/p/a/text()').extract()
        # 二级标题
        two_title_list = response.xpath('//div[@class="crumbs"]/a/text()').extract()
        two_title = two_title_list[-1]
        if two_title not in ci_list:
            ci_list.append(two_title)
        item["keysword"] = ','.join(ci_list)
        item['category'] = CATEGORY
        yield item
