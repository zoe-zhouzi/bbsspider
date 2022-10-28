import json
import re

import scrapy
from scrapy import Request

from ImageSpider.items import BbsItem
from ImageSpider.settings import USER_AGENT


class NewsSpider(scrapy.Spider):
    name = 'jrtt'
    # start_urls =  "https://www.toutiao.com/?wid=1665818574739"

    def __init__(self):
        self.cookie = "__ac_signature=_02B4Z6wo00f010DUlJwAAIDD2L8D7xX2jNtA9JAAALOK7b; tt_webid=7154636261922391582; ttcid=fdfae0322c3c4fffaa429829124e668e12; local_city_cache=北京; _tea_utm_cache_24=undefined; MONITOR_WEB_ID=02a8e274-2973-4cd2-9d2a-f9b5067e018a; csrftoken=b5b1c8ed87f8f1a4ea264df06383f7a8; s_v_web_id=verify_l99ldfky_Kf2L36th_OMoX_4NUP_9CKZ_c4F5ez13ppdQ; msToken=fn80ZuEAraOg-k3d5o8wWg-Cwmph9v2nTckoDocr7Qx8k210MVt-M-qzlP3pKlWytXXLEjf6YUbnyyZ2VLTpQ-ySI9IpdiLKo1kuqknwej8=; ttwid=1|sILfO3ZmH0Y-y7fEqdsqWdfp4-HPbdxXP4tRzbxdKq0|1665822002|e1dfb81fcdc2c6f3cdf5ef9e76bbf80d9fe869ef166ac8c1a2aa7a914779670e; tt_scid=8kxdyHMRWgPvrUcAle6rYahGHZyenp1SFFGvga3m-e6CPNc-uAMz9RYOezgnOPLEe2fb"
        self.header = {
            "user-agent": USER_AGENT,
            "Host": "www.toutiao.com",
            "cookie": self.cookie,
        }

    def start_requests(self):
        url = "https://www.toutiao.com/article/7152151234139456035/?log_from=4827ee13844ce_1665825249574"

        # url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00f01D-3Z2AAAIDAp9zwE2Ry4tw.k2PAAGyu0L324TcoXPLh9FNqNzKKBPHXRVrundjGJi3c2td9i9sFcqTFrcZIPRepIfoei3YPlEsyuiT3EXblE7kj2hPUzgMvbzkhGwLNDAlQ65"
        # 因为我只需要爬取一个网页就行，这里我不需要再返回的到这个函数，因此直接用的return
        yield Request(url=url, headers=self.header)

    def parse(self, response):
        if response.status == 200:
            print(response.text)
            # json_response = json.loads(response.text)
            # hotboard_list = json_response['data']
            # print(len(hotboard_list))  # 50
            # for hotboard in hotboard_list:
            #     if hotboard['Label'] != 'live':
            #         url = hotboard['Url']
            #         yield Request(url=url, callback=self.detail_parse ,headers=self.header)


    # def detail_parse(self, response):
    #     detail_data = response.text
    #     print(detail_data)
    #     head_title = detail_data.xpath("/html/head/title/text()").extract()[0]
    #     if head_title != "":
    #         print("执行到这里了")
    #     print("页面标题", end="")
    #     print(head_title)