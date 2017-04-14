# coding=utf-8
import re
import urllib
import os

def getHtml( url ):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg (html):
    reg = r'src="(data/attachment/forum/.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    #os.mkdir("D:\Img\\"+str(i))
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'D:\Img\%s.jpg' % x)
        x+=1
    return imglist

url = "http://www.photohn.com/bbs/forum.php?mod=viewthread&tid=475665"
html = getHtml(url)
print getImg(html)