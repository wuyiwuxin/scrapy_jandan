# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from jandan.items import Scrapy_jandanItem


class JdspinderSpider(CrawlSpider):
    name = "jdSpinder"
    allowed_domains = ["jandan.net"]
    start_urls = (
        'http://jandan.net/ooxx',
    )

    rules = (
        Rule(LinkExtractor(allow=[]), callback='parse_item'),
    )

    def parse_item(self, response):
		item = JandanItem()
		item['image_urls'] = response.xpath('//img/@src').extract()
		return item