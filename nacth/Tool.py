#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: v1.0
@author: fy
@site: 
@software: PyCharm
@file: Tool.py
@time: 2017/4/12 9:26
"""
import re

class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|<p>')
    # 将表格制表<td>替换为\t
    replaceTd = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replaceP = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBr = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeOther = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTd,"\t",x)
        x = re.sub(self.replaceP,"\n",x)
        x = re.sub(self.replaceBr,"\n",x)
        x = re.sub(self.removeOther,"",x)
        return  x.strip()