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

from urllib import urlencode
from lib.common import Common
from scrapy import log
from goods.items import stockInfo

class iwencaiSpider(scrapy.Spider):
    name = "wencai"
    allowed_domains = ["iwencai.com"]
    start_urls = [
        "http://www.iwencai.com/stockpick",
    ]
    source_currency = "RMB"
    picType = "jpg"
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

            ## 获取技术指标列表
            # for option in response.xpath("//div[@class='area_item']/a[@name='lm_c_jszb']/../div//a[@class='other_link']/@href"):
            #     href = option.extract().strip()

            #     self.commonLib.write_log("get indicator list url is [%s]" % (href))
            #     request = scrapy.Request(href, callback=self.parse_indicator_list)
            #     yield request
                
            #     if self.debug:
            #         self.commonLib.write_log("debug")
            #         return
            day = "2016年03月23日"
            query = "MACD金叉"
            queryStr = day + query

            queryData = {
                "typed" : "1",
                "preParams" : "",
                "ts" : "1",
                "f" : "1",
                "qs" : "result_rewrite",
                "selfsectsn" : "",
                "querytype" : "",
                "searchfilter" : "",
                "tid" : "stockpick",
                "w" : queryStr,
            }
            baseUrl = "http://www.iwencai.com/stockpick/search?"
            queryUrl = baseUrl + urllib.urlencode(queryData)
            #queryUrl = "ts=1&tid=stockpick&queryarea=all&qs=hd_ma_all&w=MACD%E9%87%91%E5%8F%89"
            day = day.replace("年","").replace("月","").replace("日","")
            queryInfo = {
                "day" : day,
                "query" : query,
            }
            request = scrapy.Request(queryUrl, callback=self.parse_indicator_detail)
            request.meta['queryInfo'] = copy.deepcopy(queryInfo)
            yield request
            
        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)


    def parse_indicator_list(self, response):
        try:         
            self.commonLib.write_log("parse_indicator_list url is [%s]" % (response.url))

            indicatorListStr = response.xpath('//script').re("data_item.typeData = ([^;]+);")[0].strip()
            #print "indicatorListStr is ",indicatorListStr
            indicatorList = json.loads(indicatorListStr)
            #print "indicatorList is ",indicatorList

            subList = []
            for option in indicatorList:
                subListArr = option['sub_querys'].split("_")
                subList = subList + subListArr

            for indicator in subList:
                print indicator
            self.commonLib.set_header("subList",subList)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)

        self.commonLib.write_log("finish parse_indicator_list")

    def parse_indicator_detail(self, response):
        try:         
            self.commonLib.write_log("parse_indicator_detail url is [%s]" % (response.url))
            queryInfo = response.meta['queryInfo']
            #codeList = response.meta.get("codeList")
            token = response.meta.get("token")

            day = queryInfo['day']
            query = queryInfo['query']

            if token:
                resultStr = response.body
                result = json.loads(resultStr)
            else:
                resultStr = response.xpath('//script').re("var allResult = ([^;]+);")[0].strip()
                result = json.loads(resultStr)
                token = result['token']
            
            total = int(result['total'])
            currentPage = int(result['page'])
            perpage = 30

            codeList = []
            for option in result['result']:
                code = option[0]
                value = 1

                stock =  stockInfo()
                stock['itemType'] = common.TYPE_STOCK
                stock['code'] = code
                stock['day'] = day
                stock['query'] = query
                stock['value'] = value
                yield stock

                codeList.append(code)

            print "codeList is ",codeList,queryInfo

            self.commonLib.write_log("total is [%s], currentPage is [%s]" % (total,currentPage))

            if currentPage*perpage<total:
                nextPage = currentPage + 1
                params = {
                    'token':token,
                    'p':nextPage,
                    'perpage':perpage,
                    'sort':'{"column":2,"order":"DESC"}',
                    'showType':'["","","onTable","onTable","onTable","onTable"]',
                }

                queryParams = urlencode(params)
                nextUrl = "http://www.iwencai.com/stockpick/cache?" + queryParams
                self.commonLib.write_log("total is [%s], currentPage is [%s], nextPage url is [%s]" % (total,currentPage,nextUrl))
                request = scrapy.Request(nextUrl, callback=self.parse_indicator_detail)
                request.meta['token'] = token
                request.meta['codeList'] = copy.deepcopy(codeList)
                request.meta['queryInfo'] = copy.deepcopy(queryInfo)
                yield request
            else:
                self.commonLib.write_log("finish to parse indicator and list is [%s]" % (json.dumps(codeList)))
        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)

        self.commonLib.write_log("finish parse_indicator_detail")

