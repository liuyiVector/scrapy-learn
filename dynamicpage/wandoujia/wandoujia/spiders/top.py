# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector


class WDJSpider(CrawlSpider):
    # 爬虫名称，运行的时候用到
    name = "top"
    # 允许的域名
    allowed_domains = ["wandoujia.com"]
    # 爬虫的种子地址，即第一个地址
    start_urls = [
        "http://www.wandoujia.com/apps",
    ]
    
    rules = (
        # 这里会将符合r'/subject/\d+/'这个正则的地址的网页用parse_subject这个方法解析
        Rule(LinkExtractor(allow=(r'/top/app',)),callback='parse_applist',follow=True),
    )

    def parse_applist(self, response):
        # 提取top列表的应用名称
        apps = response.xpath('//*[@id="j-top-list"]/li/div[2]/h2/a/text()').extract()
        for app in apps:
            print app
        pass
       