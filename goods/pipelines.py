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
IMAGES_STORE = settings.get("IMAGES_STORE")
#UPLOAD_IMAGE = "true"
UPLOAD_IMAGE = "true"

class GoodsPipeline(ImagesPipeline):

    # #pipeline默认调用
    # def process_item(self, item, spider):
    #     query = self.dbpool.runInteraction(self._conditional_insert, item)
    #     return item

    # #将每行写入数据库中
    # def _conditional_insert(self, tx, item):
    #     if item.get('title'):
    #         for i in range(len(item['title'])):
    #             tx.execute('insert into book values (%s, %s)', (item['title'][i], item['link'][i]))

    def get_media_requests(self, item, info):
        if UPLOAD_IMAGE != "true":
            return
        if not item.get('image_urls'):
            return
        for image_url in item['image_urls']:
            try:
                yield scrapy.Request(image_url)
            except Exception, e:
                print e
            

    # def process_item(self, item, spider):
    #     print "process_item "
    #     item_data = {}
    #     trip_arr = ["itemName","itemDetail","size","categoryLevel1","categoryLevel2"]
    #     for key,value in item.items():
    #         if key=="size":
    #             #value = value.replace("-","--").replace("½",".5")
    #             value = value.replace("½",".5")
    #         if key in trip_arr:
    #             value = value.replace("®"," ").replace("™"," ").replace("½",".5")
    #         item_data[key] = value
    #     # if item_data.get('sourceSkuId'):
    #     #     ## sku信息
    #     #     url = '/api/spider/addSku'
    #     #     post_data = {}
    #     #     post_data['sku'] = item_data
    #     #     self.http_post(url,post_data)
    #     #     print "this is a sku"
    #     # elif item_data.get('image_urls'):
    #     #     return item
    #     # elif item_data.get('sourceItemId'):
    #     #     url = '/api/spider/addItem'
    #     #     post_data = {}
    #     #     post_data['item'] = item_data
    #     #     self.http_post(url,post_data)
    #     #     print "this is a item"
    #     commonLib = Common()
    #     itemType = item_data.pop("itemType")

    #     if itemType == spiders.common.TYPE_URL:
    #         url = '/api/spider/addUrl'
    #         commonLib.http_post(url,item_data)
    #         print "this is a url"
    #     elif itemType == spiders.common.TYPE_LOG:
    #         url = '/api/spider/addLog'
    #         post_data = {}
    #         post_data['log'] = item_data
    #         commonLib.http_post(url,post_data)
    #         print "this is a log"
    #     elif itemType == spiders.common.TYPE_ITEM:
    #         url = '/api/spider/addItem'
    #         post_data = {}
    #         post_data['item'] = item_data
    #         commonLib.http_post(url,post_data)
    #         print "this is a item"

    #     elif itemType == spiders.common.TYPE_SKU:
    #         url = '/api/spider/addSku'
    #         post_data = {}
    #         post_data['sku'] = item_data
    #         commonLib.http_post(url,post_data)
    #         print "this is a sku"

    #     # elif 'image_url' in item:
    #     #     images = []
    #     #     dir_path = '%s/%s' % ('/home/work/opbin/2015111615liu', spider.name)

    #     #     if not os.path.exists(dir_path):
    #     #         os.makedirs(dir_path)
    #     #     for image_url in item['image_url']:
    #     #         us = image_url.split('/')[3:]
    #     #         image_file_name = '_'.join(us)
    #     #         file_path = '%s/%s' % (dir_path, image_file_name)
    #     #         print "file_path = ",file_path
    #     #         images.append(file_path)
    #     #         if os.path.exists(file_path):
    #     #             continue
    #     #         with open(file_path, 'wb') as handle:
    #     #             response = requests.get(image_url, stream=True)
    #     #             for block in response.iter_content(1024):
    #     #                 if not block:
    #     #                     break

    #     #                 handle.write(block)
        
    #     return item

    def item_completed(self, results, item, info):
        item_data = {}
        trip_arr = ["itemName","itemDetail","size","categoryLevel1","categoryLevel2"]
        for key,value in item.items():
            if key=="size":
                #value = value.replace("-","--").replace("½",".5")
                value = value.replace("½",".5")
            if key in trip_arr:
                value = value.replace("®"," ").replace("™"," ").replace("½",".5")
            item_data[key] = value
        commonLib = Common()
        itemType = item_data.pop("itemType")

        if itemType == spiders.common.TYPE_URL:
            url = '/api/spider/addUrl'
            commonLib.http_post(url,item_data)
            print "this is a url"
        elif itemType == spiders.common.TYPE_LOG:
            url = '/api/spider/addLog'
            post_data = {}
            post_data['log'] = item_data
            commonLib.http_post(url,post_data)
            print "this is a log"
        elif itemType == spiders.common.TYPE_ITEM:
            url = '/api/spider/addItem'
            post_data = {}
            post_data['item'] = item_data
            commonLib.http_post(url,post_data)
            print "this is a item"

        elif itemType == spiders.common.TYPE_SKU:
            url = '/api/spider/addSku'
            post_data = {}
            post_data['sku'] = item_data
            commonLib.http_post(url,post_data)
            print "this is a sku"
        elif itemType == spiders.common.TYPE_PIC:
            url = '/api/spider/uploadPic'
            image_urls = item['image_urls']
            #print "this is a pic ",item,results

            for ok, x in results:
                if ok:
                    picUrl = x['url']
                    picUrl = unquote(picUrl)
                    if picUrl in image_urls:
                        image_urls.remove(picUrl)
                    picPath = IMAGES_STORE + x['path']

                    commonLib.write_log("download pic path is [%s], url [%s] " % (picPath,picUrl))
                    post_data = {
                        'picUrl':picUrl,
                        'picPath':picPath,
                    }
                    commonLib.http_post(url,post_data)
            if image_urls:
                for picUrl in image_urls:
                    commonLib.write_log("download pic url [%s] failed " % (picUrl))
                    post_data = {
                        'picUrl':picUrl,
                        'picPath':spiders.common.STATUS_FAIL,
                    }
                    commonLib.http_post(url,post_data)
        return item

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if UPLOAD_IMAGE != "true":
            return
        if not item.get('image_urls'):
            return
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        picList = []

        url = "/api/spider/uploadPic"
        # for ok, x in results:
        #     picUrl = x['url']
        #     path = IMAGES_STORE + x['path']
        #     picType = path.split(".")[-1]

        #     m1 = md5.new()   
        #     m1.update(picUrl)   
        #     picUrlMd5 = m1.hexdigest()
        #     newPicName = picUrlMd5 + "." + picType
        #     newPicPath = "/home/work/image/%s" % (newPicName)
        #     log.msg("download pic path is [%s] picName is [%s], url [%s] " % (path,newPicName,picUrl))

        #     shutil.copyfile(path,newPicPath) 

        #     try:
        #         post_data = {}
        #         post_data['picUrl'] = picUrl
        #         post_data['imgBase64'] = newPicName
                
        #         self.http_post(url,post_data)

        #     except Exception, e:
        #         print e

        # for pic in image_paths:
        #     picList.append(IMAGES_STORE + pic)

        # if UPLOAD_IMAGE != "true":
        #     return item
        # if picList:
        #     url = '/api/spider/updateItemBySourceItemId'
        #     # updateData = {}
        #     # updateData['picList'] = json.dumps(picList)
            
        #     # for pic in picList:
        #     #     fp=open(pic,'rb')
        #     #     imgBase64=base64.b64encode(fp.read())

        #     #     post_data = {}
        #     #     post_data['picUrl'] = picUrl
        #     #     post_data['imgBase64'] = imgBase64        

        #     # post_data = {}
        #     # post_data['sourceItemId'] = item['sourceItemId']
        #     # post_data['sourceWebsite'] = item['sourceWebsite']
        #     # post_data['item'] = updateData
        #     # self.http_post(url,post_data)
        # print "item_completed item is ",IMAGES_STORE,picList,results
        return item


    def http_post(self, url,data):
        httpClient = None
        try:
            params = json.dumps(data)
            headers = {"Content-type": "application/json"}
            #print "========== ",params
         
            httpClient = httplib.HTTPConnection("apidev.bonbon.club", 80, timeout=30)
            httpClient.request("POST", url, params, headers)
            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
            print response.getheaders() #获取头信息            

        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
        return response.status  
