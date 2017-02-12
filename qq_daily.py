#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用selenium
from selenium import webdriver
import time
import json
driver = webdriver.Chrome()
driver.maximize_window()

def get_daily(qq):
    driver.get('http://user.qzone.qq.com/{}/2'.format(qq))
    time.sleep(2)
    driver.find_element_by_id('login_div')
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id("img_out_670076298").click()
    time.sleep(5)
    driver.switch_to.frame('app_canvas_frame')
    last_page = int(driver.find_element_by_xpath("//a[6]").text)
    i = 0
    while i < last_page:
        content = driver.find_elements_by_css_selector('c_tx2')
        # stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con in zip(content):
            data = {
                u'内容': con.text,
            }
            with open('haha.json', "a+") as f:
                f.write('\n')
                json.dump([data], f, ensure_ascii=False)
        time.sleep(2)
        print i, last_page
        if int(i) + 1 != last_page:
            driver.find_element_by_link_text(u"下一页").click()
        i += 1
        time.sleep(3)
    print("==========完成================")
if __name__ == '__main__':
    get_daily("670076298")