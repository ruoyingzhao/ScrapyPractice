# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl

class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['图书','出版信息','评分','简介'])

    def process_item(self, item, spider):
        line = [item['title'], item['info'], item['score'], item['summary']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('./doubanbooks.xlsx')
        self.wb.close()