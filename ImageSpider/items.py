import scrapy


class ImagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # image_name = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    tag = scrapy.Field()

class BbsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    pubDate = scrapy.Field()
    # guid = scrapy.Field()
    comments = scrapy.Field()
    description = scrapy.Field()