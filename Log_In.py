# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
import logging
from scrapy.http import FormRequest,Request
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


        News_Headline = response.css('.story').css('::text').extract()
        News_date = response.css('time::text').extract()
        News_Author = response.css('.p > a').css('::text').extract()



        items['News_Headline'] = News_Headline
        items['News_Author'] = News_Author
        items['News_date'] = News_date

        yield items














