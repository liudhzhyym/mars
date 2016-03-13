#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import httplib
import urllib
import json
import time
import commands
import lib.common as common

common = common.Common()
dirPath = os.path.dirname(os.path.abspath(__file__))
common.write_log("dirPath is [%s]" % (dirPath))
boundaryId = 0

while True:
    try:
        logFile = "log/spider.log." + time.strftime('%Y%m%d%H') 
        url = '/api/task/getCeleryTaskListByStatus'

        post_data = {
            'taskStatus' : 'new',
            'taskType' : 'shopping',
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

            taskId = taskInfo['taskId']
            taskName = taskInfo['taskName']
            boundaryId = taskId
            common.set_header("taskInfo",taskInfo)
            
            sourceWebsite = taskName.split("#")[0]

            spiderName = sourceWebsite + "_buy"
            ## 执行抓取任务
            #cmd = "cd %s && scrapy crawl %s -a taskId=%s >> %s" % (dirPath,taskName,taskId,logFile)
            cmd = "cd %s && scrapy crawl %s -a taskId=%s" % (dirPath,spiderName,taskId)
            common.write_log("start to scrapy task [%s],cmd is [%s]"%(spiderName,cmd))
            (cmdStatus, output) = commands.getstatusoutput(cmd)
            #cmdStatus = os.system(cmd)
            
            if cmdStatus!=0:
                url = '/api/task/runCeleryTask'
                post_data = {}
                post_data['taskId'] = taskId
                retStr = common.http_post(url,post_data)
                runTaskRet = json.loads(retStr)
                if runTaskRet['errno'] != 0:
                    common.write_log("runTask [%s][%s] failed and ret is [%s]" % (taskId,taskName,retStr))

                taskStatus = "fail"

                post_data = {
                    'taskId' : taskId,
                    'taskStatus' : taskStatus,
                }
                ## 更新任务结果
                url = '/api/task/finishCeleryTask'
                updateTaskStr = common.http_post(url,post_data)
                updateTaskRet = json.loads(updateTaskStr)
                common.write_log("updateTask url is [%s][%s] and ret is [%s]" % (url,taskId,updateTaskStr))
                if updateTaskRet['errno'] != 0:
                    raise ValueError("updateTask [%s][%s] failed and ret is [%s]" % (taskId,taskName,updateTaskStr))

            common.write_log("run cmd is [%s] and cmdStatus is [%s]" % (cmd,cmdStatus))
        else:
            boundaryId = 0
            common.write_log("getTaskListByStatus list is null")

    except Exception, e:
        msgStr = "[Fatal] Exception is [%s] " % (e)
        common.write_log(msgStr)
        print msgStr
    finally:
    	common.write_log("shopping spider task")
        time.sleep(10)



