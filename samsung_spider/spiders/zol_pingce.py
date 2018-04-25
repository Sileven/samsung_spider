# -*- coding: utf-8 -*-
import scrapy
from samsung_spider.items import SamsungSpiderItem
from scrapy.selector import Selector

class ZolPingceSpider(scrapy.Spider):
    name = 'zol_pingce'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://mobile.zol.com.cn/682/6825302.html']

    def parse(self, response):
        item=SamsungSpiderItem()
        sel=Selector(response)

        title = sel.xpath('//div[@class="main"]/div[1]/h1/text()').extract()
        text = sel.xpath('//div[@class="main"]/div[@id="article-content"]/div[1]/p/text()').extract()
        print(title,text)
