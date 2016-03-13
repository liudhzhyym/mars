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

class zaraSpider(scrapy.Spider):
    name = "zara"
    allowed_domains = ["zara.cn"]
    start_urls = [
        #"http://www.zara.cn/cn/zh/%E5%84%BF%E7%AB%A5-c277007.html",
        "http://www.zara.cn/cn/zh/%E5%84%BF%E7%AB%A5-c359013.html",
    ]
    source_currency = "RMB"
    picType = "jpg"
    debug = "true"
    taskId = -1
    commonLib = False
    env_type = "offline"

    def __init__(self, taskId=None, *args, **kwargs):
        super(zaraSpider, self).__init__(*args, **kwargs)
        #self.start_urls = ['http://www.example.com/categories/%s' % category]
        self.taskId = int(taskId)
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
            assert self.taskId > 0, "taskId [%s] should not be null" % (self.taskId)
            ## //li[@rootid]/ul/li/ul/li

            barList = response.xpath("//li[@class='current selected']/ul/li/a")

            expectCnt = len(barList)
            for category in barList:
                category_url = category.xpath("@href")[0].extract().strip() + "#" + common.LEVEL_HOME
                top_bar_name = category.xpath("text()")[0].extract().strip()
                top_bar = top_bar_name.split(" ")[0].strip()

                actualCnt = actualCnt + 1
                # if top_bar not in top_bar_list:
                #     self.commonLib.write_log("top_bar [%s] is not child category" % (top_bar))
                #     continue
                
                self.commonLib.write_log("top_bar_name is [%s], top_bar is [%s],parse zara url is [%s],actualCnt is [%s] " % (top_bar_name,top_bar,category_url,actualCnt))

                product_info = {}
                product_info['top_bar'] = top_bar
                request = scrapy.Request(category_url, callback=self.parse_category_list)
                request.meta['product_info'] = copy.deepcopy(product_info)
                yield request

            assert actualCnt == expectCnt and expectCnt>0, "parse ActualCnt [%s] is not [equal] expectCnt [%s]" % (actualCnt,expectCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_FATAL,response.url,self.name)
        finally:
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_HOME,expectCnt,actualCnt,urlStatus)

    def parse_category_list(self, response):
        try:         
            product_info = response.meta['product_info']
            ## 有302跳转
            top_bar = product_info['top_bar']
            self.commonLib.write_log("parse_category_list url is [%s]" % (response.url))
            
            #top_bar_list = ["男婴","女婴","男童","女童"]

            ## xpath("contains(@class,'selected')"):
            expectCnt = 5
            actualCnt = 0

            urlStatus = common.STATUS_DONE

            # top_bar = response.xpath("//li[@id='menuItemData_436074']/ul/li[contains(@class,'current')]/a/text()")[0].extract().strip()
            #assert top_bar in top_bar_list, "parse_category_list top_bar [%s] is not in the available bar list" % (top_bar)

            # if pageType == "new":
            #     categoryList = response.xpath("//li[@rootid]/ul/li/ul/li/a")
            # else:
            #     categoryList = response.xpath("//li[@rootid]/ul/li/ul/li/ul/li/a")
            #     
            
            categoryList = response.xpath("//li[@rootid]/ul/li/ul/li/a")

            expectCnt = len(categoryList)
            for category_option in categoryList:
                category_name = category_option.xpath("text()")[0].extract().strip()
                product_list_url = category_option.xpath("@href")[0].extract().strip()
                product_list_url = product_list_url + "#" + common.LEVEL_CATEGORY1
                
                actualCnt = actualCnt + 1
                self.commonLib.write_log("get product_list_url is [%s],top_bar is [%s],category_name is [%s],actualCnt is [%d] " % (product_list_url,top_bar,category_name,actualCnt))

                product_info['top_bar'] = top_bar
                product_info['category_name'] = category_name
                request = scrapy.Request(product_list_url, callback=self.parse_product_list)
                request.meta['product_info'] = copy.deepcopy(product_info)
                yield request

                if self.debug:
                    self.commonLib.write_log("in debug modal")
                    expectCnt = 1
                    break
                    # self.commonLib.write_log("parse category list url is [%s],top_bar is [%s],actualCnt is [%s] " % (list_url,top_bar,actualCnt))

            assert actualCnt >= expectCnt and expectCnt>0, "parse_category_list ActualCnt [%s] is [small] than expectCnt [%s]" % (actualCnt,expectCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_FATAL,response.url,self.name)
        finally:
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_CATEGORY1,-1,-1,urlStatus)

    def parse_product_list(self, response):
        try:        
            product_info = response.meta['product_info']
            ## 有302跳转
            self.commonLib.write_log("parse_product_list url is [%s]" % (response.url))
            
            expectCnt = 1
            actualCnt = 0 

            urlStatus = common.STATUS_DONE

            product_list = response.xpath("//section[@id='products']/ul/li/a")
            expectCnt = len(product_list)
            for option in product_list:
                product_url = option.xpath("@href")[0].extract().strip()
                #product_url = "http://www.zara.cn/cn/zh/%E6%89%93%E6%8A%98/%E5%84%BF%E7%AB%A5/%E5%A5%B3%E5%A9%B4-%7C-3-%E4%B8%AA%E6%9C%88---3-%E5%B2%81/%E9%85%8D%E9%A5%B0/%E8%A2%9C%E5%AD%90%E5%92%8C%E8%BF%9E%E8%A3%A4%E8%A2%9C/%E7%BD%97%E7%BA%B9%E8%A3%A4%E8%A2%9C-c698700p2945533.html"
                actualCnt = actualCnt + 1
                self.commonLib.write_log("get product url is [%s],actualCnt is [%s]" % (product_url,actualCnt))

                if "http" not in product_url:
                    product_url = "http:" + product_url

                request = scrapy.Request(product_url, callback=self.parse_product_detail)
                request.meta['product_info'] = copy.deepcopy(product_info)
                yield request

                # product_url = "http://www.zara.cn/cn/zh/2016-%E6%98%A5%E5%A4%8F%E6%96%B0%E5%93%81/%E5%A5%B3%E5%A3%AB/%E5%A4%A7%E8%A1%A3/%E6%9F%A5%E7%9C%8B%E5%85%A8%E9%83%A8/%E7%BF%BB%E9%A2%86%E7%BE%8A%E6%AF%9B%E5%A4%A7%E8%A1%A3-c719012p3186217.html"
                # actualCnt = actualCnt + 1
                # self.commonLib.write_log("get product url is [%s],actualCnt is [%s]" % (product_url,actualCnt))

                # yield common.addUrl(product_url,self.taskId,list_url,common.LEVEL_PRODUCT_DETAIL,-1,-1,common.STATUS_NEW)

                # product_info = {}
                # product_info['url'] = product_url
                # request = scrapy.Request(product_url, callback=self.parse_product_detail)
                # request.meta['product_info'] = copy.deepcopy(product_info)
                # yield request

                if self.debug:
                    self.commonLib.write_log("in debug modal")
                    expectCnt = 1
                    break

            assert actualCnt >= expectCnt and expectCnt>0, "parse_product_list ActualCnt [%s] is [small] than expectCnt [%s]" % (actualCnt,expectCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_FATAL,response.url,self.name)
        finally:
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_PRODUCT_LIST,-1,-1,urlStatus)

    def parse_product_detail_new(self, response):

        try:         

            self.commonLib.write_log("parse_product_detail url is [%s]" % (response.url))
            product_info = response.meta['product_info']
            product_url = response.url

            expectItemCnt = 1
            expectSkuCnt = 1

            actualItemCnt = 0
            actualSkuCnt = 0

            urlStatus = common.STATUS_DONE

            productDataStr = response.xpath('//script').re("window.zara.dataLayer = (.*);")[0].strip()

            #print "productDataStr is ",productDataStr
            
            productData = json.loads(productDataStr)

            product_id = productData['product']['id']

            self.commonLib.write_log("parse_product_detail product_url is [%s],product_id is [%s] " % (product_url,product_id))

            brand = "zara"
            name = productData['product']['name']
            #product_detail = productData['product']['description']
            product_detail = ""

            #time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())

            product =  ProductInfo()
            product['itemType'] = common.TYPE_ITEM
            product['sourceItemId'] = product_id
            product['sourceItemVersion'] = self.taskId
            product['sourceUrl'] = product_url
            product['sourceWebsite'] = self.name
            product['brandName'] = brand
            product['itemName'] = name
            product['categoryLevel1'] = product_info['top_bar']
            product['categoryLevel2'] = product_info['category_name']
            product['sourceCurrency'] = self.source_currency
            product['itemDetail'] = product_detail

            yield product

            actualItemCnt = actualItemCnt + 1

            sourceOriginalPrice = productData['product']['price']
            sourceOriginalPrice = int(sourceOriginalPrice)/100

            for colorOption in productData['product']['detail']['colors']:
                color = colorOption['name']
                path = colorOption['image']['path']
                colorImageUrl = colorOption['colorImageUrl']

                colorPicList = []
                for picOption in colorOption['xmedia']:
                    picUrl = "http://static.zara-static.cn/photos//%s/w/560/%s.jpg" % (picOption['path'],picOption['name'])
                    colorPicList.append(picUrl)

                for sizeOption in colorOption['sizes']:
                    sku_product_id = sizeOption['sku']
                    size = sizeOption['name']

                    stock = 0
                    if sizeOption['availability'] == "in_stock":
                        stock = -1

                    sourceSellingPrice = sizeOption['price']
                    sourceSellingPrice = int(sourceSellingPrice)/100


                    sku = SkuInfo()
                    sku['itemType'] = common.TYPE_SKU
                    sku["sourceSkuId"] = sku_product_id
                    sku["sourceItemId"] = product['sourceItemId']
                    sku["sourceWebsite"] = self.name
                    sku["sourceUrl"] = product['sourceUrl']
                    sku["sourceItemVersion"] = product['sourceItemVersion']
                    sku["brandName"] = product['brandName']
                    sku['sourceOriginalPrice'] = sourceOriginalPrice
                    sku["sourceSellingPrice"] = sourceSellingPrice
                    sku["sourceCurrency"] = self.source_currency
                    sku["sourceStock"] = stock
                    sku["size"] = size
                    sku['color'] = color
                    sku['colorPic'] = colorPicList[0]
                    sku['picList'] = json.dumps(colorPicList);
                    yield sku

                    actualSkuCnt = actualSkuCnt + 1

            assert actualItemCnt >= expectItemCnt, "item ActualCnt [%s] is [small] than expectCnt [%s]" % (actualItemCnt,expectItemCnt)
            assert actualSkuCnt >= expectSkuCnt, "sku ActualCnt [%s] is [small] than expectCnt [%s]" % (actualSkuCnt,expectSkuCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_WARNING,response.url,self.name)
        finally:
            self.commonLib.write_log("done")
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_PRODUCT_DETAIL,expectItemCnt,actualItemCnt,urlStatus)

    def parse_product_detail(self, response):

        try:         

            self.commonLib.write_log("parse_product_detail url is [%s]" % (response.url))
            product_info = response.meta['product_info']
            product_url = response.url

            expectItemCnt = 1
            expectSkuCnt = 1

            actualItemCnt = 0
            actualSkuCnt = 0

            urlStatus = common.STATUS_DONE

            #如果一个页面里面有多个item，进入这个分支模块
            if not response.xpath('//script').re("productData: (.*),"):
                #从productsData里面提取productId列表
                productsssDataStr=response.xpath('//script').re("productsData: (.*),")[0].strip()
                productsssData=json.loads(productsssDataStr)
                #分别别提取页面里面的catalogId，categoryId，langId，storeId
                storeId=response.xpath('//script').re("storeId: '(.*)',")[0].strip()
                langId=response.xpath('//script').re("langId: '(.*)',")[0].strip()
                catalogId=response.xpath('//script').re("catalogId: '(.*)',")[0].strip()
                categoryId=response.xpath('//script').re("currentCategoryId: '(.*)',")[0].strip()
                #构造ajax请求 http://www.zara.cn/webapp/wcs/stores/servlet/CatentryPopUpView?catalogId=25052&categoryId=805005&langId=-7&storeId=11716&productId=3270544&ajaxCall=true
                for p in productsssData['products']:
                    productsssId=p['productId']
                    psssurl='http://www.zara.cn/webapp/wcs/stores/servlet/CatentryPopUpView?catalogId=%s&categoryId=%s&langId=%s&storeId=%s&productId=%s&ajaxCall=true'%(catalogId,categoryId,langId,storeId,productsssId)
                    
                    actualItemCnt+=1
                    actualSkuCnt+=1
                    self.commonLib.write_log('get more product url [%s]'%psssurl)
                    common.addUrl(psssurl,self.taskId,response.url,common.LEVEL_PRODUCT_DETAIL,-1,-1,common.STATUS_NEW)
                    
                    request=scrapy.Request(psssurl, callback=self.parse_item_detail)
                    request.meta['product_info']=copy.deepcopy(product_info)
                    request.meta['product_url']=response.url
                    yield request
                return


            productDataStr = response.xpath('//script').re("productData: (.*),")[0].strip()
            mediaDataStr = response.xpath('//script').re("xmedias: (.*)}}")[0].strip() + "}}"

            productData = json.loads(productDataStr)
            mediaData = json.loads(mediaDataStr)

            product_id = productData['productId']

            self.commonLib.write_log("parse_product_detail product_url is [%s],product_id is [%s] " % (product_url,product_id))

            brand = "zara"
            name = response.xpath("//section[@id='product']/div/div/header/h1/text()")[0].extract().strip()
            product_detail = response.xpath("//div[@id='description']/p[@class='description']/span/text()")[0].extract().strip()

            #time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())

            product =  ProductInfo()
            product['itemType'] = common.TYPE_ITEM
            product['sourceItemId'] = product_id
            product['sourceItemVersion'] = self.taskId
            product['sourceUrl'] = product_url
            product['sourceWebsite'] = self.name
            product['brandName'] = brand
            product['itemName'] = name
            product['categoryLevel1'] = product_info['top_bar']
            product['categoryLevel2'] = product_info['category_name']
            product['sourceCurrency'] = self.source_currency
            product['itemDetail'] = product_detail

            yield product

            actualItemCnt = actualItemCnt + 1

            #yield product
            ## 获取颜色对应关系
            color_map = {}
            for color in response.xpath("//div[@class='colors']/label"):
                color_code = color.xpath("@data-colorcode")[0].extract().strip()
                color_name = color.xpath("div/@title")[0].extract().strip()
                color_map[color_code] = color_name

            ## 分析sku列表
            picList = []
            for sku_color in productData['colors']:
                pColorImgBaseUrl = sku_color['pColorImgBaseUrl']
                colorImgUrl = sku_color['colorImgUrl']
                color_code = sku_color['code']
                color = color_map[color_code]
                colorPicList = []
                for color_img_option in mediaData[color_code]["xmedias"]:
                    pic_url = 'http:'+color_img_option['url']
                    colorPicList.append(pic_url)
                    picList.append(pic_url)

                for sku_size in sku_color['sizes']:
                    sku_product_id = sku_size["catentryId"]
                    origin_price = float(sku_size["oldPrice"])
                    sell_price = float(sku_size["currentPrice"])
                    size = sku_size["description"]

                    self.commonLib.write_log("parse sku  is [%s] [%s]" % (sku_product_id,size))

                    ## 价格为空
                    assert sku_product_id, "sku_product_id [%s] can not be null" % (sku_product_id)
                    assert sell_price>1, "sell_price [%s] is error" % (sell_price)

                    if origin_price<1:
                        origin_price = sell_price

                    stock = 0
                    availability = sku_size["availability"]
                    #availability = "aaa"
                    if availability == "InStock":
                        stock = -1
                    elif availability in ["OutOfStock","BackSoon","ComingSoon"]:
                        stock = 0
                    else:
                        raise ValueError("availability[%s] is unknow type" %(availability))

                    sku = SkuInfo()
                    sku['itemType'] = common.TYPE_SKU
                    sku["sourceSkuId"] = sku_product_id
                    sku["sourceItemId"] = product['sourceItemId']
                    sku["sourceWebsite"] = self.name
                    sku["sourceUrl"] = product['sourceUrl']
                    sku["sourceItemVersion"] = product['sourceItemVersion']
                    sku["brandName"] = product['brandName']
                    sku['sourceOriginalPrice'] = origin_price
                    sku["sourceSellingPrice"] = sell_price
                    sku["sourceCurrency"] = self.source_currency
                    sku["sourceStock"] = stock
                    sku["size"] = size
                    sku['color'] = color
                    sku['colorPic'] = colorPicList[0]
                    sku['picList'] = json.dumps(colorPicList);
                    yield sku

                    actualSkuCnt = actualSkuCnt + 1

            assert actualItemCnt >= expectItemCnt, "item ActualCnt [%s] is [small] than expectCnt [%s]" % (actualItemCnt,expectItemCnt)
            assert actualSkuCnt >= expectSkuCnt, "sku ActualCnt [%s] is [small] than expectCnt [%s]" % (actualSkuCnt,expectSkuCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_WARNING,response.url,self.name)
        finally:
            self.commonLib.write_log("done")
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_PRODUCT_DETAIL,expectItemCnt,actualItemCnt,urlStatus)


    def parse_item_detail(self, response):
        try:         
            self.commonLib.write_log("parse_item_detail url is [%s]" % (response.url))
            product_info = response.meta['product_info']
            product_url = response.meta['product_url']
            
            expectItemCnt = 1
            expectSkuCnt = 1

            actualItemCnt = 0
            actualSkuCnt = 0

            urlStatus = common.STATUS_DONE

            productDataStr = response.xpath('//script').re("productData: (.*),")[0].strip()
            mediaDataStr = response.xpath('//script').re("xmedias: (.*)}}")[0].strip() + "}}"

            productData = json.loads(productDataStr)
            mediaData = json.loads(mediaDataStr)

            product_id = productData['productId']

            self.commonLib.write_log("parse_item_detail product_url is [%s],product_id is [%s] " % (product_url,product_id))

            brand = "zara"
            name = response.xpath('//script').re('productName: "(.*)",')[0].strip()
            #如果名字为空，品牌+分类
            if not name:
                name=brand+' '+product_info['category_name']

            product_detail = ''
            #time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())

            product =  ProductInfo()
            product['itemType'] = common.TYPE_ITEM
            product['sourceItemId'] = product_id
            product['sourceItemVersion'] = self.taskId
            product['sourceUrl'] = product_url
            product['sourceWebsite'] = self.name
            product['brandName'] = brand
            product['itemName'] = name
            product['categoryLevel1'] = product_info['top_bar']
            product['categoryLevel2'] = product_info['category_name']
            product['sourceCurrency'] = self.source_currency
            product['itemDetail'] = product_detail

            yield product
            actualItemCnt = actualItemCnt + 1

            ## 获取颜色对应关系
            color_map = {}
            for color in response.xpath("//div[@class='colors']/label"):
                color_code = color.xpath("@data-colorcode")[0].extract().strip()
                color_name = color.xpath("div/@title")[0].extract().strip()
                color_map[color_code] = color_name

            ## 分析sku列表
            picList = []
            for sku_color in productData['colors']:
                #pColorImgBaseUrl = sku_color['pColorImgBaseUrl']
                #colorImgUrl = sku_color['colorImgUrl']
                color_code = sku_color['code']
                color = color_map[color_code]
                colorPicList = []
                for color_img_option in mediaData[color_code]["xmedias"]:
                    pic_url = 'http:'+color_img_option['url']
                    colorPicList.append(pic_url)
                    #picList.append(pic_url)

                for sku_size in sku_color['sizes']:
                    sku_product_id = sku_size["catentryId"]
                    origin_price = float(sku_size["oldPrice"])
                    sell_price = float(sku_size["currentPrice"])
                    size = sku_size["description"]

                    self.commonLib.write_log("parse sku  is [%s] [%s]" % (sku_product_id,size))

                    ## 价格为空
                    assert sku_product_id, "sku_product_id [%s] can not be null" % (sku_product_id)
                    assert sell_price>1, "sell_price [%s] is error" % (sell_price)

                    if origin_price<1:
                        origin_price = sell_price

                    stock = 0
                    availability = sku_size["availability"]
                    #availability = "aaa"
                    if availability == "InStock":
                        stock = -1
                    elif availability in ["OutOfStock","BackSoon","ComingSoon"]:
                        stock = 0
                    else:
                        raise ValueError("availability[%s] is unknow type" %(availability))

                    sku = SkuInfo()
                    sku['itemType'] = common.TYPE_SKU
                    sku["sourceSkuId"] = sku_product_id
                    sku["sourceItemId"] = product['sourceItemId']
                    sku["sourceWebsite"] = self.name
                    sku["sourceUrl"] = product['sourceUrl']
                    sku["sourceItemVersion"] = product['sourceItemVersion']
                    sku["brandName"] = product['brandName']
                    sku['sourceOriginalPrice'] = origin_price
                    sku["sourceSellingPrice"] = sell_price
                    sku["sourceCurrency"] = self.source_currency
                    sku["sourceStock"] = stock
                    sku["size"] = size
                    sku['color'] = color
                    sku['colorPic'] = colorPicList[0]
                    sku['picList'] = json.dumps(colorPicList);
                    yield sku

                    actualSkuCnt = actualSkuCnt + 1

            assert actualItemCnt >= expectItemCnt, "item ActualCnt [%s] is [small] than expectCnt [%s]" % (actualItemCnt,expectItemCnt)
            assert actualSkuCnt >= expectSkuCnt, "sku ActualCnt [%s] is [small] than expectCnt [%s]" % (actualSkuCnt,expectSkuCnt)

        except Exception, e:
            urlStatus = common.STATUS_FAIL
            exc_type, exc_value, exc_traceback = sys.exc_info()
            msgStr = self.commonLib.write_exception(exc_type, exc_value, exc_traceback)
            self.commonLib.write_log(msgStr)
            yield common.addLog(msgStr,self.taskId,common.LOG_WARNING,response.url,self.name)
        finally:
            self.commonLib.write_log("done")
            yield common.addUrl(response.url,self.taskId,'',common.LEVEL_PRODUCT_DETAIL,expectItemCnt,actualItemCnt,urlStatus)



