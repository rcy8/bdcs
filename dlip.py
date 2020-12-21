# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
#from bs4 import BeautifulSoup
import requests
import os
#import pyperclip

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
#driver.maximize_window()
driver.set_window_size(1020,620)
url = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=800&picType=3'
driver.get(url)
driver.get_screenshot_as_file(r"工银黄金.png")
url = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=903&picType=3'
driver.get(url)
driver.get_screenshot_as_file("工银白银.png")