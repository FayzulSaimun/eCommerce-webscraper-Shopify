import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

options = Options()
options.page_load_strategy = 'eager'
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)


def parse_data(url):
    name = []
    types = []
    prices = []
    ratings = []
    reviews = []
    image_link = []
    
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    product_body = soup.find_all('div', class_ = 'product-contents')
    for product in product_body:
        title = product.find('a', class_ = 'product-title').get_text().strip()
        prod_type = product.find('div', class_  = 'product-type').get_text().strip()
        price = product.find('div', class_ = 'product-price').get_text().strip()
        rating = product.find('span', class_ = 'sr-only').get_text().strip()
        review = product.find('a', class_ = 'text-m').get_text().strip()

        name.append(title)
        types.append(prod_type)
        prices.append(price)
        ratings.append(rating)
        reviews.append(review)


    df = pd.DataFrame({'Product Name':name, 'Product Type':prod_type,
                       'Price':prices,
                       'Reviews':reviews})
    df.to_csv('Kylie Cosmetics.csv', index = False)
    print(df.head(5))

parse_data('https://www.kyliecosmetics/collections/lips.com')    #you can change the url
