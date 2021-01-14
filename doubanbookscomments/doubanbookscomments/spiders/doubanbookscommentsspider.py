import scrapy, bs4
from ..items import DoubanbookscommentsItem

class DoubanbookscommentsSpider(scrapy.Spider):
    name = 'doubanbookscomments'
    #allowed_domains = ['https://book.douban.com/']
    start_urls = []
    for i in range(2):
        page = 'https://book.douban.com/top250?start='+str(i*25)
        start_urls.append(page)


    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('tr', class_= 'item')
        for book in books:
            url = book.find('a')['href']
            comments_url = url + 'comments/'
            print(comments_url)
            print('找到一本书啦！')
            yield scrapy.Request(comments_url, callback = self.find_comments)
            
    def find_comments(self, response):
        print('开始抓取评论！')
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        title = bs.find('div', id='content').find('h1').text
        comments = bs.find('div', id = 'comments')
        comments = comments.find_all('div', class_='comment')
        for comment in comments:
            item = DoubanbookscommentsItem()
            item['booktitle'] = title
            item['ID'] = comment.find_all('a')[1].text
            item['comment'] = comment.find('span', class_='short').text
            print('找到评论啦！')
            yield item