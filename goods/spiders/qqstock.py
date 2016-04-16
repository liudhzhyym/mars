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
import urllib
import conf.stock as stockConf

from urllib import urlencode
from lib.common import Common
from scrapy import log
from goods.items import stockInfo

class qqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["qq.com","data.gtimg.cn"]
    start_urls = [
        #"http://data.gtimg.cn/flashdata/hushen/daily/14/",
        "http://stockapp.finance.qq.com/mstats/",
    ]

    debug = ""
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
        try:        

            stockList = stockConf.stockList
            # print stockList
            # return
            for code in stockList:
                #code = "sh601009"
                url = "http://data.gtimg.cn/flashdata/hushen/daily/15/%s.js" % (code)
                request = scrapy.Request(url, callback=self.parse_stock_data)
                request.meta['code'] = code
                yield request

                url = "http://data.gtimg.cn/flashdata/hushen/daily/16/%s.js" % (code)
                request = scrapy.Request(url, callback=self.parse_stock_data)
                request.meta['code'] = code
                yield request

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            print (msgStr)

    def parse_stock_data(self,response):
        try:        
            code = response.meta['code']
            self.commonLib.write_log("start to parse_stock_data [%s] and url is [%s]" % (code,response.url))
            
            #code = code.replace("sz","").replace("sh","")

            codePlace = code[0:2].upper()
            codeNum = code[-6:]
            #print codePlace,codeNum
            #return
            code = codeNum + "." + codePlace

            lineArr = response.body.split("\\n\\")
            dataArr = []
            for line in lineArr:
                #print line
                tempArr = line.split(" ")
                #print tempArr
                if len(tempArr) < 5:
                    continue
                day = "20" + tempArr[0].strip()
                openPrice = tempArr[1].strip()
                closePrice = tempArr[2].strip()
                maxPrice = tempArr[3].strip()
                minPrice = tempArr[4].strip()
                amount = tempArr[5].strip()

                info = {
                    "openPrice" : openPrice,
                    "closePrice" : closePrice,
                    "maxPrice" : maxPrice,
                    "minPrice" : minPrice,
                    "amount" : amount,
                }
                for key,value in info.items():
                    stock =  stockInfo()
                    stock['itemType'] = common.TYPE_STOCK
                    stock['code'] = code
                    stock['day'] = day
                    stock['query'] = key
                    stock['value'] = value
                    yield stock
                # stock =  stockInfo()
                # stock['itemType'] = common.TYPE_STOCK
                # stock['code'] = code
                # stock['day'] = day
                # yield stock

                #print day,openPrice,closePrice,maxPrice,minPrice,amount
            #print lineArr

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            print (msgStr)         


