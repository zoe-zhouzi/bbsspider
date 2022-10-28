# from kafka import KafkaProducer;
# import json;
#
# producer = KafkaProducer(
#     security_protocol="SSL",
#     value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#     bootstrap_servers=['172.17.33.136:2181'],
#     api_version=(0,11)
# )
# msg_dict = {
#     "operatorId": "test",  # 公交公司ID
#     "terminalId": "123",  # 设备Id
#     "terminalCode": "123",  # 设备编码（使用车辆ID）
#     "terminalNo": "1",  # 同一车辆内terminal序号从1开始
# }
#
# producer.send("test_20221017", msg_dict)
# producer.close()


# from kafka import KafkaProducer
# producer = KafkaProducer(security_protocol="SSL",bootstrap_servers='172.17.33.136:9092',api_version=(0,11))
# for _ in range(100):
#     producer.send('test',b'some_message_bytes')

from kafka import KafkaProducer
from kafka.errors import KafkaError

# security_protocol="SSL",  api_version=(0,11)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Asynchronous by default
future = producer.send('test', b'world is nice, peace')

