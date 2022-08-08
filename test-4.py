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
import multiprocessing
from multiprocessing import Pool

from bs4 import BeautifulSoup
import requests

import re
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

def is_infringe(publisher, book_name, content): #침해하지 않은 사례도 걸리는 문제..
    infringe = 0
    if publisher in content:
        infringe += 1

    cnt = 0 
    book_keywords = book_name.replace('(', ' ').replace(')', ' ').replace('  ', ' ').split(' ')
    for noun in book_keywords:
        if noun in content.split(' '):
            cnt += 1
    if cnt >= (len(book_keywords))*0.3:
        infringe += 1
        
    return infringe

def open_browser():
    options = webdriver.ChromeOptions() 
    options.add_argument('headless')
    options.add_argument("disable-gpu") 
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
    return driver

def get_infringe_naver_blog(info):
    publishers, book_names, inf_ids, inf_urls, inf_dates = [], [], [], [], []
    driver = open_browser()
    
    for i in tqdm(range(len(info[:100]))):
        publisher, book_name = info[i].split('|')[0], info[i].split('|')[1]
    
        query = f'{book_name} %26 첨부파일 %26 파일 다운로드' #f'{publisher} &26 {book_name} %26 첨부파일 %26 파일 다운로드'
        driver.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword={query}')
        time.sleep(0.5)
        page_source = driver.page_source
        bs = BeautifulSoup(page_source, 'lxml')

        search_num = bs.find('em', {'class':'search_number'}).text
        pages = math.ceil(int(search_num[:-1].replace(',', ''))/7)

        links = []
        for page in range(1, pages+1):
            url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=ALL&orderBy=recentdate&keyword={query}'
            driver.get(url)
            driver.implicitly_wait(3)
            time.sleep(0.5)
            page_source = driver.page_source
            bs = BeautifulSoup(page_source, 'lxml')
            try:
                post = bs.find_all('a', {'class': 'desc_inner'})
                links = [p['href'] for p in post]
            except:
                pass

        for link in links:
            driver.get(link)
            driver.switch_to.frame('mainFrame')
            time.sleep(0.5)
            page_source = driver.page_source
            bs = BeautifulSoup(page_source, 'lxml')
            
            if bs.find('div', {'class': 'se-module se-module-file'}) is not None:
                content = bs.find('div', {'id':'postListBody'}).text
                infringe = is_infringe(publisher, book_name, content)

                if infringe:
                    publishers.append(publisher)
                    book_names.append(book_name)
                    inf_ids.append(link.split('/')[3] + '@naver.com')
                    inf_urls.append(link)
                    date_tag = bs.find('span', {'class': 'se_publishDate pcol2'}).text
                    try:
                        date = datetime.strptime(date_tag, '%Y. %m. %d. %H:%M').strftime('%Y-%m-%d')
                    except:
                        date = datetime.now().strftime('%Y-%m-%d')
                    inf_dates.append(date)

    return publishers, book_names, inf_ids, inf_urls, inf_dates

if __name__ == '__main__':
    info_list = get_book_list('/home/ec2-user/solbook.xlsx')
    publishers, book_names, inf_ids, inf_urls, inf_dates = get_infringe_naver_blog(info_list)
    print(publishers, book_names, inf_ids, inf_urls, inf_dates)
