#!/usr/bin/env python
# coding: utf-8

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from bs4 import BeautifulSoup
import requests

import pandas as pd
import csv
import math
from tqdm.auto import tqdm

def get_book_list(path):
    df = pd.read_excel(path)
    info = []
    for idx in range(len(df)):
        info.append(str(df['출판사 명'][idx]) + '|' + str(df['교재명'][idx]))
    return info

def open_browser():
    options = webdriver.ChromeOptions() 
    options.add_argument('headless')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
    return driver

def is_infringe(publisher, book_name, content): #침해하지 않은 사례도 걸리는 문제..
    infringe = 0
    if publisher in content:
        infringe += 1

    cnt = 0 
    book_keywords = book_name.replace('(', ' ').replace(')', ' ').replace('  ', ' ').split(' ')
    for noun in book_keywords:
        if noun in content.split(' '):
            cnt += 1
    if cnt >= (len(book_keywords))*0.8:
        infringe += 1
        
    return infringe

def get_infringe_naver_blog(info):
    publishers, book_names, inf_ids, inf_urls, inf_dates = [], [], [], [], []
    driver = open_browser()
    
    for i in tqdm(range(len(info[:30]))):
        publisher, book_name = info[i].split('|')[0], info[i].split('|')[1]
    
        query = f'{book_name} %26 첨부파일 %26 파일 다운로드' #f'{publisher} &26 {book_name} %26 첨부파일 %26 파일 다운로드'
        driver.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword={query}')
        driver.implicitly_wait(3)

        search_num = driver.find_element(By.CLASS_NAME, 'search_number').text
        pages = math.ceil(int(search_num[:-1].replace(',', ''))/7)

        links = []
        for page in range(1, pages+1):
            url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=ALL&orderBy=recentdate&keyword={query}'
            driver.get(url)
            driver.implicitly_wait(3)
            try:
                for p in range(1,8):
                    post = driver.find_element(By.CSS_SELECTOR, f'#content > section > div.area_list_search > div:nth-child({p}) > div > div.info_post > div.desc > a.text')   
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
                content = driver.find_element(By.CLASS_NAME, 'se-main-container').text
                infringe = is_infringe(publisher, book_name, content)
                
                if infringe:
                    publishers.append(publisher)
                    book_names.append(book_name)
                    inf_ids.append(link.split('/')[3] + '@naver.com')
                    inf_urls.append(link)
                    date_tag = driver.find_element(By.CLASS_NAME, 'se_publishDate.pcol2').text
                    try:
                        date = datetime.strptime(date_tag, '%Y. %m. %d. %H:%M').strftime('%Y-%m-%d')
                    except:
                        date = datetime.now().strftime('%Y-%m-%d')
                    inf_dates.append(date) 

    return publishers, book_names, inf_ids, inf_urls, inf_dates

def get_infringe_naver_cafe(info):
    publishers, book_names, inf_urls, inf_dates = [], [], [], []
    driver = open_browser()
    for i in tqdm(range(len(info[:30]))):
        publisher, book_name = info[i].split('|')[0], info[i].split('|')[1]
        query = f'{book_name} %26 첨부파일 %26 파일 다운로드' #f'{publisher} &26 {book_name} %26 첨부파일 %26 파일 다운로드'
        driver.get(f'https://section.cafe.naver.com/ca-fe/home/search/articles?q={query}&od=1')
        time.sleep(1.5)

        search_num = driver.find_element(By.CLASS_NAME, 'total_count').text
        pages = math.ceil(int(search_num[:-1].replace(',', ''))/12)

        links = []
        for page in range(1, pages+1):
            url = f'https://section.cafe.naver.com/ca-fe/home/search/articles?q={query}&p={page}&od=1'
            driver.get(url)
            driver.implicitly_wait(3)
            try:
                for p in range(1,13):
                    post = driver.find_element(By.CSS_SELECTOR, f'#mainContainer > div > div.SectionSearchContent > div.section_search_content > div > div.article_list_area > ul > li:nth-child({p}) > div > div > div > a')   
                    links.append(post.get_attribute('href'))
            except:
                pass

        for link in links:
            driver.get(link)
            driver.switch_to.frame('cafe_main')
            try:
                file = driver.find_element(By.CLASS_NAME, 'se-module.se-module-file')
            except:
                pass
            else:
                content = driver.find_element(By.CLASS_NAME, 'se-main-container').text
                infringe = is_infringe(publisher, book_name, content)

                if infringe:
                    publishers.append(publisher)
                    book_names.append(book_name)
                    inf_urls.append(link)
                    date_tag = driver.find_element(By.CLASS_NAME, 'date').text
                    try:
                        date = datetime.strptime(date_tag, '%Y. %m. %d. %H:%M').strftime('%Y-%m-%d')
                    except:
                        date = datetime.now().strftime('%Y-%m-%d')
                    inf_dates.append(date) 


    return publishers, book_names, inf_urls, inf_dates

info_list = get_book_list('/home/ec2-user/solbook.xlsx')
publishers, book_names, inf_ids, inf_urls, inf_dates = get_infringe_naver_blog(info_list)
print(publishers, book_names, inf_ids, inf_urls, inf_dates)