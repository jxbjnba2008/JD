# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class JdPipeline(object):
    def __init__(self):
        self.client = MongoClient(host='localhost',port=27017)
        self.spider = self.client.JD
        self.col = self.spider.JDdata
    def process_item(self, item, spider):
        self.col.insert({'name':item['name'],'price':item['price'],'sales':item['sales']})
        return item
