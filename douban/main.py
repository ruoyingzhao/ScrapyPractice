from scrapy import cmdline
#导入cmdline模块可以实现控制终端命令行

#用execute()方法， 输入运行scrapy的命令
#在真正的终端可以跳转到本项目的文件件内
#然后打 scrapy crawl douban开始爬取
#在这里要写成列表格式
cmdline.execute(['scrapy', 'crawl', 'doubanbooksinfo'])
