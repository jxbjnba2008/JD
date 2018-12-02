# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem
from scrapy.http import Request

class JdspiderSpider(scrapy.Spider):
    name = 'JDspider'
    allowed_domains = ['search.jd.com']
    i = 1
    url1 = 'https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=3.def.0.V08&wq=kou&stock=1&page='
    url2 = '&s=54&click=0'
    start_urls = [url1 + str(i) + url2]
    
    def parse(self, response):
        temp_list = response.xpath("//*[@id='J_goodsList']/ul/li")
        for temp in temp_list:
            item = JdItem()
            item['name'] = str(temp.xpath('div/div[3]/a/em/text()').extract()).replace("['","").replace("']","")
            item['sales'] = temp.xpath('div/div[4]/strong/a/text()').extract()[0]
            item['price'] = temp.xpath('div/div[2]/strong/i/text()').extract()[0]
            yield item

        if self.i<100:
            self.i = self.i + 2
        url = self.url1 + str(self.i) + self.url2
        yield Request(url,callback=self.parse)
