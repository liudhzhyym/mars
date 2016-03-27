# -*- coding: utf-8 -*-

# Scrapy settings for goods project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'goods'

SPIDER_MODULES = ['goods.spiders']
NEWSPIDER_MODULE = 'goods.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN=8
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
#COOKIES_ENABLED=True
#COOKIES_DEBUG=True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'goods.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#WEBKIT_DOWNLOADER = ['childrensalon']
DOWNLOAD_TIMEOUT = 30
DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
#    'goods.middlewares.webkitDownloader.WebkitDownloader': 543,
#    'scrapyjs.SplashMiddleware':725,
    'goods.comm.rotate_useragent.RotateUserAgentMiddleware' :400,
    'goods.middlewares.httpMiddlewares.ProxyMiddleware' :100,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware' : 600
    #'goods.middlewares.MyCustomDownloaderMiddleware': 543,
}
DUPEFILTER_CLASS ='goods.comm.seen_url_filter.SeenURLFilter'

#DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
#SPLASH_URL = 'http://127.0.0.1:8050/'
DOWNLOAD_HANDLERS = {'s3': None,}

#import os
#os.environ["DISPLAY"] = ":0"

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
	'goods.extensions.extensions.ExtensionThatAccessStats': 100,
	#'scrapy.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#	'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
	'goods.pipelines.GoodsPipeline': 300,
	#'goods.pipelines.MyImagesPipeline': 301,
}

IMAGES_STORE = '/home/work/image/'
IMAGES_EXPIRES = 15
#LOG_LEVEL = 'INFO'

#LOG_FILE = "log/spider.log"
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
