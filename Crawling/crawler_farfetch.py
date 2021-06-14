from bs4 import BeautifulSoup
import requests
import json
import urllib.request


# url = "https://www.farfetch.com/uk/shopping/women/sale/all/"

url = "https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx?page=1&view=90&category=135983"

custom_header = {
    "referer": url,
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}


class ClothingCategory:
    def __init__(self, category_name: str, category_code: int):
        self.category_name = category_name
        self.category_code = category_code
        self.category_page = 1

    def get_page_number(self, url, custom_header):
        req = requests.get(url, headers=custom_header)
        soup = BeautifulSoup(req.content, "lxml")
        self.category_page = soup.find("div")
        return 


# class Product:
#     def __init__(self, item_category):
#         self.item_catagory = (item_category,)
#         self.item_brand = "brand"
#         self.item_detail = ""
#         self.item_original_price = ""
#         self.sale_rate = ""
#         self.thumbnail_url = ""
#         self.item_url = ""

#     def get_item_description(self, product: str):
#         self.brand = product.find("h3", {"data-testid": "productDesignerName"}).get_text()
#         self.item_detail = product.find("p", {"data-testid": "productDescription"}).get_text()
#         self.sale_price = product.find("span", {"data-testid": "price"}).get_text()
#         self.original_price = product.find("span", {"data-testid": "initialPrice"}).get_text()
#         self.thumbnail_url = "https://www.farfetch.com" + find("a")["href"].lstrip()
#         self.item_url = product.find("meta")["content"]

#     def get_item_sale_rate(self):
#         self.sale_rate = math.floor(
#             (self.original_price - self.sale_price) / self.original_price * 100
#         )

#     def download_image(sefl, img_url: str, item_detail: str):

#         static_url = item_detail.replace(" ", "") + ".jpg"
#         urllib.request.urlretrieve(img_url, static_url)

#         return static_url



def main():

    a = ClothingCategory("Denim", 135983)

    print(page)


if __name__ == "__main__":
    main()
