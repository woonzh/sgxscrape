# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:32:31 2018

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

chromepath='D:\stuff\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(chromepath)

driver.get("https://www2.sgx.com/securities/stock-screener")
time.sleep(5)

buts=driver.find_elements_by_xpath('//span[@class="action-btn"]')
buts[0].click()