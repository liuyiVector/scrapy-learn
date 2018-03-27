# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from doubanmovie.items import DoubanmovieItem
from scrapy.selector import Selector


class DBMSpider(CrawlSpider):
    # 爬虫名称，运行的时候用到
    name = "doubanMovie"
    # 允许的域名
    allowed_domains = ["movie.douban.com"]
    # 爬虫的种子地址，即第一个地址
    start_urls = [
        "https://movie.douban.com"
    ]
    #该spider将从https://movie.douban.com的首页开始爬取，获取subject的链接后使用parse_item方法。
    rules = (
        # 这里会将符合r'/subject/\d+/'这个正则的地址的网页用parse_subject这个方法解析
        Rule(LinkExtractor(allow=(r'/subject/\d+/',)),callback='parse_subject',follow=True),
    )

    # 这里可以用xpath或者css选择器来获取内容，直接用chrome开发者工具就可以了
    def parse_subject(self, response):
        item = DoubanmovieItem()
        # todo extract item content
        item['movie_name'] = response.xpath('//*[@id="content"]/h1/span[1]').xpath('normalize-space(string(.))').extract()[0]
        item['intro'] = response.xpath('//*[@id="link-report"]/span').xpath('normalize-space(string(.))').extract()[0]
        item['actors'] = response.xpath('//*[@id="info"]/span[3]/span[2]').xpath('normalize-space(string(.))').extract()
        item['date'] = response.xpath('//*[@id="info"]/span[11]').xpath('normalize-space(string(.))').extract()[0]
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a').xpath('normalize-space(string(.))').extract()[0]
        return item