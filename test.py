# coding:utf-8

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")

assert u"百度" in browser.title

