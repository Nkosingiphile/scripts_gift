# -*- coding: utf-8 -*-
import scrapy

from ..items import SlashdotMediaNewsItem

class LogInSpider(scrapy.Spider):
    name = 'media'

    start_urls = ['https://slashdot.org/login.pl/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'uickname': 'GiftMamba', 'upasswd': 'NNkosingiphile#12'},

            callback=self.log_In
        )


    def log_In(self, response):

        items = SlashdotMediaNewsItem()
        News_Headline = response.css("span.story-title")

        for data in News_Headline:
            Headline = response.urljoin(data.extract())
            items['News_Headline'] = Headline
            yield items








