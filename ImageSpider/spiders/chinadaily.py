import json
import re
import time

import scrapy
from scrapy import Request

from ImageSpider.items import BbsItem
from ImageSpider.settings import USER_AGENT


class ChinadailySpider(scrapy.Spider):
    name = 'chinadaily'
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
                # break


    def first_parse(self, response):
        print(response.meta['type'], end=" ")
        if response.status == 200:
            # print(response.text)  # body > div.topNav
            selectors = response.xpath('/html/body/div[@class="topNav2_art"]/ul/li')
            # print(len(selectors))
            for sel in selectors:
                href = sel.xpath('./a/@href').extract()[0]
                url_front = "http:"
                second_url = url_front + href
                print("second_url*******")
                print(second_url)
                second_type = sel.xpath('./a/text()').extract()[0]
                yield Request(url=second_url, callback=self.second_parse, meta={'url':second_url, 'first_type':type, 'type':second_type})
                # break

    def second_parse(self, response):
        # print(response.meta['type'], end=" ")
        selectors = response.xpath('//div[@class="main_art"]/div[@id="lft-art"]/div[@class="mb10 tw3_01_2"]')
        for sel in selectors:
            url_front = "http:"
            href = sel.xpath('./span[@class="tw3_01_2_p"]/a/@href').extract()[0]
            detail_url = url_front + href
            print("细节url：", end="")
            print(detail_url)
            yield Request(url=detail_url, callback=self.detail_parse, meta={'url':detail_url, 'first_type':response.meta['first_type']})
            # break

    def detail_parse(self, response):
        # print(response.text)
        # print("helloworld")
        selector = response.xpath('//div[@class="main_art"]/div[@class="lft_art"]')
        # 标题
        title_x = selector.xpath('./h1/text()').extract()
        # if len(title_x) == 0:
        #     return
        title = title_x[0]
        print("标题", end="")
        print(title)


        info = selector.xpath('./div[@class="info"]/span[@class="info_l"]/text()').extract()[0]
        info_list = [i.strip() for i in info.split("|")]
        author = ""
        if len(info_list) == 3:
            # 作者
            author = re.sub('By', "", info_list[0]).strip()
            # print(author)
            # 数据源
            source = info_list[1]
            # print(source)
            # 发布时间
            updated_time = info_list[2].split("Updated:")[-1]
            # print(updated_time)
            # print(author, source, updated_time)
        elif len(info_list) == 2:
            # 数据源
            source = info_list[0]
            # print(source)
            # 发布时间
            updated_time = info_list[-1].split("Updated:")[-1]
            # print(updated_time)
            # print(source, updated_time)
        # 内容
        p_list = selector.xpath('./div[@id="Content"]/p/text()').extract()
        content = ""
        for p in p_list:
            content += p
            content += '\n'

        # print(content)
        item = {}
        item['_id'] = title+'/'+author
        item['title'] = title
        item['author'] = author
        item['publishdate'] = updated_time
        # item['channel'] = response.meta['first_type']
        # item['url'] = response.meta['url']
        item['content'] = content
        # item['fetchtime'] = int(time.time())

        # print(item)
        yield item










