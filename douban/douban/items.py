# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#DoubanItem可以以类似字典的形式记录数据
#里面的Field大概相当于字典的keys
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    summary = scrapy.Field()

