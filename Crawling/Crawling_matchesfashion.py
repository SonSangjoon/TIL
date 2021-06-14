from unicodedata import category
import requests
from bs4 import BeautifulSoup
import math
import re
import urllib.request
import time
import random
import os
#카테고리 
category_kor_to_eng = {
    "원피스": 'all-in-ones',
    "아우터": 'coats',
    "데님": 'denim',
    "긴치마": 'dresses',
    "자켓": 'jackets',
    "청바지": 'jeans',
    "긴팔상의": 'knitwear',
    "짧은바지": 'shorts',
    "짧은치마": 'skirts',
    "슈트": 'suits',
    "짧은상의": 'tops',
    "바지": 'trousers',
}

#쇼핑몰 크롤링
def get_cloth_data(kategorie):
    #페이지 수
    last_page_number = get_cloth_count(kategorie)
    data = []
    print(category_kor_to_eng[kategorie])

    #페이지별 크롤링
    for i in range(last_page_number):
        url =f"https://www.matchesfashion.com/en-kr/womens/apac-sale/clothing/{category_kor_to_eng[kategorie]}?page={i}&noOfRecordsPerPage=240&sort="
        custom_header = {
            'referer' : url,
            'Accept': '*/*', 
            'Accept-Encoding': 'gzip, deflate, br', 
            'Connection': 'keep-alive', 
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
            }
        req = requests.get(url, headers = custom_header)
        req.raise_for_status()
        #log 처리를 해주는 것이 좋다. 


        print(f"page - start: {i} / {last_page_number}")
        soup = BeautifulSoup(req.content, 'lxml')
        product_grid = soup.find("ul", {'class': 'lister__wrapper'})
        products = product_grid.find_all("li", {'class': 'lister__item'})
        cnt = 0

        #상품별 크롤링
        for product in products:
            cnt += 1
            len_product = len(products)
            print(f"item start: {cnt} / {len_product}")
            if cnt % 39 == 0 :
                time.sleep(0.2)
            else:
                time.sleep(random.random()/10)
            
            brand = product.find('div', class_='lister__item__title').get_text()
            item_detail = product.find('div', class_='lister__item__details').get_text()

            price = product.find('span', class_='lister__item__price-down').get_text()
            price = int(re.findall("\d+",price.replace(',',''))[0])
            original_price =  product.find('strike').get_text()
            original_price =int(re.findall("\d+",original_price.replace(',',''))[0])
            sale = math.floor((original_price-price)/original_price*100)

            product_url = "https://www.matchesfashion.com" + product.find('a')['href'].lstrip()
            image_url = "http://" +product.find('img')['data-original'][2:]
            
            image_static_url = download_image(image_url, brand, item_detail)

            data.append({"category": kategorie, "brand": brand, "item_detail" : item_detail,  "price(KWR)": price, "original_price(KWR)": original_price, 'sale': sale , "product_url": product_url, "image_url": image_url})
        
        return data


def get_cloth_count(kategorie):
    url = f"https://www.matchesfashion.com/en-kr/womens/apac-sale/clothing/{category_kor_to_eng[kategorie]}?page=1&noOfRecordsPerPage=240&sort="
    custom_header = {
        'referer' : url,
        'Accept': '*/*', 
        'Accept-Encoding': 'gzip, deflate, br', 
        'Connection': 'keep-alive', 
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }

    req = requests.get(url, headers = custom_header)
    req.raise_for_status()


    soup = BeautifulSoup(req.content, 'lxml')
    try: 
        max_page =max(re.findall("\d+",(soup.find("ul", class_="redefine__right__pager").get_text())))
        return int(max_page)
    except:
        return 1

def download_image(img_url, str_brand, str_item_detail):
    dir = '/Users/sangjoon/Downloads/crawling/'
    static_url = dir + str_brand + str_item_detail +'.jpg'
    # try:
    #     return urllib.request.urlretrieve(img_url, static_url )
    # except urllib.error.HTTPError as e:
    #     print('error')
    #     if e.code == 429:
    #          time.sleep(5);
    #          return download_image(img_url, str_brand, str_item_detail)
    #     raise
    # download_file = requests.get(img_url)
    # photo = open(static_url, 'wb')
    # photo.write(download_file.content)
    # photo.close()
    urllib.request.urlretrieve(img_url, static_url )
    # os.system("curl " + img_url + f" > /Users/sangjoon/Downloads/crawling/{str_brand}_{str_item_detail}_test.jpg")



    # return static_url


 