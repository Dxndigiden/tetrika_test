# Scrapy settings for wik_animals project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "wik_animals"

SPIDER_MODULES = ["wik_animals.spiders"]
NEWSPIDER_MODULE = "wik_animals.spiders"

ADDONS = {}

ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = "utf-8"
