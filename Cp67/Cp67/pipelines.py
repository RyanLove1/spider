# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
import pymysql

from .settings import *


class Cp67Pipeline(object):
    def process_item(self, item, spider):
        # print(item)
        return item


class Cp67MysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = "insert into news (title,keysword,content,category,`desc`,img) values(%s,%s,%s,%s,%s,%s)"
        job_list = [
            item['title'], item['keysword'], item['content'], item['category'], item["desc"], item["img"]
        ]
        self.cursor.execute(ins, job_list)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
