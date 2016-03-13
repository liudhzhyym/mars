#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import copy
from goods.items import UrlInfo
from goods.items import logInfo

## 调起一个url，

TYPE_ITEM = "item"
TYPE_SKU = "sku"
TYPE_LOG = "log"
TYPE_URL = "url"
TYPE_PIC = "pic"

LOG_FATAL = "fatal"
LOG_WARNING = "warning"
LOG_DEBUG = "debug"

LEVEL_HOME = 'home'
LEVEL_CATEGORY1 = 'category1'
LEVEL_CATEGORY2 = 'category2'
LEVEL_PRODUCT_LIST = 'productList'
LEVEL_PRODUCT_DETAIL = 'productDetail'
LEVEL_SKU_SIZE = 'productSize'
LEVEL_SKU_COLOR = 'productColor'
LEVEL_SKU_PRICE = 'productPrice'
LEVEL_SKU_STOCK = 'productStock'

STATUS_NEW = 'new'
STATUS_RUNNING = 'running'
STATUS_DONE = 'done'
STATUS_SUCCESS = 'success'
STATUS_FAIL = 'fail'
STATUS_TIMEOUT = 'timeout'
STATUS_APPROVING = 'approving'
STATUS_DENY = 'deny'

SHOPPING_TASK_ERR = '任务参数错误'
LOGIN_FAILED = "登陆失败"
LOGIN_SUCCEED = "登陆成功"
ADD_CART_FAILED = '加购物车失败'
ADD_CART_SUCCEED = '加购物车成功'
CHECKOUT_FAILED = '生成订单失败'
CHECKOUT_SUCCEED = '生成订单成功'
PAY_FAILED = '支付失败'
PAY_SUCCEED = '支付成功'

def addLog(logDetail,taskId,level,url,sourceWebsite):
    logInfoData = logInfo()
    logInfoData['itemType'] = "log"
    logInfoData['logDetail'] = logDetail
    logInfoData['taskId'] = taskId
    logInfoData['level'] = "FATAL"
    logInfoData['url'] = url
    logInfoData['sourceWebsite'] = sourceWebsite
    return logInfoData

def addUrl(url,taskId,parentUrl,urlLevel,expectCnt,actualCnt,urlStatus):
    ## 添加抓取的url信息
    urlInfoData = UrlInfo()
    urlInfoData["itemType"] = "url"
    urlInfoData["url"] = url
    urlInfoData["taskId"] = taskId
    urlInfoData["parentUrl"] = parentUrl
    urlInfoData["urlLevel"] = urlLevel
    urlInfoData["expectCnt"] = expectCnt
    urlInfoData["actualCnt"] = actualCnt
    urlInfoData["urlStatus"] = urlStatus

    return urlInfoData

def addUrlInfo(url,taskId,parentUrl,urlLevel,urlStatus):
    ## 添加抓取的url信息
    urlInfoData = UrlInfo()
    urlInfoData["itemType"] = "url"
    urlInfoData["url"] = url
    urlInfoData["taskId"] = taskId
    urlInfoData["parentUrl"] = parentUrl
    urlInfoData["urlLevel"] = urlLevel
    urlInfoData["urlStatus"] = urlStatus

    return urlInfoData
