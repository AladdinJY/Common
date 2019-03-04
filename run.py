# -*- coding: utf-8 -*-
from JobSpider.spiders.lagou import LagouSpider

__author__ = 'Aladdin'
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置


settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider类
# process.crawl(Spider1)
# process.crawl(Spider2)
process.crawl(LagouSpider)

# 启动爬虫，会阻塞，直到爬取完成
process.start()