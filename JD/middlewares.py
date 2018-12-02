# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
import time
from scrapy.http import HtmlResponse

class JdDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        '''无窗口化启动'''
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
    def process_request(self, request, spider):
        print('#'*30 + '中间件' + '*'*30)
        driver = webdriver.Chrome(options=self.options)
        time.sleep(1)
        driver.get(request.url)
        for i in range(5):
            driver.execute_script('window.scrollBy(0,2200)')
            time.sleep(1)
        body = driver.page_source   #取出源码
        return HtmlResponse(url=driver.current_url,body=body,encoding='utf-8',request=request)
