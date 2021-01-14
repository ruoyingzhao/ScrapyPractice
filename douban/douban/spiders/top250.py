import scrapy
import bs4
#从上一级的items文件夹里引入DoubanItem
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    #爬虫的名字
    name = 'doubanbooksinfo'
    #只允许爬虫访问book.douban.com域名下的url
    allowed_domains = ['book.douban.com']
    #定义爬虫的起始网址，从这个网站开始抓取
    start_urls = []
    for x in range(5):
        url = 'https://book.douban.com/top250?start=' + str(x*25)
        start_urls.append(url)
        print('找到一页书啦！')

    #定义parse函数来解析爬到的response对象的数据    
    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('tr', class_= 'item')
        for i in data:
            #建立一个DoubanItem对象
            item = DoubanItem()

            #标题
            item['title'] = i.find_all('a')[1]['title']
            #出版信息
            item['info'] = i.find('p', class_='pl').text
            #评分
            item['score'] = i.find('span', class_= 'rating_nums').text

            try:
                item['summary'] = i.find('span', class_= 'inq').text
            except:
                item['summary'] = '暂无图书简介'

            print(item['title'], ' 爬取完成。')
            #用yield把获得的item传给引擎
            yield item