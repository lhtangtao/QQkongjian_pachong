#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = qqnews
#author = tangtao
#time   = 2017/2/8 10:35
#Description=添加描述信息
#eMail   =tangtao@lhtangtao.com
#git     =lhtangtao
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# 引入相关模块
import requests
from bs4 import BeautifulSoup
import json

url = "http://news.qq.com/"
# 请求腾讯新闻的URL，获取其text文本
wbdata = requests.get(url).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata, 'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")

# 对返回的列表进行遍历
for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = {
        '标题': title,
        '链接': link,

    }
    with open('haha.json', "a+") as f:
        f.write('\n')
        json.dump([data], f, ensure_ascii=False)
