from unicodedata import category
import requests
from bs4 import BeautifulSoup
import math

kategorie_data = {
    "니트": 'mglr',
    "바지": 'pntln',
    "셔츠": 'cmc',
    "블레이저": 'cmplt',
    "스커트": 'gnn',
    "원피스": 'vstt',
    "데님": 'jns',
    "코트": 'cpspll',
    '탑': 'tpwr',
}


def get_cloth_data(kategorie):
    #마지막 페이지
    last_page_number = get_cloth_count(kategorie)
    data = []
    # input last_page_number
    print(kategorie)
    for i in range(2):
        result = requests.get(f"https://www.yoox.com/kr/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98%20sale/shoponline#/dept=clothingwomensl&gender=D&page={i}&attributes=%7b%27ctgr%27%3a%5b%27{kategorie_data[kategorie]}%27%5d%7d&season=X")
        # Check for 200 OK response
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        product_grid = soup.find("div", {'id': 'srpage1'})
        products = product_grid.find_all("div", {'class': 'col-8-24'})

        # test += len(cloth_data.find_all("li"))
        for product in products:
            price_list = list(product.find('div', class_='price').get_text().strip().split('\n'))

            if len(price_list) != 2:
                continue
            #할인가 원화 일의 자리 반올림
            new_price = price_list[0].replace(')', '').split('(')
            new_price = new_price[1].replace('KRW ', '').split('.')
            new_price = round(int(new_price[0].replace(',', '')), -1)
            #정상가 원화 일의 자리 반올림
            old_price = price_list[1].replace(')', '').split('(')
            old_price = old_price[1].replace('KRW ', '').split('.')
            old_price = round(int(old_price[0].replace(',', '')), -1)
            
            brand = product.select('div')[0]['data-brand']
            category =  product.select('div')[0]['data-category']

            try:
                product_url = product.select('div')[0]['rel']
                image_url = product.select('img')[0]['src']
            except:
                continue

            data.append({"brand": brand, "category": category, "new_price(KWR)": new_price, "old_price(KWR)": old_price,"product_url": product_url,})
        return data


def get_cloth_count(kategorie):
    result = requests.get(f"https://www.yoox.com/kr/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98%20sale/shoponline#/dept=clothingwomensl&gender=D&page=1&attributes=%7b%27ctgr%27%3a%5b%27{kategorie_data[kategorie]}%27%5d%7d&season=X")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    pagination_list = soup.find("ul", class_="pagination list-inline pull-right text-center js-pagination").get_text().split()
    pagination_list = list(pagination_list)
    last_page = pagination_list[-1]

    return last_page


print(get_cloth_data(input()))


