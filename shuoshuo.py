#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = shuoshuo
#author = tangtao
#time   = 2017/2/7 17:43
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
type = sys.getfilesystemencoding()
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 使用selenium
driver = webdriver.Chrome()
driver.maximize_window()


# 登录QQ空间
def get_shuoshuo(qq):
    # driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
    driver.get("http://user.qzone.qq.com/670076298/311")
    time.sleep(2)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id("img_out_670076298").click()
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.switch_to.frame('app_canvas_frame')
    content = driver.find_elements_by_css_selector('.content')
    stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
    for con, sti in zip(content, stime):
        data = {
            'time': sti.text,
            'shuos': con
        }
        print(data)
    pages = driver.page_source
    soup = BeautifulSoup(pages, 'lxml')

    cookie = driver.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print('Cookies:', i)
    print("==========完成================")

    # driver.close()
    # driver.quit()


if __name__ == '__main__':
    get_shuoshuo('670076298')