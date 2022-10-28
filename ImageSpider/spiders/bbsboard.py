import json
import re

import scrapy
from scrapy import Request

from ImageSpider.items import BbsItem
from ImageSpider.settings import USER_AGENT


class BbsBoardSpider(scrapy.Spider):
    name = 'bbsboard'

    def __init__(self):
        self.cookie = "__gads=ID=2e5eacb3cc6296c9-2261c537f7d600b1:T=1665475233:RT=1665475233:S=ALNI_MaqneR7ZJFfqi6TxfScgJYb-yczkg; Hm_lvt_3663c777a66d280fdb290b6b9808aff0=1665475233,1665554022; main[XWJOKE]=hoho; __gpi=UID=00000b5ee5cddb6e:T=1665475233:RT=1665555082:S=ALNI_Maxsu8zSQKlxhwB7w6ncTbDRMZmoQ; main[UTMPUSERID]=guest; main[UTMPKEY]=35177226; main[UTMPNUM]=43688; left-index=00100000000; nforum-left=0100; Hm_lpvt_3663c777a66d280fdb290b6b9808aff0=1665582212"
        self.base_url = "https://www.mysmth.net"
        self.card_list = []
        self.header = {
            "user-agent": USER_AGENT,
            "cookie": self.cookie,
        }

    def start_requests(self):
        url = 'https://www.mysmth.net/nForum/mainpage'
        yield Request(url=url, headers=self.header)

    def parse(self, response):
        if response.status == 200:
            # print(response.text)
            base_url = "https://www.mysmth.net"
            selectors = response.xpath('/html/body/section/section/div/div[2]/div[3]/ul/li')

            type = selectors[0].xpath('./div/a[1]/@title').extract()[0]
            # print(type)
            detail = selectors[0].xpath('./div/a[2]/@href').extract()[0]
            detail_url = base_url + detail
            yield Request(url=detail_url, callback=self.detail_parse, headers=self.header)
            # for sel in selectors:
            #     type = sel.xpath('./div/a[1]/@title').extract()[0]
            #     # print(type)
            #     detail = sel.xpath('./div/a[2]/@href').extract()[0]
            #     detail_url = base_url + detail
            #     # print(detail_url)
            #     yield Request(url=detail_url, callback=self.detail_parse, headers=self.header)
        else:
            print("响应码错误")

    def detail_parse(self, response):
        # 正则解析，但是遇到很多问题
        data = response.text
        regex = '<table.*?>.*?</table>'
        table_list = re.findall(regex, data)
        for table in table_list:
            print("************")
            card = {}
            floor_x = '<span.*?class="a-pos">(.*?)</span>'
            floor = re.findall(floor_x, table)[0]
            card['floor'] = floor
            regex = "<p.*?></p>"
            p_data = re.findall(regex, table)[0]
            result = re.sub("<br.*?/>", "\n", p_data)
            result2 = result.split("--")[0]
            result3 = re.sub('&nbsp;|&nbsp;&nbsp;\n|&nbsp;&nbsp;', '', result2)
            result4 = re.sub('<.*?>|</.*?>', '', result3)
            data_temp = result4.split('\n')
            # 第一个元素
            user_info = data_temp[0]
            # 用户id
            user_id_x = re.search(':(.*?)\(', user_info)
            user_id = user_id_x.group(1).strip()
            card['user_id'] = user_id
            # 用户名
            nickname_x = re.search('\((.*?)\)', user_info)
            nickname = nickname_x.group(1).strip()
            card['nickname'] = nickname

            # 第二个元素
            title_info = data_temp[1].strip()
            title_x = re.search(':(.*)', title_info)
            # 标题
            title = title_x.group(1).strip()
            card['title'] = title

            # 第三个元素
            time_info = data_temp[2]
            create_time_x = re.search('\((.*?)\)',time_info)
            create_time = create_time_x.group(1)
            card['create_time'] = create_time

            # 第四个元素
            content_info = data_temp[3:-1]
            # 内容
            content = ""
            for content_i in content_info:
                if content_i != '':
                    content += content_i.strip()
                    content += '\n'
            card['content'] = content
            print(card)
            yield card
        detail_url_x = '<li class="page-select"><a title="当前页">.*?</a></li><li class="page-normal"><a href="(.*?)" .*?></a></li>'  # <li><a href="(.*?)"></a></li>
        print(detail_url_x)
        detail_url = re.findall(detail_url_x, data)[0]
        # print(detail_url)
        detail_url = re.findall(detail_url_x, data)[0]
        if detail_url != "":
            detail_url = self.base_url + detail_url
            print(detail_url)
            yield Request(url=detail_url, callback=self.detail_parse, headers=self.header)




