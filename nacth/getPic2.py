#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: v1.0
@author: fy
@site: 
@software: PyCharm
@file: getPic2.py
@time: 2017/4/6 15:36
"""
import urllib2

def getHtml(html):
    request = urllib2.Request(html)
    response = urllib2.urlopen(request)
    return response.read()

print getHtml("http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html")