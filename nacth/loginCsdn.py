#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: v1.0
@author: fy
@site: 
@software: PyCharm
@file: loginCsdn.py
@time: 2017/4/6 15:42
"""
import urllib
import urllib2
import re
import socket


def getQsbk(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?'+
                             'content">(.*?)</div>(.*?).*?<div class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
                print item[0], item[1],item[3]
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
socket.setdefaulttimeout(10)
for i in range(10):
    print  '----------------第%s页-------------------' % (i+1)
    getQsbk(i)