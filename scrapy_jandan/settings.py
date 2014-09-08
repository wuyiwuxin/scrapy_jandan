# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_jandan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_jandan'

SPIDER_MODULES = ['scrapy_jandan.spiders']
NEWSPIDER_MODULE = 'scrapy_jandan.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_jandan (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
#COOKIES_ENABLED = True
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = 'D:\workspace\imgoutput'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'