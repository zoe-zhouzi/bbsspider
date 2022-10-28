import scrapy
from scrapy import Request


class ChinadailySpider(scrapy.Spider):
    name = 'chinatest'
    start_urls =  ["http://www.chinadaily.com.cn/",]

    def parse(self, response):
        if response.status == 200:
            selectors = response.xpath('/html/body/div[@class="topNav"]/ul/li')
            for sel in selectors:
                url_front = "http:"
                type = sel.xpath('./a/text()').extract()[0]
                if type == "HOME" or type =="WATCHTHIS" or type == "REGIONAL" or type == "FORUM" or type == "NEWSPAPER" or type=="MOBILE":
                    continue
                print("*********")
                print(type)
                print("*********")
                href = sel.xpath('./a/@href').extract()[0]
                type_url = url_front + href
                yield Request(url=type_url, callback=self.first_parse, meta={'url':type_url, 'type':type})
                break