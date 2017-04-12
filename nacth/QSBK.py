#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: v1.0
@author: fy
@site: 
@software: PyCharm
@file: QSBK.py
@time: 2017/4/10 17:21
"""
import urllib
import urllib2
import re
import thread
import time

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
        self.headers = {'User-Agent':self.user_agent}

        self.stories = []
        self.enable = False


    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因", e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode :
            print "页面加载失败。。。"
            return None

        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?'+
                             'content">(.*?)</div>(.*?).*?<div class="stats.*?class="number">(.*?)</i>', re.S)

        pageItems = re.findall(pattern, pageCode)

        pageStories = []

        for pageItem in pageItems:
            hasImg = re.search('img',pageItem[2])
            if not hasImg:
                pageStories.append([pageItem[0].strip(),pageItem[1].strip(),pageItem[3].strip()])

        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)

                if pageStories :
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self,pageStroies,pageIndex):
        for story in pageStroies:
            code = raw_input()
            self.loadPage()
            if code == 'Q':
                self.enable = False
                return

            print u"第%d页\t发布人:%s\t赞:%s\n%s" % (pageIndex, story[0],story[2], story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"

        self.enable = True
        self.loadPage()

        pageIndex = 0
        while self.enable :
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                # 当前读到的页数加一
                pageIndex += 1
                print pageIndex
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, pageIndex)



bk = QSBK()
bk.start()