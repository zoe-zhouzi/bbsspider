import json

import scrapy
from scrapy import Request

from ImageSpider.items import ImagespiderItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['baidu.com']
    start_urls = ['https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10933962675394535709&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E8%9D%B4%E8%9D%B6&queryWord=%E8%9D%B4%E8%9D%B6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e0000000000001e&1665397267049=']
    # start_urls = ['https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11975259607554728209&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a0000000000005a&1665398921023=']

    # def start_requests(self):
    #     keywords = ['蝴蝶'] # , '笔记本电脑', '键鼠套装']
    #     for keyword in keywords:
    #         # url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1665390718377_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDEsNCw1LDgsNiw3LDIsOQ%3D%3D&ie=utf-8&sid=&word={keyword}'
    #         url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11975259607554728209&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a0000000000005a&1665398921023='
    #         yield Request(url=url)

    def parse(self, response):
        if response.status == 200:
            # print(response.text)
            img_str = json.loads(response.text)
            img_tag = img_str["queryExt"]
            image_list = img_str['data']
            print(img_str)
            count = 0
            for imageObj in image_list:
                if len(imageObj) != 0: # 真实数据只有30条，但是这个对象有31个，最后一个取空，如果不加if会报错
                    item = ImagespiderItem()
                    item['url'] = imageObj['thumbURL']
                    item['type'] = imageObj['type']
                    item['tag'] = img_tag
                    print(item)
                    yield item
        else:
            print("响应码错误")

        # print(json_response)



