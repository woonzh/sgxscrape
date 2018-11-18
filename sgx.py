# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pandas as pd

chromepath='D:\stuff\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(chromepath)
df=pd.DataFrame(columns=['names', 'last price', 'vol', 'val traded'])

def retrieveText(lst):
    store=[]
    for i in lst:
        string=i.text
#        print(string)
        store.append(string)
    
    return store

def extractData(df2):
    
    names=driver.find_elements_by_class_name('sgx-table-cell-security-name')
    lastPrice=driver.find_elements_by_xpath('//sgx-table-cell-number[@data-column-id="lt"]')
    vol=driver.find_elements_by_xpath('//sgx-table-cell-number[@data-column-id="vl"]')
    valTraded=driver.find_elements_by_xpath('//sgx-table-cell-number[@data-column-id="v"]')
    
    df=pd.DataFrame()
    df['names']=retrieveText(names)
    df['last price']=retrieveText(lastPrice)
    df['vol']=retrieveText(vol)
    df['val traded']=retrieveText(valTraded)
    
    df2=df2.append(df)
    df2=df2[df2['names']!='']
    return df2, df

driver.get("https://www2.sgx.com/securities/securities-prices")
time.sleep(0.5)

driver.find_element_by_xpath("//button[text()='OK']").click()
time.sleep(0.1)
driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
cont=driver.find_element_by_class_name('table-container')

driver.execute_script("window.scrollBy(0,300)")

lst=[]

df, df2 = extractData(df)
lst.append(df2)

option=driver.find_element_by_class_name("vertical-scrolling-bar")
actionChains = ActionChains(driver)

for j in range(30):
    actionChains.click_and_hold(option).move_by_offset(0,1).release().perform()
    time.sleep(0.2)
    
#    new_height = driver.execute_script("return arguments[0].scrollHeight", cont)
#    print(new_height)
    df, df2 = extractData(df)
    lst.append(df2)
    
df.drop_duplicates(subset ="names", keep = 'first', inplace = True)
