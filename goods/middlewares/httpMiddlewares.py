#!/usr/bin/env python
#-*-coding:utf-8 -*-
import random
import requests
from requests.exceptions import *
import json
import copy
import urllib
import time
from lxml import etree
import threading
import gevent
from gevent.threadpool import ThreadPool
from gevent.coros import BoundedSemaphore
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Start your middleware class
class ProxyMiddleware(object):

    def __init__(self):
        self.jp_ip_list = [
            "106.186.25.85:8081",
            "54.238.246.207:3128",
            "52.68.207.5:3128",
        ]
        self.us_ip_list = [
            "107.151.152.218:80",
            "107.151.152.210:80",
            #"107.151.142.125:80",
            #"107.151.142.115:80",
            #"158.69.237.1:3128",
            "52.34.207.158:8080",
            "198.2.202.41:80",
            "45.32.253.190:3128",
        ]
        self.uk_ip_list = [
            "46.101.36.74:3128",
            "185.43.211.243:3128",
            "82.68.75.140:8080",
            "107.151.142.115:80",
        ]
        self.fr_ip_list = [
            "62.23.15.92:3128",
            "51.254.103.206:3128",
            "46.218.85.101:3129",
            "37.187.60.61:80",
            "188.165.154.254:3128",
            "149.202.49.42:80",
            "51.254.36.222:3128",
            "149.202.249.227:3128",
            "51.254.39.174:3128",
            "94.23.196.148:3128",
        ]

        self.firstCrawl = 1
        self.imageCrawl = 0
        self.proxy_japan = "http://www.haodailiip.com/guoji/JP/1"
        self.proxy_us = "http://www.haodailiip.com/guoji/US/1"
        self.proxy_uk = "http://www.haodailiip.com/guoji/GB/1"
        self.proxy_fr = "http://www.haodailiip.com/guoji/FR/1"
        self.using_proxy_ip = []

        self.test_urls = {
                'japan' : 'http://akachan.omni7.jp/detail/295035600',
                'us' : 'http://www.okaidi.fr/',
                'uk' : 'http://www.bonpoint.com/fr/',
        }
        self.use_proxy_list = [
                "img.muji.net",
                "akachan.omni7.jp",
                "amazonaws.com",
                "www.adidas.com",
                "okaidi.fr",
                "rockyourbaby.com",
                "bonpoint.com",
                "united-arrows.co.jp",
                "caramel-shop.co.uk",
        ]
        self.pic_spider_list = [
                "pic",
                "picTest",
                "omni7",
        ]
        self.mutex = threading.Lock()

    def do_check(self, url):
        for option in self.use_proxy_list:
            if option in url:
                return 0
        return 1
    

    def get_proxy_type(self, url):
        if "adidas.com" in url or "amazonaws.com" in url:
            proxy_type = 'US'
        elif "okaidi" in url:
            proxy_type = 'UK'
        elif "rockyourbaby.com" in url or "bonpoint.com" in url or "caramel-shop.co.uk" in url:
            proxy_type = 'UK'
        else:
            proxy_type = 'Japan'

        return proxy_type

    def check_page_parse(self, test_url, response):
        if 'omni7' in test_url:
            if len(response.xpath('//input[@name="item"]/@value')) == 0:
                return 1
        elif 'okaidi' in test_url:
            if len(response.xpath('//nav[@class="header-nav"]/ul/li[@class="li-submenu"]')) == 0:
                return 1
        elif 'bonpoint' in test_url:
            if len(response.xpath('//ul[@id="nav"]/li')) == 0:
                return 1
        else:
            return 1

        return 0

    def test_single_proxy(self, proxy, test_url):
        proxies = {
            'http' : proxy,
        }
        try:
            resp = requests.get(test_url, proxies=proxies, timeout=1)
            response = etree.HTML(resp.content.decode('utf-8'))
            if self.check_page_parse(test_url, response) != 0:
               return 1
        except Exception, e:
            return 1

        if self.mutex.acquire(1):
            self.using_proxy_ip.append(proxy[proxy.find('/') + 2:])
            self.mutex.release()
        return 0

    def run_proxy_parse(self, url, proxy_type):
        try:
            for i in range(3):
                #这里对url进行重新组装
                url = url[0:-1] + str(i+1)
                resp = requests.get(url, timeout=5)
                response = etree.HTML(resp.content.decode('utf-8'))
                #解析代理IP，获取代理ip列表
                proxy_ip_list = []
                for item in response.xpath('//tr[contains(@style,"font-size")]'):
                    ip = item.xpath('./td[1]/text()')[0].strip()
                    port = item.xpath('./td[2]/text()')[0].strip()
                    proto = item.xpath('./td[4]/text()')[0].strip()
                    if proto.lower() == 'https':
                        continue
                    proxy_ip = proto.lower() + '://' + ip + ':' + port
                    if proxy_ip not in proxy_ip_list:
                        proxy_ip_list.append(proxy_ip)

                #对每个IP进行测试，留下可用的代理ip
                pool = ThreadPool(len(proxy_ip_list))
                for pip in proxy_ip_list:
                    pool.spawn(self.test_single_proxy, pip, self.test_urls[proxy_type.lower()])
                pool.join()
            
        except Exception, e:
            pass
        finally:
            return self.using_proxy_ip

    def put_default_to_list(self, proxy_type):
        if proxy_type == 'US':
            self.using_proxy_ip.extend(self.us_ip_list)
        elif proxy_type == 'UK':
            self.using_proxy_ip.extend(self.uk_ip_list)
        elif proxy_type == 'FR':
            self.using_proxy_ip.extend(self.fr_ip_list)
        else:
            self.using_proxy_ip.extend(self.jp_ip_list)

    def get_proxy_ip_list(self, url, spiderName):
        if self.do_check(url) != 0:
            return []

        proxy_type = self.get_proxy_type(url)
        if proxy_type == 'US':
            self.using_proxy_ip = self.run_proxy_parse(self.proxy_us, proxy_type)
        elif proxy_type == 'UK':
            self.using_proxy_ip = self.run_proxy_parse(self.proxy_uk, proxy_type)
        elif proxy_type == 'FR':
            self.using_proxy_ip = self.run_proxy_parse(self.proxy_fr, proxy_type)
        else:
            self.using_proxy_ip = self.run_proxy_parse(self.proxy_japan, proxy_type)

        #print '--' * 100
        #print self.using_proxy_ip
        #print '--' * 100
        #print '@@@-' * 100
        #这里暂时不对z除日本的网站做自动代理
        #if proxy_type == 'UK' or proxy_type == 'US':
        if proxy_type == 'US':
            self.using_proxy_ip = []

        if len(self.using_proxy_ip) < 4:
            self.put_default_to_list(proxy_type)
        
        return self.using_proxy_ip

    # overwrite process request
    def process_request(self, request, spider):
        
        if 'bonbon.club' in request.url:
            self.imageCrawl = 1
        elif self.imageCrawl == 1 and self.do_check(request.url) == 0:
            proxy_type = self.get_proxy_type(request.url)
            self.put_default_to_list(proxy_type)
        if self.firstCrawl == 1:
            self.using_proxy_ip = self.get_proxy_ip_list(request.url, spider.name)
            self.firstCrawl = 0

        if self.using_proxy_ip != []:
            ip = random.choice(self.using_proxy_ip)
            if ip:
                print("use proxy url is [%s] and ip is [%s]" % (request.url,ip))
                request.meta['proxy'] = "http://" + ip


