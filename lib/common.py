#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import os
import httplib
import urllib
import json
import sys
import log
import datetime
import conf.env as env

from scrapy.http import Request, FormRequest

class Common(object):
    def __init__(self):
        self.prefix = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_file = os.path.join(self.prefix, 'log', 'spider.log.%Y%m%d%H')
        self.log = log.Log(self.log_file)
        #print "init"

    def set_header(self,key,value):
        self.log.set_once(key, value)
        #print "set_header"

    def write_log(self,logMsg):
        self.log.write_log(log.Log.INFO, logMsg)
        self.log.renew()
        #print "write_log"
    
    def write_file(self,name,content):
        #self.prefix = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_file = os.path.join(self.prefix, 'log', name)
        html_dir = os.path.dirname(html_file)
        if not os.path.isdir(html_dir):
            os.makedirs(html_dir)
        file_object = open(html_file, 'w')
        file_object.write(content)
        file_object.close()

    def write_exception(self,exc_type,exc_value,exc_traceback):
        #print "--------exc_value",dir(exc_value)
        traceback_details = {
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'lineno' : exc_traceback.tb_lineno,
            'name'  : exc_traceback.tb_frame.f_code.co_name,
            'type'  : exc_type.__name__,
            'message' : exc_value.message,
        }
        self.set_header("traceback_details",traceback_details)
        return json.dumps(traceback_details)

    # def main(self):
    #     self.test_write_log()
    #     self.test_notice()
    #     self.test_std()
    #     self.test_header()
    #     self.test_notice_header()
    def http_post(self,url,data):
        try:
            hostName = "172.31.27.151"
            env_type = self.get_env()
            if env_type == "online":
               #hostName = "172.31.9.126"
               hostName = "172.31.9.162"

            self.set_header('env_type', env_type)
            self.set_header('hostName', hostName)
            self.set_header('data', data)

            httpClient = None
            ret = ''
            urlInfo = hostName + url

            params = json.dumps(data)
            headers = {"Content-type": "application/json"}
         
            httpClient = httplib.HTTPConnection(hostName, 8081, timeout=30)
            
            
            httpClient.request("POST", url, params, headers)
            response = httpClient.getresponse()
            ret = response.read()
            status = response.status
            reason = response.reason
            headers = response.getheaders() #获取头信息     

            self.set_header('ret', ret)
            self.set_header('status', status)
            self.set_header('reason', reason)
            #self.set_header('headers', headers)
                 

        except Exception, e:
            self.set_header('Exception', e)
        finally:
            if httpClient:
                httpClient.close()
            self.write_log(urlInfo)  
        return ret  

    ## 获取当前环境类型，默认是offline
    def get_env(self):
        env_type = "offline"
        if env.env_type == "online":
            env_type = "online"
        return env_type

    def finish_task(self, taskId, taskStatus,taskRet):
        url = '/api/task/finishCeleryTask'
        postData = {
            'taskId' : taskId,
            'taskStatus' : taskStatus,
            'taskRet' : taskRet,
        }
        ret = self.http_post(url,postData)
        self.write_log("finish_task of [%s][%s] and ret is[%s]" % (taskId,taskStatus,ret)) 
        retData = json.loads(ret)
        return retData

    def run_task(self, taskId):
        url = '/api/task/runCeleryTask'
        postData = {
            'taskId' : taskId,
        }
        ret = self.http_post(url,postData)
        self.write_log("runTask of [%s] and ret is[%s]" % (taskId,ret)) 
        retData = json.loads(ret)
        return retData

    def create_form_data(self,url,formdata,method,formxpath=None,response=None,meta=None,callback=None):
        if meta is None:
            meta = {}
        meta['method'] = method

        if formxpath is not None:
            if not url:
                url = None
            req = [scrapy.FormRequest.from_response(
                response,
                formdata = formdata,
                formxpath = formxpath,
                dont_click = False,
                meta = meta,
                url = url,
                callback=callback,
            )]
        else:
            req = FormRequest(
                url=url,
                formdata = formdata,
                meta = meta,
                callback=callback,
            )
        return req


