#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import httplib
import urllib
import json
import time
import commands
import lib.common as common

## 配置了自动更新的网站
websiteList = ["zara","mikihouse"]
common = common.Common()
dirPath = os.path.dirname(os.path.abspath(__file__))
common.write_log("dirPath is [%s]" % (dirPath))
boundaryId = 0

while True:
    try:
        logFile = "log/spider.log." + time.strftime('%Y%m%d%H') 
        url = '/api/task/getTaskListByStatus'
        # post_data = {}
        # post_data['taskStatus'] = 'new'
        # post_data['taskType'] = 'spider'
        # post_data['num'] = 1
        post_data = {
            'taskStatus' : 'new',
            'taskType' : 'spider',
            'num' : 1,
            'boundaryId' : boundaryId,
        }
        ret = common.http_post(url,post_data)
        retData = json.loads(ret)

        if retData['errno'] != 0:
            raise ValueError("getTaskListByStatus failed and ret is [%s]" % (ret))

    #    if True:
        if len(retData['data']['list']) > 0:
            taskInfo = retData['data']['list'][0]
            # cmdStatus = 0

            # ## UPDATE `spider_task` SET `taskStatus` = 'new' WHERE `spider_task`.`taskId` = 7;
            # taskInfo = {}
            # taskInfo['taskId'] = 7
            # taskInfo['taskName'] = "zara"
            taskId = taskInfo['taskId']
            taskName = taskInfo['taskName']
            boundaryId = taskId
            common.set_header("taskInfo",taskInfo)
            ## 将任务置为running状态

            url = '/api/task/runTask'
            post_data = {}
            post_data['taskId'] = taskId
            retStr = common.http_post(url,post_data)
            runTaskRet = json.loads(retStr)
            if runTaskRet['errno'] != 0:
                raise ValueError("runTask [%s][%s] failed and ret is [%s]" % (taskId,taskName,retStr))

            ## 执行抓取任务
            #cmd = "cd %s && scrapy crawl %s -a taskId=%s >> %s" % (dirPath,taskName,taskId,logFile)
            cmd = "cd %s && scrapy crawl %s -a taskId=%s" % (dirPath,taskName,taskId)
            common.write_log("start to scrapy task [%s],cmd is [%s]"%(taskName,cmd))
            (cmdStatus, output) = commands.getstatusoutput(cmd)
            #cmdStatus = os.system(cmd)

            common.write_log("run cmd is [%s] and cmdStatus is [%s]" % (cmd,cmdStatus))
            ## 更新任务状态
            if cmdStatus == 0:
                taskStatus = "done"
            else:
                taskStatus = "fail"

            post_data = {
                'taskId' : taskId,
                'taskStatus' : taskStatus,
            }
            ## 更新任务结果
            url = '/api/spider/updateTaskResultByTaskId'
            updateTaskStr = common.http_post(url,post_data)
            updateTaskRet = json.loads(updateTaskStr)
            common.write_log("updateTask url is [%s][%s] and ret is [%s]" % (url,taskId,updateTaskStr))
            if updateTaskRet['errno'] != 0:
                raise ValueError("updateTask [%s][%s] failed and ret is [%s]" % (taskId,taskName,updateTaskStr))
        else:
            boundaryId = 0
            common.write_log("getTaskListByStatus list is null")

    except Exception, e:
        msgStr = "[Fatal] Exception is [%s] " % (e)
        common.write_log(msgStr)
        print msgStr
    finally:
    	common.write_log("spider task")
        time.sleep(10)



