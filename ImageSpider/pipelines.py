import datetime
import json
import os
import time

import pandas as pd
import pymongo
import redis
import scrapy
from kafka import KafkaProducer


class ImagespiderPipeline:

    def process_item(self, item, spider):
        return item
    
    def get_image_requests(self, item, info):
        print("开始下载")
        return scrapy.Request(item['url'], meta={'item':item})

    def image_completed(self, request, response=None, info=None):
        base_path = os.path.split(os.path.realpath(__file__))[0]
        folder = "image"
        path = os.path.join(base_path, folder)
        current_time = int(time.time())
        filename = str(current_time)
        with open(path+"/"+folder+filename+".jpeg", "wb") as f:
            f.write(response.content)
        return path

class BbsspiderPipeline:
    def __init__(self):
        self.bbs_key = "bbs:result"
        # redis连接
        redis_host = "127.0.0.1"
        redis_port = "6379"
        redis_schedule_database = 8
        redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=redis_schedule_database)
        self.client = redis.Redis(connection_pool=redis_pool, decode_responses=True)

    def process_item(self, item, spider):
        # mongodb正确连接方法
        # db_name = "media_resp"
        # client = pymongo.MongoClient('mongodb://mediadba:mediadb2k@172.17.33.225/media_resp')
        # db = client[db_name]
        # collection = db['bbt_test_zzy1']
        # collection.insert_one(item)

        # kafka的正确连接方法
        # producer = KafkaProducer(
        #     bootstrap_servers='172.17.33.136:2181',
        #     value_serializer=lambda v: json.dumps(v).encode('utf-8')
        # )
        # producer.send('test_20221017', item)

        _push_data = json.dumps(item, ensure_ascii=False)
        self.client.lpush(self.bbs_key, _push_data)
        return item


class Bbs2spiderPipeline:
    def process_item(self, item, spider):
        item = self.data_format(item)
        print(item)
        # 'localhost:9092'
        # '172.17.33.136:9092'
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send('test', item)
        return item

    def data_format(self, item):
        # temp =  item['data'][0]
        new_item = {}
        # new_item['customerId'] = temp['user_id']+'/'+temp['nickname']
        # new_item['dataType'] = "String"
        # new_item['title'] = temp['title']
        # new_item['author'] = ""
        # new_item['channerl'] = ""
        # new_item['publishdate'] = temp['create_time']
        # new_item['url'] = item['url']
        # new_item['SourceID'] = 2  # 假设2是论坛数据
        # new_item['sourceName'] = "水木论坛"
        # new_item['sentiment'] = 0
        # new_item['contentid'] = ""
        # new_item['OrgSourceName'] = ""
        # new_item['content'] = ""
        new_item['reply'] = item['data']
        # print(item['data'])
        # new_item['fetchtime'] = item['fetchtime']
        # new_item['newsType'] = 0
        # new_item['areacode'] = ""
        # new_item['imgs'] = []
        # new_item['alertWords'] = []
        # new_item['hitcount'] = 0
        # new_item['filtered'] = "false"
        # new_item['hitsubids'] = []
        # new_item['authorcode'] = ""
        # new_item['refcontent'] = ""
        # new_item['comtcount'] = 0
        # new_item['transfercount'] = 0
        # new_item['transferurl'] = ""
        # new_item['appsource'] = 0
        # new_item['stmscore'] = 0
        # new_item['commenturl'] = ""
        # new_item['weibotype'] = 0
        # new_item['headimg'] = ""
        # new_item['geo'] = ""
        # new_item['place'] = ""
        # new_item['address'] = ""
        # new_item['verify'] = 0
        # new_item['verified_type'] = -1
        # new_item['gender'] = ""
        # new_item['fansCount'] = 0
        # new_item['followCount'] = 0
        # new_item['weibocount'] = 0
        # new_item['appsourceName'] = ""
        # new_item['appsourceUrl'] = ""
        # new_item['playNum'] = 0
        # new_item['cmtNum'] = 0
        # new_item['area'] = ""
        # new_item['playhtml'] = ""
        # new_item['datatype'] = 0
        # new_item['prob'] = 0
        # new_item['refDate'] = ""
        return new_item



class NewsspiderPipeline:
    def process_item(self, item, spider):
        # mongodb
        # db_name = "media_resp"
        # client = pymongo.MongoClient('mongodb://mediadba:mediadb2k@172.17.33.225/media_resp')
        # db = client[db_name]
        # collection = db['new_test_z3']
        # collection.insert_one(item)

        # kafka
        producer = KafkaProducer(
            bootstrap_servers='172.17.33.136:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        item_new = item
        # item_new = self.data_format(item)
        print(item_new)
        producer.send('test', item_new)
        return item


    def data_format(self, item):
        new_item = {}
        # new_item['customerId'] = item['user_id'] +'/'+item['nickname']
        # new_item['dataType'] = "String"
        # new_item['title'] = item['title']
        # new_item['author'] = ""
        # new_item['channerl'] = ""
        # new_item['publishdate'] = item['create_time']
        # new_item['url'] = ""
        # new_item['SourceID'] = 2  # 假设2是论坛数据
        # new_item['sourceName'] = "水木论坛"
        # new_item['sentiment'] = 0
        # new_item['contentid'] = ""
        # new_item['OrgSourceName'] = ""
        # new_item['content'] = ""
        new_item['reply'] = item['data']
        # new_item['fetchtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # new_item['newsType'] = 0
        # new_item['areacode'] = ""
        # new_item['imgs'] = []
        # new_item['alertWords'] = []
        # new_item['hitcount'] = 0
        # new_item['filtered'] = "false"
        # new_item['hitsubids'] = []
        # new_item['authorcode'] = ""
        # new_item['refcontent'] = ""
        # new_item['comtcount'] = 0
        # new_item['transfercount'] = 0
        # new_item['transferurl'] = ""
        # new_item['appsource'] = 0
        # new_item['stmscore'] = 0
        # new_item['commenturl'] = ""
        # new_item['weibotype'] = 0
        # new_item['headimg'] = ""
        # new_item['geo'] = ""
        # new_item['place'] = ""
        # new_item['address'] = ""
        # new_item['verify'] = 0
        # new_item['verified_type'] = -1
        # new_item['gender'] = ""
        # new_item['fansCount'] = 0
        # new_item['followCount'] = 0
        # new_item['weibocount'] = 0
        # new_item['appsourceName'] = ""
        # new_item['appsourceUrl'] = ""
        # new_item['playNum'] = 0
        # new_item['cmtNum'] = 0
        # new_item['area'] = ""
        # new_item['playhtml'] = ""
        # new_item['datatype'] = 0
        # new_item['prob'] = 0
        # new_item['refDate'] = ""
        return new_item
        # return item


class TestPipeline:
    def process_item(self, item, spider):
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        item_new = item
        # item_new['test'] = ['a', 'b']
        item_new['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(item_new)
        producer.send('test', item_new)
        return item








