#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib
import urllib
import json

def http_post(url,data):
    httpClient = None
    ret = ''
    try:
        params = json.dumps(data)
        headers = {"Content-type": "application/json"}
     
        httpClient = httplib.HTTPConnection("apidev.bonbon.club", 80, timeout=30)
        print "url is ",url
        httpClient.request("POST", url, params, headers)
        response = httpClient.getresponse()
        ret = response.read()
        print response.status
        print response.reason
        print ret
        print response.getheaders()

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    return ret  
            
