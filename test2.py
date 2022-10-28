import datetime
import os
import re
import time

from kafka import KafkaProducer

# tt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(tt)
# print(type(tt))
#
# print(type(datetime.datetime.now()))
# a = datetime.datetime.now()
# print(a)
# # b = a.strftime()
# b = a.strftime("%Y%M%D%H%M%S")
# print(b)
# print(type(b))
#
# date = datetime.datetime(2022, 12, 2)
# date2 = datetime.datetime(2022, 2, 2, 22, 3, 22)
# print(date)
# print(date2)

# aa = '2121-5-6 22:22:22'
# bb = datetime.datetime.strptime(aa, "%Y-%m-%d %H:%M:%S")
# print(bb)

# re.sub的第一个参数里面可以用 .*?
# text = '<div class="i like"><a><img src="https://www.baidu.com"/>可爱的人</a></div>'
# result = re.sub('class=".*?"'," ",text)
# print(result)

# print(os.path.dirname(__file__))

text = '<img title="资料图：特斯拉汽车首席执行官马斯克。\n&lt;a target=\'_blank\' href=\'/\'&gt;中新社&lt;/a&gt;发 盛佳鹏 摄" src="//image1.chinanews.com.cn/cnsupl136313376e14a709811ca070a4b4f0c.jpg" alt="资料图：特斯拉汽车首席执行官马斯克。\n&lt;a target=\'_blank\' href=\'/\'&gt;中新社&lt;/a&gt;发 盛佳鹏 摄">'
print(text)
text11 = re.sub('\n', '', text)
print(text11)
raw_text = r'{}'.format(text)
print(raw_text)
alt_regex = 'alt="(.*)"'
alt = re.findall(alt_regex, text11)
print("alt", alt)