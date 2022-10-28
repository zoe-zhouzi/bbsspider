FROM python:3.9.12
ENV TZ Asia/Shanghai
WORKDIR /ImageSpider

COPY requirements.txt requirements.txt

COPY . /ImageSpider

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip install --upgrade pip \
    && pip install -r requirements.txt


CMD [ "bash", "./resatrt_bbs_spider.sh" ]