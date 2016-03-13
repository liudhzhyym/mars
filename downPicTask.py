#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import httplib
import urllib
import json
import time
import commands
import random
import traceback
import sys
import lib.common as common
import conf.spider as spider

common = common.Common()
dirPath = os.path.dirname(os.path.abspath(__file__))
common.write_log("dirPath is [%s]" % (dirPath))


threadNum = spider.threadNum
if not threadNum:
    threadNum = 1

common.write_log("threadNum [%s]" % (threadNum))

spiderPicId = 0
num = 16
url = '/api/spider/getPicList'
type = "download"
while True:
    try:

        common.write_log("spiderPicId is [%s]" % (spiderPicId))
        post_data = {}
        post_data['type'] = type
        post_data['boundaryId'] = spiderPicId
        post_data['num'] = num
        ret = common.http_post(url,post_data)
        retData = json.loads(ret)

        if retData['errno'] != 0:
            raise ValueError("getPicList failed and ret is [%s]" % (ret))

        if len(retData['data']['list']) > 0:
            picInfoList = retData['data']['list']
            total = retData['data']['total']
            # cmdStatus = 0
            urlList = []
            for picInfo in picInfoList:
                urlList.append(picInfo['picUrl'])
                spiderPicId = picInfo['spiderPicId']

            maxGroup = threadNum
            totalGroup = int(total/num)
            if totalGroup<maxGroup:
                maxGroup = totalGroup
            randInt = random.randint(0, maxGroup)
            spiderPicId = int(spiderPicId) + randInt*num
            common.write_log("randInt is [%s],spiderPicId is [%s]" % (randInt,spiderPicId))

            if urlList:
                ## 下载图片
                urlListStr = json.dumps(urlList)
                ## 执行抓取任务
                common.write_log("start to scrapy taskName")

                cmd = "cd %s && scrapy crawl pic -a picList='%s'" % (dirPath,urlListStr)
                (cmdStatus, output) = commands.getstatusoutput(cmd)
                #cmdStatus = os.system(cmd)

                common.write_log("run cmd is [%s] and cmdStatus is [%s]" % (cmd,cmdStatus))
                if cmdStatus != 0:
                    raise ValueError("down load pic failed and ret is [%s]" % (cmdStatus))

        else:
            common.write_log("getTaskListByStatus list is null")
            time.sleep(10)
            spiderPicId = 0

    except Exception, e:
        msgStr = "[Fatal] exception is [%s][%s] " % (e,traceback.format_exc())
        common.write_log(msgStr)
        print msgStr
    finally:
    	common.write_log("download pic task")
        time.sleep(1)



