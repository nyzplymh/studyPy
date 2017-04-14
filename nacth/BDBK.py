#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: v1.0
@author: fy
@site: 
@software: PyCharm
@file: BDBK.py
@time: 2017/4/11 16:38
"""
import urllib
import urllib2
import re
import Tool


class BDBK:

    def __init__(self,baseUrl,seeLZ,floorFlag):
        self.baseUrl = baseUrl
        self.seeLZ ='?seeLZ='+str(seeLZ)
        self.floorFlag = floorFlag
        self.tool = Tool.Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u"百度贴吧"


    def getPage(self,pageNum):
        try:
            url = self.baseUrl +self.seeLZ+'&pn='+str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return  response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print u'链接百度贴吧失败'+e.reason
                return None

    def getTitle(self,pageCode):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        title = re.search(pattern,pageCode)
        if title :
            print title.group(1)
            return title.group(1).strip()
        else :
            return None

    def getPageTotalNum(self,pageCode):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        totalNum = re.search(pattern,pageCode)
        if totalNum:
            print totalNum.group(1)
            return totalNum.group(1).strip()
        else:
            return None

    def getContent(self,pageCode):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        contentItems = re.findall(pattern,pageCode)
        if len(contentItems) > 0:
            contents =[]
            tmpFloor =self.floor
            for item in contentItems :
                print tmpFloor,u"楼----------------------------------------" \
                            u"-------------------\n"
                content = self.tool.replace(item)
                print content
                contents.append("\n"+content.encode('utf-8')+"\n")
                tmpFloor += 1
            return contents
        else :
            print "该帖子没有评论内容"
            return None
    def setFileTitle(self,title):
        if title is not None :
            self.file = open("d:\\"+title+".txt",'w+')
        else :
            self.file = open("d:\\"+self.defaultTitle+".txt",'w+')

    def writeData(self,contents):
        for content in contents :
            if self.floorFlag == '1':
                floorLine = '\n'+ str(self.floor) +u"---------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(content)
            self.floor += 1

    def start(self):
        page = self.getPage(1)
        pageNum = self.getPageTotalNum(page)
        title = self.getTitle(page)
        self.setFileTitle(title)

        if pageNum == None :
            print "链接已失效"
            return
        try:
            print "该帖子共有"+str(pageNum)+"页"
            for i in range(1,int(pageNum)+1):
                print "正在写入第"+str(i)+"页数据"
                contents = self.getContent(self.getPage(i))
                self.writeData(contents)
        except IOError,e:
            print "写入异常"+e.message
        finally:
            print "写入文件完毕"



print '请输入帖子代号'
baseUrl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否获取楼主发言 是输入 1 否输入0\n")
floorFalg = raw_input("是否显示楼层信息 是输入1 否输入0\n")
bdbk = BDBK(baseUrl,seeLZ,floorFalg)
bdbk.start()