#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup
import requests

import pandas as pd
import csv
import math
from tqdm import tqdm

df = pd.read_excel('/solbook.xlsx')
df

options = webdriver.ChromeOptions() 
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #webdriver 객체 생성

publishers = []
book_names = []
inf_urls = []
inf_dates = []
    
for idx in tqdm(range(len(df))[:100]):
    publisher = df['출판사 명'][idx]
    book_name = df['교재명'][idx]
    
    publishers.append(publisher)
    book_names.append(book_name)
    
    query = f'{book_name} %26 첨부파일 %26 파일 다운로드'
    url = f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword={query}'

    driver.get(url)
    time.sleep(2)

    search_num = driver.find_element(By.CLASS_NAME, 'search_number').text
    pages = math.ceil(int(search_num[:-1].replace(',', ''))/7)
            
    links = []
    for page in range(1, pages+1):
        url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=ALL&orderBy=recentdate&keyword={query}'
        driver.get(url)
        time.sleep(2)
        try:
            for i in range(1,8):
                post = driver.find_element(By.CSS_SELECTOR, f'#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.desc > a.text')   
                links.append(post.get_attribute('href'))
        except:
            pass

    for link in links:
        driver.get(link)
        driver.switch_to.frame('mainFrame')
        try:
            file = driver.find_element(By.CLASS_NAME, 'se-component.se-file.se-l-default.__se-component')
        except:
            pass
        else:
            infringe = 0
            body = driver.find_element(By.CLASS_NAME, 'se-main-container').text
            if publisher in body:
                infringe += 1

            cnt = 0
            book_keywords = book_name.replace('(', ' ').replace(')', ' ').replace('  ', ' ').split(' ')
            for noun in book_keywords:
                if noun in body.split(' '):
                    cnt += 1
            if cnt >= (len(book_keywords))*0.8:
                infringe += 1

            if infringe:
                print(link)
                inf_urls.append(link)
                inf_dates.append(driver.find_element(By.CLASS_NAME, 'se_publishDate.pcol2').text)       

