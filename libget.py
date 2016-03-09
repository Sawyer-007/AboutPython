# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：成都信息工程大学图书馆爬虫
#   版本：1.0
#   作者：Saywer
#   日期：2015.5.8
#   语言：Python 2.7.9
#   操作：输入学号和密码
#   功能：获取图书应还日期
#---------------------------------------

import urllib  
import urllib2
import cookielib
from pyquery import PyQuery as pq
from lxml import etree

f = open('out.txt','a')

cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#设置浏览器信息#
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
headers = { 'User-Agent' : user_agent }  

#需要POST的数据#
value = {'number':'2013081221','passwd':'2013081221','select':'cert_no','returnUrl':''}
postdata=urllib.urlencode(value)

#自定义一个请求#
loginUrl = 'http://210.41.233.144:8080/reader/redr_verify.php'
req = urllib2.Request(loginUrl,postdata,headers)

#完成登录，此时进入读者信息界面#
loginResult = opener.open(req)

#打印返回的内容#
#f.write('=============================================================\n')
#f.write('Login Ok')
print 'Login Ok'

#打开借阅信息#
listUrl = 'http://210.41.233.144:8080/reader/book_lst.php'
listResult = opener.open(listUrl)

#============================================pyquery==============================================#

#打印返回的内容#
#f.write(listResult.read())

#d = pq(url = 'http://210.41.233.144:8080/reader/book_lst.php')
parserOne = pq(listResult.read())
parserTwo = pq(parserOne('table'))
i = 1
for data in parserTwo('tr'):
    if i :
        i = 0
    else:
        print pq(data).find('td').eq(0).text()
        print pq(data).find('td').eq(1).text()
        print pq(data).find('td').eq(2).text()
        print pq(data).find('td').eq(3).text()
        print pq(data).find('td').eq(4).text()
        #f.write(pq(data).find('td').eq(0).text()+'\n')
        #f.write(pq(data).find('td').eq(1).text()+'\n')
        #f.write(pq(data).find('td').eq(2).text()+'\n')
        #f.write(pq(data).find('td').eq(3).text()+'\n')
        #f.write(pq(data).find('td').eq(4).text()+'\n')
#f.close()