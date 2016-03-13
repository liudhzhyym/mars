#!/usr/bin/python
# -*- coding: utf-8 -*-

## zara抓取程序，需要输入版本号 scrapy crawl zara -a taskId=1

import scrapy
import re
import json
import urlparse
import base64
import time
import copy
import common
import sys

from lib.common import Common
from scrapy import log
from goods.items import ProductInfo
from goods.items import SkuInfo
from goods.items import ImageInfo
from goods.items import UrlInfo
from goods.items import logInfo

class iwencaiSpider(scrapy.Spider):
    name = "wencai"
    allowed_domains = ["iwencai.com"]
    start_urls = [
        "http://www.iwencai.com/",
    ]
    source_currency = "RMB"
    picType = "jpg"
    debug = "true"
    taskId = -1
    commonLib = False
    env_type = "offline"

    def __init__(self, *args, **kwargs):

        self.commonLib = Common()
        self.env_type = self.commonLib.get_env()
        if self.env_type == "online":
            self.debug = ""
        self.commonLib.set_header("env_type",self.env_type)
        self.commonLib.set_header("debug",self.debug)
        self.commonLib.write_log("get task id is [%s]" % (self.taskId))

    def parse(self, response):
        # ## 打折

        try:        
            expectCnt = 1
            actualCnt = 0

            top_bar_list = ["男婴","女婴","男童","女童"]
            urlStatus = common.STATUS_DONE

            url = "http://www.iwencai.com/stockpick/search?typed=0&preParams=&ts=1&f=1&qs=1&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=2015%E5%B9%B46%E6%9C%8828%E6%97%A5%E6%B6%A8%E5%B9%85%E5%A4%A7%E4%BA%8E2%25%E5%B0%8F%E4%BA%8E5%25%EF%BC%9B2015%E5%B9%B46%E6%9C%8828%E6%97%A5%E7%9A%84%E6%8D%A2%E6%89%8B%E7%8E%87%E5%B0%8F%E4%BA%8E2%25%EF%BC%9B2015%E5%B9%B46%E6%9C%8828%E6%97%A5kdj%E9%87%91%E5%8F%89"
            request = scrapy.Request(url, callback=self.parse_product_detail)
            yield request

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_FATAL,response.url,self.name)
        finally:
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_HOME,expectCnt,actualCnt,urlStatus)


    def parse_product_detail(self, response):
        try:         

            self.commonLib.write_log("parse_product_detail url is [%s]" % (response.url))


            productDataStr = response.xpath('//script').re("var allResult = (.*);")[0].strip()
            print "productDataStr is ",productDataStr
            productData = json.loads(productDataStr)
            print "productData is ",productData


        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
        finally:
            self.commonLib.write_log("done")

