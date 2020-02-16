# -*- coding: utf-8 -*-
import scrapy

# use
# scrapy crawl isinget -t csv -o out.csv -a isinum=/home/dev/workspace/git/hackathon/isin/a


class IsingetSpider(scrapy.Spider):
    name = 'isinget'
    allowed_domains = ['http://www.moner.in']
    def __init__(self, isinum=None, *args, **kwargs):
        super(IsingetSpider, self).__init__(*args, **kwargs)
        with open(isinum,"r") as f:
            for line in f:
                self.start_urls += ['http://www.moner.in/isin/%s' % line]

    def parse(self, response):
        ret_list = []
        for table in response.xpath("//div[@id='leftcolumn']/table[@class='pd']/thead/tr/th/text()").getall():
            if (not ( table == "Isin" or table == "Nominal" or (table == "Name, Description"))):
                ret_list.append(table)
        yield { "ISIN" :ret_list[0], "Name" : ret_list[1] }
