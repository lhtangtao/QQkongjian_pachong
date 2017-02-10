#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = shuoshuo_cookies
#author = tangtao
#time   = 2017/2/10 14:13
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

import time

from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')
# 使用selenium
driver = webdriver.Chrome()
driver.maximize_window()


# 登录QQ空间
def get_shuoshuo(qq):
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
    time.sleep(2)
    driver.find_element_by_id('login_div')
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id("img_out_670076298").click()
    time.sleep(3)
    # 以下是登录后的cookies
    cookie = driver.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print('Cookies:', i)


if __name__ == '__main__':
    get_shuoshuo("670076298")
