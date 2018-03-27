# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest


class ZhihuhpSpider(CrawlSpider):
    name = 'zhihuhp'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
