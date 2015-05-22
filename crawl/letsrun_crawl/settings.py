# -*- coding: utf-8 -*-

# Scrapy settings for letsrun_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'letsrun_crawl'

SPIDER_MODULES = ['letsrun_crawl.spiders']
NEWSPIDER_MODULE = 'letsrun_crawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'letsrun_crawl (+http://www.yourdomain.com)'