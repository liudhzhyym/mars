# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import MySQLdb
import httplib
import urllib
import json
import os
import requests
import scrapy
import base64
import md5
import shutil
import spiders.common

from lib.common import Common
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy import settings
from scrapy.utils.project import get_project_settings
from urllib import unquote

settings = get_project_settings()

class GoodsPipeline(ImagesPipeline):
        

    def item_completed(self, results, item, info):

        commonLib = Common()
        
        item_data = {}
        for key,value in item.items():
            item_data[key] = value

        itemType = item_data.pop("itemType")
        if itemType == spiders.common.TYPE_STOCK:
            url = '/api/stock/addStock'
            # stock = {
            #     "code" : item['code'],
            #     "day" : item['day'],
            #     item['query'] : item['value'],
            # }
            post_data = {
                "stock" : item_data,
                "col" : 'qq',
            }
            commonLib.http_post(url,post_data)
            print "this is a stock"
        else:
            print "unknow item type"
        return item

