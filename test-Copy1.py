def get_infringe_naver_blog(info):
    publishers, book_names, inf_ids, inf_urls, inf_dates = [], [], [], [], []
    driver = open_browser()
    
    for i in tqdm(range(len(info[:100]))):
        publisher, book_name = info[i].split('|')[0], info[i].split('|')[1]
    
        query = f'{book_name} %26 첨부파일 %26 파일 다운로드' #f'{publisher} &26 {book_name} %26 첨부파일 %26 파일 다운로드'
        driver.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword={query}')
        driver.implicitly_wait(3)
        page_source = driver.page_source
        bs = BeautifulSoup(page_source, 'lxml')
        
        search_num = bs.find('em', {'class':'search_number'}).text
        pages = math.ceil(int(search_num[:-1].replace(',', ''))/7)

        links = []
        for page in range(1, pages+1):
            url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=ALL&orderBy=recentdate&keyword={query}'
            driver.get(url)
            driver.implicitly_wait(3)
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
            page_source = driver.page_source
            bs = BeautifulSoup(page_source, 'lxml')
            try:
                file = bs.find('div', {'class': 'se-module.se-module-file'})
            except:
                pass
            else:
                content = bs.find('div', {'class':'se-main-container'}).text
                infringe = is_infringe(publisher, book_name, content)
                
                if infringe:
                    publishers.append(publisher)
                    book_names.append(book_name)
                    inf_ids.append(link.split('/')[3] + '@naver.com')
                    inf_urls.append(link)
                    date_tag = bs.find('span', {'class': 'se_publishDate.pcol2'}).text
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