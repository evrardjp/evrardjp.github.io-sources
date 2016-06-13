#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Check if the links are completely borked.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import config
import custom_depth_mw

class BorkenItem(Item):
    url = Field()
    referer = Field()
    status = Field()

class BorkenLinks(CrawlSpider):
    name = 'borkenlinks'
    handle_httpstatus_all = True
    start_urls = config.start_urls
    download_delay = config.download_delay
    custom_settings = config.custom_settings

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if response.status >= 300:
            item = BorkenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status
            return item