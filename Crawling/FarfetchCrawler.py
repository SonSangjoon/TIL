import requests
from bs4 import BeautifulSoup
import math
import urllib.request

category_to_code = {
    "Denim": "136043",
    "Dresses": "135979",
    "Shorts": "136045",
    "Skirts": "135985",
    "Jumpsuits": "136253",
    "Jackets": "136226",
    "Coats": "136227",
    "Tops": "135983",
    "Trousers": "135981",
}

custom_header = {
    "referer": "https://www.farfetch.com/uk",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}


def check_last_page(amount_item: int):
    if amount_item != 90:
        return True
    else:
        return False


def download_product_image(image_url: str, item_detail: str):
    static_url = "/" + item_detail + ".jpg"
    urllib.request.urlretrieve(image_url, static_url)
    return static_url


def get_category_data(category_name: str, category_code: int):
    pagination = 1
    last_page = False
    category_data = []

    while not last_page:
        url = f"https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx?page={pagination}&view=90&code={category_code}"
        req = requests.get(url, headers=custom_header)
        soup = BeautifulSoup(req.content, "lxml")
        products = soup.find_all("li", {"data-testid": "productCard"})
        amount_item = len(products)

        if check_last_page(amount_item):
            last_page = True

        for product in products:
            product_brand = product.find("h3", {"data-testid": "productDesignerName"}).get_text()
            product_detail = product.find("p", {"data-testid": "productDescription"}).get_text()
            product_sale_price = product.find("span", {"data-testid": "price"}).get_text()
            product_sale_price = int(product_sale_price[1:].replace(",", ""))
            product_original_price = product.find(
                "span", {"data-testid": "initialPrice"}
            ).get_text()
            product_original_price = int(product_original_price[1:].replace(",", ""))
            product_sale_rate = (
                (product_original_price - product_sale_price) / product_sale_price * 100
            )
            adjusted_sale_rate = math.floor(product_sale_rate)
            product_url = "https://www.farfetch.com" + product.find("a")["href"].lstrip()
            product_image_url = product.find("meta")["content"]

            # download_product_image(product_image_url, product_detail)
            category_data.append(
                [
                    category_name,
                    product_brand,
                    product_detail,
                    product_sale_price,
                    product_original_price,
                    adjusted_sale_rate,
                    product_url,
                    product_image_url,
                ]
            )

        pagination += 1

    return category_data


def main():
    for category, code in category_to_code.items():
        get_category_data(category, code)
        print(category)


if __name__ == "__main__":
    main()
